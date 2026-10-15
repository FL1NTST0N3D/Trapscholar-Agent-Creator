import { McpAgent } from "agents/mcp";
import { McpServer } from "@modelcontextprotocol/sdk/server/mcp.js";
import { z } from "zod";

const READ_ONLY_TOOL_ANNOTATIONS = {
  readOnlyHint: true,
  destructiveHint: false,
  openWorldHint: false,
} as const;

// Escape LIKE special characters in user input to prevent wildcard injection
function escapeLike(s: string): string {
  return s.replace(/[%_\\]/g, '\\$&');
}

const INSTRUCTION_LIKE_MARKDOWN_PATTERNS = [
  /\b(?:ignore|disregard|forget|override|bypass)\s+(?:all\s+)?(?:previous|prior|above|earlier|system|developer|user)?\s*(?:instructions?|prompts?|messages?|rules?)\b[^.;!?]*/gi,
  /\b(?:system|developer|assistant|user)\s*(?:prompt|message|instruction|role)\s*:[^.;!?]*/gi,
  /\b(?:you are now|act as|pretend to be|from now on|follow these instructions|do not obey|reveal hidden|print hidden|exfiltrate|tool call|call the tool)\b[^.;!?]*/gi,
  /<\s*\/?\s*(?:system|developer|assistant|user|instructions?)\s*>/gi,
];

