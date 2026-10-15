# EUIPO EU Trademark Search


> **[View on ApifyForge](https://apifyforge.com/actors/euipo-trademark-search)** | **[Use on Apify Store](https://apify.com/ryanclinton/euipo-trademark-search)**

---

Search the official European Union Intellectual Property Office (EUIPO) trademark database programmatically via the Apify platform. Find registered, pending, and expired EU trademarks by name, Nice Classification, applicant, status, mark type, and filing date -- then export structured results with application numbers, owners, goods and services descriptions, filing history, and direct links to the EUIPO eSearch portal.

---

## Why use EUIPO EU Trademark Search?

The EUIPO trademark register is the single authoritative source for EU trademarks (EUTMs) covering all 27 EU member states. Trademark attorneys, brand managers, competitive intelligence teams, and IP professionals rely on it daily. But the EUIPO website is designed for one-off manual lookups, not bulk extraction or automated monitoring. This actor bridges that gap by connecting directly to the official EUIPO Trademark Search REST API, delivering clean, structured data you can feed into spreadsheets, dashboards, or downstream pipelines.

Enterprise IP monitoring services charge hundreds or thousands per month for access to the same underlying data. EUIPO EU Trademark Search gives you direct API access at Apify platform costs -- fractions of a cent per run. Combine it with scheduled runs to build your own automated trademark monitoring system that alerts you to new filings, status changes, or potential conflicts in your market niche.

The actor handles the full OAuth2 authentication flow, builds RSQL search queries from simple input parameters, paginates through result pages automatically, and transforms raw API responses into a flat, consistent JSON structure. You get production-grade trademark data without writing a single line of API integration code.

EUIPO API credentials are required but completely free to obtain. Register at [dev.euipo.europa.eu](https://dev.euipo.europa.eu/) in under 2 minutes, create an app, subscribe to the Trademark Search API, and copy your Client ID and Client Secret into the actor's input fields.

---

## Key features

- **Official EUIPO API data** -- results come directly from the EUIPO Trademark Search API, the same authoritative source used by IP offices and legal professionals across Europe
- **OAuth2 authentication** -- handles the full client credentials flow automatically, including token acquisition and header management with X-IBM-Client-Id
- **Flexible RSQL queries** -- search by trademark name (with wildcards), Nice Classification, status, applicant name, mark type, and filing date range, all combined into a single query
- **14 status filters** -- narrow results by Registered, Received, Under Examination, Application Published, Registration Pending, Withdrawn, Refused, Opposition Pending, Appealed, Cancellation Pending, Cancelled, Surrendered, Expired, or Accepted
- **11 mark type filters** -- Word Mark, Figurative, 3D Shape, Colour, Sound, Hologram, Position, Pattern, Motion, Multimedia, or Other
- **Automatic pagination** -- retrieves up to 500 trademarks per run in pages of 100, sorted by application date descending
- **Rate limit handling** -- detects HTTP 429 responses and respects the Retry-After header with automatic backoff and retry
- **English-preferred descriptions** -- extracts goods and services descriptions in English when available, falling back to the first available language
- **Sandbox environment** -- test your queries against EUIPO sandbox data while waiting for production API approval
- **Clear error messages** -- provides step-by-step registration instructions if credentials are missing or invalid

---

## How to use EUIPO EU Trademark Search

### Using the Apify Console

1. Go to the [EUIPO EU Trademark Search actor page](https://apify.com/ryanclinton/euipo-trademark-search) on Apify.
2. Enter a trademark name in the **Trademark Name** field (e.g., "Nike").
3. Optionally add filters for Nice Classification, status, applicant name, mark type, or date range.
4. Paste your EUIPO **Client ID** and **Client Secret** into the credential fields (required -- register free at [dev.euipo.europa.eu](https://dev.euipo.europa.eu/)).
5. Click **Start** and wait for results.
6. Download results as JSON, CSV, or Excel from the **Dataset** tab, or access them via the Apify API.

### Using the Apify API

Send a POST request to start a run and retrieve results programmatically. See the [API and integration](#api--integration) section below for complete code examples.

---

## Input parameters

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| `query` | String | **Yes** | -- | Trademark name or verbal element to search for. Supports wildcards with `*`. Automatically wrapped in `*query*` if no wildcards provided. |
| `niceClass` | String | No | -- | Nice Classification number (1-45). Use comma-separated values for multiple classes (e.g., `9,42`). |
| `status` | String | No | -- | Filter by trademark status. One of: REGISTERED, RECEIVED, UNDER_EXAMINATION, APPLICATION_PUBLISHED, REGISTRATION_PENDING, WITHDRAWN, REFUSED, OPPOSITION_PENDING, APPEALED, CANCELLATION_PENDING, CANCELLED, SURRENDERED, EXPIRED, ACCEPTED. |
| `applicantName` | String | No | -- | Filter by applicant or owner name. Supports wildcards with `*`. Automatically wrapped in `*name*` if no wildcards provided. |
| `markFeature` | String | No | -- | Filter by mark type. One of: WORD, FIGURATIVE, SHAPE_3D, COLOUR, SOUND, HOLOGRAM, POSITION, PATTERN, MOTION, MULTIMEDIA, OTHER. |
| `dateFrom` | String | No | -- | Filter trademarks filed on or after this date (format: YYYY-MM-DD). |
| `dateTo` | String | No | -- | Filter trademarks filed on or before this date (format: YYYY-MM-DD). |
| `clientId` | String | **Yes** | -- | Your EUIPO developer portal Client ID. Register free at [dev.euipo.europa.eu](https://dev.euipo.europa.eu/). Stored as a secret. |
| `clientSecret` | String | **Yes** | -- | Your EUIPO developer portal Client Secret. Stored as a secret. |
| `useSandbox` | Boolean | No | `false` | Use the EUIPO sandbox environment for testing (uses test data, not production data). |
| `maxResults` | Integer | No | `25` | Maximum number of trademarks to return (1--500). |

### Input example

**Search for registered Nike trademarks in software and clothing:**

```json
{
    "query": "Nike",
    "niceClass": "9,25",
    "status": "REGISTERED",
    "maxResults": 50,
    "clientId": "YOUR_EUIPO_CLIENT_ID",
    "clientSecret": "YOUR_EUIPO_CLIENT_SECRET"
}
```

**Find trademarks filed by a specific company in 2024:**

```json
{
    "query": "*",
    "applicantName": "Samsung",
    "dateFrom": "2024-01-01",
    "dateTo": "2024-12-31",
    "maxResults": 100,
    "clientId": "YOUR_EUIPO_CLIENT_ID",
    "clientSecret": "YOUR_EUIPO_CLIENT_SECRET"
}
```

### Input tips

- Use `*` wildcards for partial matching -- `NIKE*` finds marks starting with "NIKE", while the default `*NIKE*` finds any mark containing "NIKE".
- Combine filters to narrow large result sets. Searching for "APPLE" alone returns thousands of results, but adding `niceClass=9` and `status=REGISTERED` narrows it significantly.
- Start with the sandbox environment if you are still waiting for production API approval. Sandbox data differs from production but lets you test your queries immediately.
- Nice Classification classes 1--34 cover goods, while 35--45 cover services. Common classes: 9 (software, electronics), 25 (clothing), 35 (advertising), 42 (IT services).

---

## Output

Each trademark in the output dataset contains the following fields:

```json
{
    "applicationNumber": "018945321",
    "markName": "NIKE AIR",
    "markImageUrl": "https://api.euipo.europa.eu/trademark-search/trademarks/018945321/image/thumbnail",
    "applicantName": "Nike Innovate C.V.",
    "niceClasses": "9, 25, 28",
    "filingDate": "2024-03-15",
    "registrationDate": "2024-09-22",
    "expiryDate": "2034-03-15",
    "status": "REGISTERED",
    "markType": "Word Mark",
    "markKind": "Individual",
    "markBasis": "EU Trademark",
    "representativeName": "Hogan Lovells (Alicante) S.L.",
    "goodsAndServicesDescription": "Class 9: Downloadable software for fitness tracking | Class 25: Athletic footwear; sports clothing | Class 28: Sporting equipment and apparatus",
    "renewalStatus": "",
    "euipoUrl": "https://euipo.europa.eu/eSearch/#basic/1+1+1+1/50+50+50+50/018945321",
    "extractedAt": "2025-01-15T14:30:00.000Z"
}
```

### Output fields

| Field | Type | Description |
|-------|------|-------------|
| `applicationNumber` | String | EUIPO application number (unique identifier for the trademark) |
| `markName` | String | Verbal element of the trademark (the word mark text) |
| `markImageUrl` | String | URL to the trademark image thumbnail hosted by EUIPO |
| `applicantName` | String | Name(s) of the trademark applicant or owner, semicolon-separated if multiple |
| `niceClasses` | String | Comma-separated Nice Classification numbers the trademark is registered under |
| `filingDate` | String | Date the trademark application was filed (YYYY-MM-DD) |
| `registrationDate` | String | Date the trademark was registered, if applicable (YYYY-MM-DD) |
| `expiryDate` | String | Expiration date of the trademark registration (YYYY-MM-DD) |
| `status` | String | Current legal status (e.g., REGISTERED, UNDER_EXAMINATION, REFUSED) |
| `markType` | String | Human-readable mark type (Word Mark, Figurative, 3D Shape, Sound, etc.) |
| `markKind` | String | Mark kind: Individual, EU Collective, or EU Certification |
| `markBasis` | String | EU Trademark or International Registration |
| `representativeName` | String | Name(s) of the legal representative, semicolon-separated if multiple |
| `goodsAndServicesDescription` | String | English-preferred description of goods and services, organized by class |
| `renewalStatus` | String | Renewal status if applicable |
| `euipoUrl` | String | Direct link to the trademark on the EUIPO eSearch portal |
| `extractedAt` | String | ISO 8601 timestamp when the data was extracted |

---

## Use cases

- **Trademark clearance searches** -- check if a proposed brand name is already registered or pending in the EU before filing a new application
- **Competitive intelligence** -- monitor competitors' trademark filings to track new product launches, brand expansions, or market entry strategies
- **Portfolio monitoring** -- schedule regular runs to track the status of your own trademark portfolio and catch expiry dates, oppositions, or cancellations early
- **IP due diligence** -- audit trademark portfolios during M&A transactions, licensing negotiations, or investment evaluations
- **Brand protection** -- detect potentially infringing marks that are confusingly similar to your registered trademarks
- **Legal research** -- gather trademark filing data for opposition proceedings, invalidity actions, or prior art analysis
- **Market analysis** -- analyze trademark filing trends by Nice Classification, mark type, or time period to identify emerging industry sectors
- **Academic research** -- extract large-scale trademark datasets for studies on IP economics, brand strategy, or innovation metrics
- **Compliance monitoring** -- track trademark registrations in regulated industries to ensure proper IP coverage across EU markets

---

## API & Integration

You can call EUIPO EU Trademark Search programmatically from any language using the Apify API.

### Python

```python
import requests
import time

# Start the actor run
run = requests.post(
    "https://api.apify.com/v2/acts/ryanclinton~euipo-trademark-search/runs",
    params={"token": "YOUR_APIFY_TOKEN"},
    json={
        "query": "Nike",
        "niceClass": "9,25",
        "status": "REGISTERED",
        "maxResults": 50,
        "clientId": "YOUR_EUIPO_CLIENT_ID",
        "clientSecret": "YOUR_EUIPO_CLIENT_SECRET"
    },
    timeout=30,
).json()

# Wait for completion
run_id = run["data"]["id"]
while True:
    status = requests.get(
        f"https://api.apify.com/v2/actor-runs/{run_id}",
        params={"token": "YOUR_APIFY_TOKEN"},
        timeout=10,
    ).json()
    if status["data"]["status"] in ("SUCCEEDED", "FAILED", "ABORTED"):
        break
    time.sleep(5)

# Get results
dataset_id = status["data"]["defaultDatasetId"]
items = requests.get(
    f"https://api.apify.com/v2/datasets/{dataset_id}/items",
    params={"token": "YOUR_APIFY_TOKEN"},
    timeout=30,
).json()

for tm in items:
    print(f"{tm['applicationNumber']} | {tm['markName']} | {tm['applicantName']} | {tm['status']}")
```

### JavaScript

```javascript
const response = await fetch(
    "https://api.apify.com/v2/acts/ryanclinton~euipo-trademark-search/run-sync-get-dataset-items?token=YOUR_APIFY_TOKEN",
    {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
            query: "Nike",
            niceClass: "9,25",
            status: "REGISTERED",
            maxResults: 50,
            clientId: "YOUR_EUIPO_CLIENT_ID",
            clientSecret: "YOUR_EUIPO_CLIENT_SECRET",
        }),
    }
);

const trademarks = await response.json();
trademarks.forEach((tm) =>
    console.log(`${tm.applicationNumber} | ${tm.markName} | ${tm.applicantName} | ${tm.status}`)
);
```

### cURL

```bash
curl -X POST "https://api.apify.com/v2/acts/ryanclinton~euipo-trademark-search/run-sync-get-dataset-items?token=YOUR_APIFY_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "query": "Nike",
    "niceClass": "9,25",
    "status": "REGISTERED",
    "maxResults": 50,
    "clientId": "YOUR_EUIPO_CLIENT_ID",
    "clientSecret": "YOUR_EUIPO_CLIENT_SECRET"
  }'
```

### Integrations

EUIPO EU Trademark Search outputs standard Apify datasets that integrate with:

- **Zapier, Make (Integromat), and n8n** -- connect trademark data to thousands of apps for automated alerting and pipeline workflows
- **Google Sheets** -- export results directly for collaborative review and portfolio tracking
- **Slack, email, and Microsoft Teams** -- receive notifications via Apify integrations when new filings match your criteria
- **Amazon S3, Google Cloud Storage, Dropbox** -- archive trademark datasets for long-term storage and compliance
- **Apify webhooks** -- trigger downstream processing when a run completes

---

## How it works

The actor follows a four-step pipeline to authenticate, query, paginate, and transform EUIPO trademark data:

```
Input (query, filters, EUIPO credentials)
  |
  v
+-----------------------------------------------------------+
|  Step 1: OAuth2 Authentication                            |
|                                                           |
|  POST to EUIPO auth endpoint with:                        |
|    client_id, client_secret, grant_type=client_credentials|
|    scope=uid                                              |
|                                                           |
|  Production: euipo.europa.eu/cas-server-webapp/oidc/...   |
|  Sandbox:    auth-sandbox.euipo.europa.eu/oidc/...        |
|                                                           |
|  Returns: Bearer access_token                             |
+-----------------------------------------------------------+
  |
  v
+-----------------------------------------------------------+
|  Step 2: RSQL Query Construction                          |
|                                                           |
|  Builds RSQL filter string from input parameters:         |
|    verbalElement==*Nike*                                   |
|    ;niceClasses=in=(9,25)                                 |
|    ;status==REGISTERED                                    |
|    ;applicants.name==*Samsung*                            |
|    ;markFeature==WORD                                     |
|    ;applicationDate>=2024-01-01                           |
|    ;applicationDate<=2024-12-31                           |
|                                                           |
|  Parts joined with semicolons (AND logic)                 |
+-----------------------------------------------------------+
  |
  v
+-----------------------------------------------------------+
|  Step 3: Paginated API Retrieval                          |
|                                                           |
|  GET /trademarks?query={rsql}&page=N&size=100             |
|    &sort=applicationDate:desc                             |
|                                                           |
|  Headers: Authorization: Bearer {token}                   |
|           X-IBM-Client-Id: {clientId}                     |
|                                                           |
|  Pages of 100 results until maxResults reached            |
|  HTTP 429 --> wait Retry-After seconds, then retry        |
+-----------------------------------------------------------+
  |
  v
+-----------------------------------------------------------+
|  Step 4: Data Transformation                              |
|                                                           |
|  For each raw trademark record:                           |
|    - Map markFeature codes to human-readable labels       |
|    - Map markKind codes to human-readable labels          |
|    - Extract English-preferred goods/services text        |
|    - Build image thumbnail URL                            |
|    - Build EUIPO eSearch portal URL                       |
|    - Flatten applicants and representatives arrays        |
|    - Sort Nice classes numerically                        |
+-----------------------------------------------------------+
  |
  v
Apify Dataset (flat JSON, one object per trademark)
```

---

## Performance & cost

EUIPO EU Trademark Search is a lightweight API-based actor that uses minimal Apify platform resources. The primary bottleneck is the EUIPO API's own response time and rate limits, not Apify compute.

| Scenario | Run time | Compute units | Estimated cost |
|----------|----------|---------------|----------------|
| 25 trademarks (default) | ~10--30 seconds | ~0.001--0.005 CU | ~$0.001 |
| 100 trademarks | ~30--60 seconds | ~0.005--0.01 CU | ~$0.005 |
| 500 trademarks (maximum) | ~1--3 minutes | ~0.01--0.03 CU | ~$0.01 |
| Daily monitoring (25 results, 30 days) | ~15 min total | ~0.03--0.15 CU | ~$0.03/month |

The Apify free tier includes $5 of monthly platform usage, which is more than enough to run this actor hundreds of times per month. The EUIPO API credentials themselves are free to obtain from the EUIPO developer portal.

---

## Limitations

- **EUIPO API credentials required** -- you must register for a free Client ID and Client Secret at [dev.euipo.europa.eu](https://dev.euipo.europa.eu/). The actor cannot search real data without valid credentials.
- **Sandbox approval delay** -- sandbox access typically takes about one week after registration. Production access may take longer depending on EUIPO's review process.
- **Maximum 500 results per run** -- the EUIPO API limits page-based retrieval. For larger datasets, run multiple queries with narrower date ranges or filters.
- **EU trademarks only** -- this actor searches the EUIPO database, which covers EU trademarks and international registrations designating the EU. It does not cover national trademark registers of individual EU member states.
- **Verbal element search only** -- the text search queries the verbal (word) element of trademarks. It cannot search by image similarity for figurative marks.
- **Rate limits apply** -- the EUIPO API enforces rate limits. The actor handles 429 responses automatically, but very high-frequency usage may experience delays.
- **Image URLs require authentication** -- the `markImageUrl` field points to the EUIPO API endpoint, which may require authentication headers to access directly outside this actor.

---

## Responsible use

- **Official data source** -- this actor connects to the official EUIPO API. Use it in accordance with the EUIPO developer portal terms of service and API usage policies.
- **Respect rate limits** -- the actor handles rate limiting automatically, but avoid scheduling unnecessarily frequent runs. Daily or weekly monitoring is appropriate for most use cases.
- **Trademark data is public** -- EU trademark registrations are public records. However, use extracted data responsibly and in compliance with applicable data protection regulations.
- **Not legal advice** -- trademark search results from this actor are informational. Consult a qualified IP attorney for legal interpretation, filing decisions, or enforcement actions.
- **Credential security** -- your EUIPO Client ID and Client Secret are stored as Apify secrets and are never logged or included in output data.

---

## FAQ

**Do I need EUIPO API credentials to use this actor?**
Yes. You need a free Client ID and Client Secret from the EUIPO developer portal at [dev.euipo.europa.eu](https://dev.euipo.europa.eu/). Registration is free and takes about 2 minutes. The actor will not run without valid credentials.

**How long does it take to get EUIPO API credentials?**
Registration on the EUIPO developer portal is instant, but sandbox access approval typically takes about one week. Production API access may take longer depending on EUIPO's review process.

**Does this actor cover all EU member states?**
Yes. EU trademarks (EUTMs) registered through EUIPO provide protection across all 27 EU member states with a single registration. This actor searches the complete EUIPO database including both EU trademarks and international registrations designating the EU.

**What are Nice Classifications?**
The Nice Classification is an international system that categorizes goods and services into 45 classes (1--34 for goods, 35--45 for services). Trademarks are registered under specific classes. For example: Class 9 (computer software, electronics), Class 25 (clothing, footwear), Class 35 (advertising, business management), Class 42 (scientific and technological services).

**Can I search for figurative (logo) trademarks?**
Yes. Set the "Mark Type" filter to "Figurative" to find logo-based trademarks. The output includes a `markImageUrl` field with a link to the trademark image thumbnail hosted by EUIPO. Note that you cannot search by image similarity -- the text query matches the verbal element only.

**What is the difference between sandbox and production?**
The sandbox environment uses test data and is meant for development and testing. Production uses real, live trademark data from the EUIPO register. Use sandbox while waiting for production access or when testing integrations.

**Can I search by multiple Nice classes at once?**
Yes. Enter comma-separated class numbers in the `niceClass` field (e.g., `9,25,42`). The actor builds an RSQL `in=()` query that matches trademarks in any of the specified classes.

**How do wildcards work in the search?**
The actor automatically wraps your search term in wildcards (`*query*`) for broad matching. You can also use explicit wildcards: `NIKE*` finds marks starting with "NIKE", `*SPORT` finds marks ending with "SPORT", and `*SPORT*` finds any mark containing "SPORT". The same wildcard behavior applies to the applicant name filter.

**What does the `markBasis` field mean?**
It indicates whether the trademark was filed directly with EUIPO as an "EU Trademark" or is an "International Registration" designating the EU through the Madrid Protocol system administered by WIPO.

**Can I monitor new filings automatically?**
Yes. Set up a scheduled run on Apify (daily or weekly) with a date range filter using `dateFrom` set to the current or recent date. The actor will return only trademarks filed within that window, effectively creating a new-filing alert system.

**What statuses can I filter by?**
14 statuses are available: Registered, Received, Under Examination, Application Published, Registration Pending, Withdrawn, Refused, Opposition Pending, Appealed, Cancellation Pending, Cancelled, Surrendered, Expired, and Accepted. Each corresponds to a stage in the EUTM lifecycle.

**Is the EUIPO API free to use?**
Yes. The EUIPO developer portal provides free API credentials. There are no per-query charges from EUIPO. Your only costs are Apify platform compute, which is minimal for this actor.

---

## Related actors

| Actor | What it does | Use with EUIPO EU Trademark Search |
|-------|-------------|-------------------------------------|
| [USPTO Patent Search](https://apify.com/ryanclinton/patent-search) | Search US patents and trademarks | Cross-reference IP portfolios across the US and EU |
| [EPO European Patent Search](https://apify.com/ryanclinton/epo-patent-search) | Search European patents | Combine trademark and patent data for complete European IP landscape analysis |
| [UK Companies House](https://apify.com/ryanclinton/uk-companies-house) | Look up UK company information | Cross-reference trademark applicants with their corporate records for due diligence |
| [Brand Protection Monitor](https://apify.com/ryanclinton/brand-protection-monitor) | Detect typosquatting and impersonation | Pair trademark registrations with domain monitoring to protect your brand online |
| [OpenCorporates Search](https://apify.com/ryanclinton/opencorporates-search) | Search global company registries | Verify trademark applicant identities against corporate registration records worldwide |
