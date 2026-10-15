# Schema: Organization

Generate complete Organization schema markup in JSON-LD format. This schema identifies a company, nonprofit, school, or other organization to search engines, providing structured information about the entity's identity, contact details, social presence, and corporate structure.

## Command

`/schema organization`

## When to Use

Organization schema belongs on the homepage or "About" page of any website that represents a company, nonprofit, educational institution, government agency, or other formal organization. It is one of the foundational schema types -- every business website should have it. Google uses Organization schema to populate Knowledge Panels, verify social profiles, display contact information, and associate branded search results with the correct entity.

## Required Properties (Google)

- `@type`: "Organization" (or subtype: Corporation, EducationalOrganization, GovernmentOrganization, MedicalOrganization, NGO, PerformingGroup, SportsOrganization)
- `name`: Official legal or brand name of the organization
- `url`: Homepage URL of the organization
- `logo`: URL to the organization's logo image (minimum 112x112px, must be crawlable)

## Recommended Properties

- `sameAs`: Array of official social media profile URLs (LinkedIn, Twitter/X, Facebook, Instagram, YouTube, Wikipedia, Wikidata, Crunchbase). Google uses these to verify social profiles for Knowledge Panels.
- `contactPoint`: Array of ContactPoint objects with `telephone`, `contactType` (customer service, technical support, sales, billing support, etc.), `areaServed`, and `availableLanguage`.
- `address`: PostalAddress with `streetAddress`, `addressLocality`, `addressRegion`, `postalCode`, `addressCountry`.
- `description`: Brief description of the organization (1-2 sentences).
- `foundingDate`: ISO 8601 date when the organization was founded.
- `founder`: Person or array of Person objects.
- `numberOfEmployees`: QuantitativeValue for employee count.
- `parentOrganization` / `subOrganization`: For corporate hierarchy.
- `taxID` / `vatID`: For official registrations.
- `email`: Contact email address.
- `image`: Photos of the organization (office, team, etc.).

## Template

The template at `templates/organization.json` provides a fully populated example with all properties. When generating, always ask the user for:

1. Organization name
2. Website URL
3. Logo URL (or ask if they need guidance on logo requirements)
4. Social media profile URLs
5. Phone number(s) and contact types
6. Physical address (if applicable)
7. Brief description

## Common Mistakes

- **Using a personal URL for sameAs**: Only include official organization social profiles, not personal accounts of founders or employees.
- **Logo too small**: Google requires minimum 112x112px. Recommend 250x250px or larger, square or landscape aspect ratio.
- **Missing logo ImageObject**: While a plain URL string works, wrapping the logo in an ImageObject with width/height is more robust.
- **Inconsistent NAP**: The name, address, and phone number in Organization schema must match Google Business Profile, social profiles, and other directory listings exactly.
- **Duplicate schema**: Only one Organization schema per domain (typically on homepage). Other pages should reference it via `@id` or `publisher` properties.
- **Wrong @type for subtype**: A restaurant should use "Restaurant" (which is a subtype of LocalBusiness, not Organization). Only use Organization for non-location-specific entities.

## Google Rich Result Eligibility

Organization schema contributes to:
- **Knowledge Panels**: Company information in the right sidebar of search results
- **Logo display**: Official logo shown in search results
- **Social profile links**: Verified social profiles displayed in Knowledge Panel
- **Contact information**: Phone numbers and support options

Note: There is no standalone "Organization" rich result test in Google's Rich Results Test tool. Organization schema influences Knowledge Panels and brand SERP features indirectly. Use Google's Schema Markup Validator to check syntax.

## Multi-Entity Considerations

For organizations with multiple brands, divisions, or subsidiaries, use `subOrganization` to establish the hierarchy. Each sub-organization can have its own schema on its dedicated page, linked back to the parent via `parentOrganization`. This is common for holding companies, franchise networks, and multi-brand retailers.

## Implementation Notes

- Place Organization schema on the homepage only. Reference it from other pages via `publisher` (for Article schema) or `brand` (for Product schema).
- Use `@id` to create a referenceable node: `"@id": "https://example.com/#organization"`. This lets other schema on other pages reference this entity without duplicating all properties.
- For Next.js or React apps, add this to the root layout or `_app` component so it appears on every page load.