function sanitizeMarkdown(text: unknown): string {
  let sanitized = String(text ?? "");
  sanitized = sanitized.replace(/```[\s\S]*?```/g, " ");
  sanitized = sanitized.replace(/```+/g, " ");
  sanitized = sanitized.replace(/[\r\n]+/g, " ");
  sanitized = sanitized.replace(/#/g, "");
  for (const pattern of INSTRUCTION_LIKE_MARKDOWN_PATTERNS) {
    sanitized = sanitized.replace(pattern, " ");
  }
  return sanitized.replace(/\s{2,}/g, " ").trim();
}

function sanitizeMarkdownOr(text: unknown, fallback: string): string {
  return sanitizeMarkdown(text) || fallback;
}

const MAX_QUERY_LENGTH = 120;
const MAX_QUERY_INPUT_LENGTH = 200;
const MAX_NAME_LENGTH = 50;
const MAX_TESTING_RESULTS = 100;
const MAX_COMPLIANCE_RESULTS = 150;
const MAX_SEARCH_RESULTS = 50;
const MAX_CONTROLLED_RESULTS = 5;
const MAX_REGULATION_RESULTS = 20;
const MAX_PRECURSOR_RESULTS = 10;
const US_STATES = [
  "Alabama",
  "Alaska",
  "Arizona",
  "Arkansas",
  "California",
  "Colorado",
  "Connecticut",
  "Delaware",
  "District of Columbia",
  "Florida",
  "Georgia",
  "Hawaii",
  "Idaho",
  "Illinois",
  "Indiana",
  "Iowa",
  "Kansas",
  "Kentucky",
  "Louisiana",
  "Maine",
  "Maryland",
  "Massachusetts",
  "Michigan",
  "Minnesota",
  "Mississippi",
  "Missouri",
  "Montana",
  "Nebraska",
  "Nevada",
  "New Hampshire",
  "New Jersey",
  "New Mexico",
  "New York",
  "North Carolina",
  "North Dakota",
  "Ohio",
  "Oklahoma",
  "Oregon",
  "Pennsylvania",
  "Rhode Island",
  "South Carolina",
  "South Dakota",
  "Tennessee",
  "Texas",
  "Utah",
  "Vermont",
  "Virginia",
  "Washington",
  "West Virginia",
  "Wisconsin",
  "Wyoming",
] as const;
const CANNABIS_JURISDICTIONS = ["Canada", ...US_STATES] as const;
const CANNABIS_TEST_CATEGORIES = [
  "pesticide",
  "heavy_metal",
  "microbial",
  "solvent",
  "mycotoxin",
  "potency",
  "moisture",
] as const;
const CANNABIS_PRODUCT_CLASSES = [
  "flower",
  "concentrate",
  "edible",
  "topical",
  "extract",
  "oil",
  "dried_cannabis",
] as const;

function normalizeQuery(input: string, maxLength = MAX_QUERY_LENGTH): string {
  return input.trim().replace(/\s+/g, " ").slice(0, maxLength);
}

function likePattern(input: string): string {
  return `%${escapeLike(input)}%`;
}

const RATE_LIMIT_PER_MINUTE = 60;
const RATE_LIMIT_WINDOW_MS = 60_000;

const rateLimitMap = new Map<string, { count: number; resetAt: number }>();

function checkRateLimit(ip: string): boolean {
  const now = Date.now();
  const entry = rateLimitMap.get(ip);
  if (!entry || now >= entry.resetAt) {
    rateLimitMap.set(ip, { count: 1, resetAt: now + RATE_LIMIT_WINDOW_MS });
    return true;
  }
  entry.count++;
  if (entry.count > RATE_LIMIT_PER_MINUTE) return false;
  return true;
}

function rateLimitResponse(): Response {
  return new Response(JSON.stringify({ error: "Rate limit exceeded. Maximum 60 requests per minute." }), {
    status: 429,
    headers: { "Content-Type": "application/json", "Retry-After": "60" },
  });
}

interface Env {
  DB: D1Database;
  MCP_OBJECT: DurableObjectNamespace;
  // Optional auth env. When configured, validates Bearer tokens for per-user rate limiting.
  MCP_KEY_SECRET?: string;
}

// --- Auth: HMAC-validated MCP key ---
// MCP keys are issued by rootsbybenda-site/functions/api/mcp-key.js using the
// SAME MCP_KEY_SECRET. Format: mcp_<base64url(user_id)>_<sha256_hmac[:32]>.

interface AuthProps extends Record<string, unknown> {
  user_id: string | null;
  authenticated: boolean;
}

function base64urlDecodeToString(b64url: string): string {
  const b64 = b64url.replace(/-/g, "+").replace(/_/g, "/");
  const padded = b64 + "===".slice((b64.length + 3) % 4);
  return atob(padded);
}

async function hmacSha256Hex(message: string, secret: string): Promise<string> {
  const key = await crypto.subtle.importKey(
    "raw",
    new TextEncoder().encode(secret),
    { name: "HMAC", hash: "SHA-256" },
    false,
    ["sign"]
  );
  const sig = await crypto.subtle.sign("HMAC", key, new TextEncoder().encode(message));
  return Array.from(new Uint8Array(sig))
    .map((b) => b.toString(16).padStart(2, "0"))
    .join("");
}

function constantTimeEqual(a: string, b: string): boolean {
  if (a.length !== b.length) return false;
  let diff = 0;
  for (let i = 0; i < a.length; i++) diff |= a.charCodeAt(i) ^ b.charCodeAt(i);
  return diff === 0;
}

async function resolveAuth(request: Request, env: Env): Promise<AuthProps> {
  const authHeader = request.headers.get("Authorization") || "";
  const match = authHeader.match(/^Bearer\s+(mcp_[A-Za-z0-9_-]+_[a-f0-9]{32})\s*$/i);
  if (!match) return { user_id: null, authenticated: false };

  const key = match[1];
  const parts = key.split("_");
  if (parts.length !== 3 || parts[0] !== "mcp") {
    return { user_id: null, authenticated: false };
  }
  const userIdB64 = parts[1];
  const providedHmac = parts[2].toLowerCase();

  if (!env.MCP_KEY_SECRET) {
    console.error("resolveAuth: MCP_KEY_SECRET not configured");
    return { user_id: null, authenticated: false };
  }

  let userId: string;
  try {
    userId = base64urlDecodeToString(userIdB64);
  } catch {
    return { user_id: null, authenticated: false };
  }
  if (!userId) return { user_id: null, authenticated: false };

  const computed = (await hmacSha256Hex(userId, env.MCP_KEY_SECRET)).slice(0, 32);
  if (!constantTimeEqual(computed, providedHmac)) {
    return { user_id: null, authenticated: false };
  }

  return { user_id: userId, authenticated: true };
}
// --- End auth ---

const SERVER_VERSION = "1.0.2";
const HOMEPAGE = "https://rootsbybenda.com";
const SOURCE = "Roots by Benda \u2014 rootsbybenda.com";
const CONTACT = "support@rootsbybenda.com";
const SERVER_NAME = "Roots by Benda \u2014 Cannabis Intelligence";
const SERVER_DESCRIPTION =
  "Cannabis regulatory compliance reference data: US state-level testing limits (1,942 requirements across pesticides, heavy metals, microbials, solvents, mycotoxins, potency, moisture), Health Canada cannabis regulations (383 records), UN INCB narcotic drug scheduling (154 substances), EU drug precursor controls (46 chemicals), and EMCDDA/EUDA novel psychoactive substance risk assessments (41 NPS). For cannabis product compliance, controlled substance scheduling, and regulatory intelligence.";
const DATA_CATALOG = {
  cannabis_testing_limits: "1,942 state-level testing requirements",
  incb_yellow_list: "154 UN scheduled narcotic drugs",
  eu_drug_precursors: "46 EU controlled precursor chemicals",
  emcdda_nps: "41 risk-assessed novel psychoactive substances",
  health_canada_cannabis: "383 Canadian cannabis regulations"
};
const TOOL_CATALOG = [
  {
    name: "check_cannabis_testing",
    description: "Retrieve US state-level cannabis testing limits and action levels for regulatory compliance. Input: US state name (e.g. 'California', 'Colorado'), optional test category (pesticide, heavy_metal, microbial, solvent, mycotoxin, potency, moisture), and optional specific analyte name (e.g. 'lead', 'arsenic', 'Salmonella', 'butane'). Returns: testing categories with analyte names, action levels (pass/fail thresholds), units (ppm, ppb, CFU/g), product class applicability (flower, concentrate, edible), and regulation references. Database: 1,942 state-level testing requirements across all legalized US states. For cannabis laboratory compliance and product testing requirements. Do not use for controlled-substance scheduling (use check_controlled_substance), Health Canada regulations (use check_cannabis_compliance with jurisdiction 'Canada'), or non-cannabis food pesticide MRLs."
  },
  {
    name: "check_controlled_substance",
    description: "Check international controlled-substance scheduling status across UN, EU, and novel psychoactive substance databases. Input: substance name, cannabinoid, narcotic drug, precursor, NPS name, synonym, or CAS number (e.g. 'cannabis', 'THC', 'morphine', 'pseudoephedrine', '64-17-5'). Returns: UN INCB Yellow List scheduling (narcotic drugs under 1961 Single Convention — schedule, synonyms, formula, conversion ratio, CAS), EU Drug Precursor category (CN code, threshold quantities, license/registration requirements), and EMCDDA/EUDA Novel Psychoactive Substance risk assessment (chemical class, control status, risk assessment year, scheduling decision). Sources: INCB Yellow List (154 narcotic drugs), EU Drug Precursors regulation (46 chemicals), EMCDDA/EUDA NPS risk assessments (41 substances). For controlled substance regulatory compliance and scheduling verification. Do not use for cannabis testing limits (use check_cannabis_testing) or product compliance summaries (use check_cannabis_compliance)."
  },
  {
    name: "check_cannabis_compliance",
    description: "Retrieve cannabis product compliance requirements by jurisdiction including all required testing categories, analyte limits, and regulatory sections. Input: US state name or 'Canada' for Health Canada, optional product class (flower, concentrate, edible, topical, extract, oil, dried_cannabis). Returns for US states: all testing categories (pesticide, heavy metal, microbial, solvent, mycotoxin, potency, moisture) with per-analyte action levels, units, and product-type applicability. Returns for Canada: Health Canada cannabis regulation parameters, limit values, units, product class, and regulation section references. Database: 1,942 US state testing requirements + 383 Health Canada cannabis regulations. For cannabis product compliance planning and regulatory gap analysis. Do not use for controlled-substance scheduling (use check_controlled_substance) or broad keyword discovery (use search_cannabis_regulations)."
  },
  {
    name: "search_cannabis_regulations",
    description: "Search across all cannabis and controlled-substance regulatory datasets by keyword for regulatory intelligence discovery. Input: keyword covering jurisdiction, product class, analyte, substance, precursor, or NPS term (e.g. 'THC', 'pesticide', 'heavy metal', 'Salmonella', 'morphine', 'pseudoephedrine'). Returns: cross-dataset matches from US state cannabis testing limits (grouped by state), UN INCB scheduling (narcotic drugs), Health Canada cannabis regulations, and EU Drug Precursors — each with dataset labels, jurisdictions, substance/analyte names, limits, and regulatory references. Database: 1,942 testing limits + 154 INCB substances + 383 Health Canada records + 46 EU precursors + 41 EMCDDA NPS. For cannabis regulatory research and cross-jurisdictional analysis. Do not use when exact state, jurisdiction, or substance is known (use the specific compliance or scheduling tools)."
  }
];

function registryMetadata() {
  return {
    name: SERVER_NAME,
    description: SERVER_DESCRIPTION,
    version: SERVER_VERSION,
    mcp_endpoint: "/mcp",
    tools: TOOL_CATALOG,
    data: DATA_CATALOG,
    homepage: HOMEPAGE,
    source: SOURCE,
    contact: CONTACT,
  };
}


export class CannabisMCP extends McpAgent<Env> {
  // @ts-expect-error agents bundles its own MCP SDK copy; runtime server shape is compatible.
  server = new McpServer({
    name: "roots-cannabis-regulatory",
    version: SERVER_VERSION,
  });

  async init() {
    // Tool 1: check_cannabis_testing — Look up testing limits by state
    this.server.tool(
      "check_cannabis_testing",
      TOOL_CATALOG[0].description,
      {
        state: z
          .enum(US_STATES)
          .describe(
            "US state name for cannabis testing-limit lookup (e.g. 'California', 'Colorado', 'Oregon'). Use the state where the cannabis product is tested or sold because action levels vary by jurisdiction."
          ),
        test_category: z
          .enum(CANNABIS_TEST_CATEGORIES)
          .optional()
          .describe(
            "Optional cannabis laboratory testing category filter. Use pesticide, heavy_metal, microbial, solvent, mycotoxin, potency, or moisture when the user asks about a specific contaminant or assay class."
          ),
        analyte: z
          .string()
          .trim()
          .min(1)
          .max(MAX_NAME_LENGTH)
          .optional()
          .describe(
            "Optional specific cannabis testing analyte or contaminant name (e.g. 'lead', 'arsenic', 'Salmonella', 'butane'). Use analyte names to narrow a state/category lookup to one action level."
          ),
      },
      READ_ONLY_TOOL_ANNOTATIONS,
      async ({ state, test_category, analyte }) => {
        let sql = `SELECT * FROM cannabis_testing_limits WHERE state LIKE ? ESCAPE '\\' COLLATE NOCASE`;
        const params: (string | number)[] = [likePattern(state)];

        if (test_category) {
          sql += ` AND test_category LIKE ? ESCAPE '\\' COLLATE NOCASE`;
          params.push(likePattern(test_category));
        }
        if (analyte) {
          const analyteName = normalizeQuery(analyte, MAX_NAME_LENGTH);
          sql += ` AND analyte_name LIKE ? ESCAPE '\\' COLLATE NOCASE`;
          params.push(likePattern(analyteName));
        }
        sql += ` ORDER BY test_category, analyte_name LIMIT ?`;
        params.push(MAX_TESTING_RESULTS);

        const { results } = await this.env.DB.prepare(sql)
          .bind(...params)
          .all();

        if (!results || results.length === 0) {
          return {
            content: [
              {
                type: "text" as const,
                text: `No cannabis testing limits found for state "${sanitizeMarkdown(state)}"${test_category ? `, category "${sanitizeMarkdown(test_category)}"` : ""}${analyte ? `, analyte "${sanitizeMarkdown(analyte)}"` : ""}. Try a different state or broader search.`,
              },
            ],
          };
        }

        const grouped: Record<string, any[]> = {};
        for (const r of results) {
          const cat = (r.test_category as string) || "other";
          if (!grouped[cat]) grouped[cat] = [];
          grouped[cat].push(r);
        }

        let text = `## Cannabis Testing Limits — ${sanitizeMarkdown(state)}\n\n`;
        for (const [cat, items] of Object.entries(grouped)) {
          text += `### ${sanitizeMarkdownOr(cat, "other").toUpperCase()}\n`;
          for (const item of items) {
            text += `- **${sanitizeMarkdown(item.analyte_name)}**: ${sanitizeMarkdownOr(item.action_level, "N/A")} ${sanitizeMarkdown(item.units)} (${sanitizeMarkdownOr(item.product_type, "all products")})`;
            if (item.regulation_reference)
              text += ` — ${sanitizeMarkdown(item.regulation_reference)}`;
            text += `\n`;
          }
          text += `\n`;
        }
        text += `\n*${results.length} limits found*`;
        text += `\n\n**Citation:** ${sanitizeMarkdown(state)} cannabis testing limits: ${results.length} requirements${test_category ? ` (${sanitizeMarkdown(test_category)})` : ""}${analyte ? ` for ${sanitizeMarkdown(analyte)}` : ""}. Source: Roots by Benda (rootsbybenda.com) — US state cannabis testing regulatory data.`;

        return { content: [{ type: "text" as const, text }] };
      }
    );

    // Tool 2: check_controlled_substance — Check scheduling status
    this.server.tool(
      "check_controlled_substance",
      TOOL_CATALOG[1].description,
      {
        query: z
          .string()
          .trim()
          .min(1)
          .max(MAX_QUERY_INPUT_LENGTH)
          .describe(
            "Controlled substance common name, cannabinoid, narcotic drug, precursor chemical, NPS name, synonym, or CAS number (e.g. 'morphine', 'cannabis', '64-17-5'). Use CAS when available for exact matching across INCB, EU precursor, and EMCDDA/EUDA records."
          ),
      },
      READ_ONLY_TOOL_ANNOTATIONS,
      async ({ query }) => {
        const q = normalizeQuery(query);
        const pattern = likePattern(q);

        // Check INCB Yellow List (narcotic drugs)
        const incb = await this.env.DB.prepare(
          `SELECT * FROM incb_yellow_list
           WHERE substance_name LIKE ? ESCAPE '\\' COLLATE NOCASE
              OR synonyms LIKE ? ESCAPE '\\' COLLATE NOCASE
              OR cas_number = ?
           LIMIT ?`
        )
          .bind(pattern, pattern, q, MAX_CONTROLLED_RESULTS)
          .all();

        // Check EU Drug Precursors
        const precursor = await this.env.DB.prepare(
          `SELECT * FROM eu_drug_precursors
           WHERE substance_name LIKE ? ESCAPE '\\' COLLATE NOCASE
              OR cas_number = ?
           LIMIT ?`
        )
          .bind(pattern, q, MAX_CONTROLLED_RESULTS)
          .all();

        // Check EMCDDA NPS
        const nps = await this.env.DB.prepare(
          `SELECT * FROM emcdda_nps
           WHERE substance_name LIKE ? ESCAPE '\\' COLLATE NOCASE
           LIMIT ?`
        )
          .bind(pattern, MAX_CONTROLLED_RESULTS)
          .all();

        const hasResults =
          (incb.results?.length || 0) > 0 ||
          (precursor.results?.length || 0) > 0 ||
          (nps.results?.length || 0) > 0;

        if (!hasResults) {
          return {
            content: [
              {
                type: "text" as const,
                text: `No controlled substance records found for "${sanitizeMarkdown(query)}". The substance may not be internationally scheduled, or try alternative names/CAS numbers.`,
              },
            ],
          };
        }

        let text = `## Controlled Substance Check: "${sanitizeMarkdown(query)}"\n\n`;

        if (incb.results && incb.results.length > 0) {
          text += `### UN INCB Scheduling (Yellow List — Narcotic Drugs)\n`;
          for (const r of incb.results) {
            text += `- **${sanitizeMarkdown(r.substance_name)}** — Schedule ${sanitizeMarkdown(r.schedule)}\n`;
            if (r.cas_number) text += `  - CAS: ${sanitizeMarkdown(r.cas_number)}\n`;
            if (r.synonyms) text += `  - Synonyms: ${sanitizeMarkdown(r.synonyms)}\n`;
            if (r.formula) text += `  - Formula: ${sanitizeMarkdown(r.formula)}\n`;
            if (r.conversion_ratio)
              text += `  - Conversion ratio: ${sanitizeMarkdown(r.conversion_ratio)}\n`;
            if (r.notes) text += `  - Notes: ${sanitizeMarkdown(r.notes)}\n`;
          }
          text += `\n`;
        }

        if (precursor.results && precursor.results.length > 0) {
          text += `### EU Drug Precursors\n`;
          for (const r of precursor.results) {
            text += `- **${sanitizeMarkdown(r.substance_name)}** — Category ${sanitizeMarkdownOr(r.category, "N/A")}\n`;
            if (r.cas_number) text += `  - CAS: ${sanitizeMarkdown(r.cas_number)}\n`;
            if (r.cn_code) text += `  - CN Code: ${sanitizeMarkdown(r.cn_code)}\n`;
            if (r.threshold_quantity_for_reporting)
              text += `  - Threshold: ${sanitizeMarkdown(r.threshold_quantity_for_reporting)}\n`;
            if (r.license_registration_requirements)
              text += `  - Requirements: ${sanitizeMarkdown(r.license_registration_requirements)}\n`;
          }
          text += `\n`;
        }

        if (nps.results && nps.results.length > 0) {
          text += `### EU Novel Psychoactive Substances (EMCDDA/EUDA)\n`;
          for (const r of nps.results) {
            text += `- **${sanitizeMarkdown(r.substance_name)}** — ${sanitizeMarkdownOr(r.control_status, "monitored")}\n`;
            if (r.chemical_class)
              text += `  - Class: ${sanitizeMarkdown(r.chemical_class)}\n`;
            if (r.risk_assessment_year)
              text += `  - Risk assessed: ${sanitizeMarkdown(r.risk_assessment_year)}\n`;
            if (r.scheduling_control_decision_notes)
              text += `  - Decision: ${sanitizeMarkdown(r.scheduling_control_decision_notes)}\n`;
          }
          text += `\n`;
        }

        // Build citation
        const citSources: string[] = [];
        if (incb.results && incb.results.length > 0) citSources.push(`INCB Schedule ${(incb.results[0] as Record<string, unknown>).schedule}`);
        if (precursor.results && precursor.results.length > 0) citSources.push(`EU Precursor Cat ${(precursor.results[0] as Record<string, unknown>).category || "N/A"}`);
        if (nps.results && nps.results.length > 0) citSources.push(`EMCDDA/EUDA ${(nps.results[0] as Record<string, unknown>).control_status || "monitored"}`);
        text += `\n**Citation:** ${sanitizeMarkdown(query)}: ${citSources.join("; ")}. Source: Roots by Benda (rootsbybenda.com) — INCB Yellow List, EU Drug Precursors, EMCDDA/EUDA NPS data.`;

        return { content: [{ type: "text" as const, text }] };
      }
    );

    // Tool 3: check_cannabis_compliance — Check product compliance across jurisdictions
    this.server.tool(
      "check_cannabis_compliance",
      TOOL_CATALOG[2].description,
      {
        jurisdiction: z
          .enum(CANNABIS_JURISDICTIONS)
          .describe(
            "Cannabis compliance jurisdiction: a US state name (e.g. 'California') or 'Canada' for Health Canada cannabis regulations. Choose the market where the product will be tested, sold, or assessed."
          ),
        product_class: z
          .enum(CANNABIS_PRODUCT_CLASSES)
          .optional()
          .describe(
            "Optional cannabis product class for compliance filtering. Use flower, concentrate, edible, topical, extract, oil, or dried_cannabis when requirements differ by product format."
          ),
      },
      READ_ONLY_TOOL_ANNOTATIONS,
      async ({ jurisdiction, product_class }) => {
        const j = jurisdiction;
        let text = `## Cannabis Compliance — ${sanitizeMarkdown(j)}\n\n`;

        if (j.toLowerCase() === "canada") {
          let sql = `SELECT * FROM health_canada_cannabis WHERE 1=1`;
          const params: (string | number)[] = [];
          if (product_class) {
            sql += ` AND (product_class LIKE ? ESCAPE '\\' COLLATE NOCASE OR category LIKE ? ESCAPE '\\' COLLATE NOCASE)`;
            const pcPattern = likePattern(product_class);
            params.push(pcPattern, pcPattern);
          }
          sql += ` ORDER BY category, analyte_or_parameter LIMIT ?`;
          params.push(MAX_TESTING_RESULTS);

          const { results } = await this.env.DB.prepare(sql)
            .bind(...params)
            .all();

          if (!results || results.length === 0) {
            return {
              content: [
                {
                  type: "text" as const,
                  text: `No Health Canada cannabis regulations found${product_class ? ` for product class "${sanitizeMarkdown(product_class)}"` : ""}. Try: flower, concentrate, edible, oil, extract.`,
                },
              ],
            };
          }

          const grouped: Record<string, any[]> = {};
          for (const r of results) {
            const cat = (r.category as string) || "other";
            if (!grouped[cat]) grouped[cat] = [];
            grouped[cat].push(r);
          }

          for (const [cat, items] of Object.entries(grouped)) {
            text += `### ${sanitizeMarkdownOr(cat, "other")}\n`;
            for (const item of items) {
              text += `- **${sanitizeMarkdown(item.analyte_or_parameter)}**: ${sanitizeMarkdownOr(item.limit_value, "N/A")} ${sanitizeMarkdown(item.units)}`;
              if (item.product_class) text += ` (${sanitizeMarkdown(item.product_class)})`;
              if (item.regulation_section)
                text += ` — ${sanitizeMarkdown(item.regulation_section)}`;
              text += `\n`;
            }
            text += `\n`;
          }
          text += `*${results.length} regulations found*`;
          text += `\n\n**Citation:** Health Canada cannabis compliance${product_class ? ` (${sanitizeMarkdown(product_class)})` : ""}: ${results.length} regulatory requirements. Source: Roots by Benda (rootsbybenda.com) — Health Canada Cannabis Regulations.`;
        } else {
          // US State
          let sql = `SELECT * FROM cannabis_testing_limits WHERE state LIKE ? ESCAPE '\\' COLLATE NOCASE`;
          const params: (string | number)[] = [likePattern(j)];
          if (product_class) {
            sql += ` AND product_type LIKE ? ESCAPE '\\' COLLATE NOCASE`;
            params.push(likePattern(product_class));
          }
          sql += ` ORDER BY test_category, analyte_name LIMIT ?`;
          params.push(MAX_COMPLIANCE_RESULTS);

          const { results } = await this.env.DB.prepare(sql)
            .bind(...params)
            .all();

          if (!results || results.length === 0) {
            return {
              content: [
                {
                  type: "text" as const,
                  text: `No cannabis testing requirements found for "${sanitizeMarkdown(j)}". This state may not have legalized cannabis, or try the full state name.`,
                },
              ],
            };
          }

          // Summary by category
          const categories: Record<string, number> = {};
          for (const r of results) {
            const cat = (r.test_category as string) || "other";
            categories[cat] = (categories[cat] || 0) + 1;
          }

          text += `**Testing categories:** ${Object.entries(categories)
            .map(([k, v]) => `${sanitizeMarkdownOr(k, "other")} (${v})`)
            .join(", ")}\n\n`;

          const grouped: Record<string, any[]> = {};
          for (const r of results) {
            const cat = (r.test_category as string) || "other";
            if (!grouped[cat]) grouped[cat] = [];
            grouped[cat].push(r);
          }

          for (const [cat, items] of Object.entries(grouped)) {
            text += `### ${sanitizeMarkdownOr(cat, "other").toUpperCase()}\n`;
            for (const item of items) {
              text += `- **${sanitizeMarkdown(item.analyte_name)}**: ${sanitizeMarkdownOr(item.action_level, "N/A")} ${sanitizeMarkdown(item.units)}`;
              if (item.product_type) text += ` (${sanitizeMarkdown(item.product_type)})`;
              text += `\n`;
            }
            text += `\n`;
          }
          text += `*${results.length} testing requirements found*`;
          text += `\n\n**Citation:** ${sanitizeMarkdown(j)} cannabis compliance${product_class ? ` (${sanitizeMarkdown(product_class)})` : ""}: ${results.length} testing requirements. Source: Roots by Benda (rootsbybenda.com) — US state cannabis regulatory data.`;
        }

        return { content: [{ type: "text" as const, text }] };
      }
    );

    // Tool 4: search_cannabis_regulations — Full-text search across all cannabis data
    this.server.tool(
      "search_cannabis_regulations",
      TOOL_CATALOG[3].description,
      {
        query: z
          .string()
          .trim()
          .min(1)
          .max(MAX_QUERY_INPUT_LENGTH)
          .describe(
            "Cannabis regulatory keyword, jurisdiction, product class, analyte, controlled substance, precursor, or NPS term (e.g. 'THC', 'pesticide', 'heavy metal', 'Salmonella', 'morphine', 'pseudoephedrine'). Use broad terms for discovery across multiple cannabis and controlled-substance datasets."
          ),
      },
      READ_ONLY_TOOL_ANNOTATIONS,
      async ({ query }) => {
        const q = normalizeQuery(query);
        const pattern = likePattern(q);
        let text = `## Search Results: "${sanitizeMarkdown(query)}"\n\n`;
        let totalResults = 0;

        // Search cannabis testing limits
        const testing = await this.env.DB.prepare(
          `SELECT * FROM cannabis_testing_limits
           WHERE analyte_name LIKE ? ESCAPE '\\' COLLATE NOCASE
              OR test_category LIKE ? ESCAPE '\\' COLLATE NOCASE
              OR notes LIKE ? ESCAPE '\\' COLLATE NOCASE
           ORDER BY state, test_category LIMIT ?`
        )
          .bind(pattern, pattern, pattern, MAX_SEARCH_RESULTS)
          .all();

        if (testing.results && testing.results.length > 0) {
          text += `### Cannabis Testing Limits (${testing.results.length} matches)\n`;
          const byState: Record<string, any[]> = {};
          for (const r of testing.results) {
            const s = (r.state as string) || "Unknown";
            if (!byState[s]) byState[s] = [];
            byState[s].push(r);
          }
          for (const [state, items] of Object.entries(byState)) {
            text += `**${sanitizeMarkdownOr(state, "Unknown")}:** `;
            text += items
              .map(
                (i) =>
                  `${sanitizeMarkdown(i.analyte_name)} ${sanitizeMarkdown(i.action_level)} ${sanitizeMarkdown(i.units)}`
              )
              .join(", ");
            text += `\n`;
          }
          text += `\n`;
          totalResults += testing.results.length;
        }

        // Search INCB
        const incb = await this.env.DB.prepare(
          `SELECT * FROM incb_yellow_list
           WHERE substance_name LIKE ? ESCAPE '\\' COLLATE NOCASE
              OR synonyms LIKE ? ESCAPE '\\' COLLATE NOCASE
           LIMIT ?`
        )
          .bind(pattern, pattern, MAX_REGULATION_RESULTS)
          .all();

        if (incb.results && incb.results.length > 0) {
          text += `### UN INCB Scheduled Substances (${incb.results.length} matches)\n`;
          for (const r of incb.results) {
            text += `- **${sanitizeMarkdown(r.substance_name)}** — Schedule ${sanitizeMarkdown(r.schedule)}${r.cas_number ? ` (CAS: ${sanitizeMarkdown(r.cas_number)})` : ""}\n`;
          }
          text += `\n`;
          totalResults += incb.results.length;
        }

        // Search Health Canada
        const hc = await this.env.DB.prepare(
          `SELECT * FROM health_canada_cannabis
           WHERE analyte_or_parameter LIKE ? ESCAPE '\\' COLLATE NOCASE
              OR category LIKE ? ESCAPE '\\' COLLATE NOCASE
           LIMIT ?`
        )
          .bind(pattern, pattern, MAX_REGULATION_RESULTS)
          .all();

        if (hc.results && hc.results.length > 0) {
          text += `### Health Canada Cannabis (${hc.results.length} matches)\n`;
          for (const r of hc.results) {
            text += `- **${sanitizeMarkdown(r.analyte_or_parameter)}**: ${sanitizeMarkdownOr(r.limit_value, "N/A")} ${sanitizeMarkdown(r.units)} (${sanitizeMarkdownOr(r.product_class, "all")})\n`;
          }
          text += `\n`;
          totalResults += hc.results.length;
        }

        // Search precursors
        const prec = await this.env.DB.prepare(
          `SELECT * FROM eu_drug_precursors
           WHERE substance_name LIKE ? ESCAPE '\\' COLLATE NOCASE
           LIMIT ?`
        )
          .bind(pattern, MAX_PRECURSOR_RESULTS)
          .all();

        if (prec.results && prec.results.length > 0) {
          text += `### EU Drug Precursors (${prec.results.length} matches)\n`;
          for (const r of prec.results) {
            text += `- **${sanitizeMarkdown(r.substance_name)}** — Category ${sanitizeMarkdownOr(r.category, "N/A")}${r.cas_number ? ` (CAS: ${sanitizeMarkdown(r.cas_number)})` : ""}\n`;
          }
          text += `\n`;
          totalResults += prec.results.length;
        }

        if (totalResults === 0) {
          return {
            content: [
              {
                type: "text" as const,
                text: `No results found for "${sanitizeMarkdown(query)}" across cannabis testing limits, controlled substance schedules, precursor lists, or Health Canada regulations. Try alternative terms or broader searches.`,
              },
            ],
          };
        }

        text += `---\n*${totalResults} total results across all databases*`;
        text += `\n\n**Citation:** Cannabis regulation search "${sanitizeMarkdown(query)}": ${totalResults} results across testing limits, INCB scheduling, Health Canada, EU precursors. Source: Roots by Benda (rootsbybenda.com).`;
        return { content: [{ type: "text" as const, text }] };
      }
    );
  }
}

export default {
  async fetch(request: Request, env: Env, ctx: ExecutionContext): Promise<Response> {
    const url = new URL(request.url);

    // Resolve auth early — use user_id for rate limiting when authenticated (better for shared IPs)
    let auth: AuthProps | null = null;
    const isDataEndpoint = url.pathname === "/mcp" || url.pathname === "/sse" || url.pathname.startsWith("/sse/") || (request.method === "POST" && url.pathname === "/");
    if (isDataEndpoint) {
      auth = await resolveAuth(request, env);
      const rateLimitKey = auth.user_id || request.headers.get("cf-connecting-ip") || request.headers.get("x-forwarded-for") || "unknown";
      if (!checkRateLimit(rateLimitKey)) {
        return rateLimitResponse();
      }
    }

    // SEP-1649: route MCP clients that POST initialize to root to streamable HTTP.
    if (request.method === "POST" && url.pathname === "/") {
      if (!auth) auth = await resolveAuth(request, env);
      (ctx as ExecutionContext & { props?: AuthProps }).props = auth;
      const mcpUrl = new URL(request.url);
      mcpUrl.pathname = "/mcp";
      const mcpRequest = new Request(mcpUrl.toString(), request);
      return CannabisMCP.serve("/mcp").fetch(mcpRequest, env, ctx);
    }

    // Health check
    if (url.pathname === "/" || url.pathname === "/health") {
      return Response.json({
        name: SERVER_NAME,
        version: SERVER_VERSION,
        status: "healthy",
        description: SERVER_DESCRIPTION,
        tools: TOOL_CATALOG.map((tool) => tool.name),
        data: DATA_CATALOG,
        docs: HOMEPAGE,
        homepage: HOMEPAGE,
        source: SOURCE,
      });
    }


    if (url.pathname === "/.well-known/mcp/server.json") {
      return Response.json(registryMetadata(), {
        headers: { "Cache-Control": "public, max-age=300" },
      });
    }

    if (url.pathname === "/.well-known/mcp/server-card.json") {
      return Response.json({
        "$schema": "https://static.modelcontextprotocol.io/schemas/mcp-server-card/v1.json",
        "version": "1.0",
        "protocolVersion": "2025-06-18",
        "serverInfo": { "name": "cannabis-mcp-server", "title": SERVER_NAME, "version": SERVER_VERSION },
        "description": SERVER_DESCRIPTION,
        "iconUrl": "https://rootsbybenda.com/icon.png",
        "documentationUrl": "https://rootsbybenda.com",
        "transport": { "type": "streamable-http", "endpoint": "/mcp" },
        "capabilities": { "tools": { "listChanged": true }, "resources": { "subscribe": false, "listChanged": false } },
        "authentication": { "required": false, "schemes": ["bearer"], "note": "Optional API key enables per-user rate limiting" },
        "rateLimit": { "requestsPerMinute": 60, "enforcement": "per-ip-or-user" },
        "tools": TOOL_CATALOG
      }, { headers: { "Content-Type": "application/json", "Cache-Control": "public, max-age=300" } });
    }

    // Resolve auth and set on ctx.props for MCP transport endpoints
    if (url.pathname === "/sse" || url.pathname.startsWith("/sse/") || url.pathname === "/mcp") {
      if (!auth) auth = await resolveAuth(request, env);
      (ctx as ExecutionContext & { props?: AuthProps }).props = auth;
    }

    // SSE transport (legacy clients)
    if (url.pathname === "/sse" || url.pathname.startsWith("/sse/")) {
      return CannabisMCP.serveSSE("/sse").fetch(request, env, ctx);
    }

    // Streamable HTTP transport (new spec)
    if (url.pathname === "/mcp") {
      return CannabisMCP.serve("/mcp").fetch(request, env, ctx);
    }

    return new Response("Not found", { status: 404 });
  },
};
