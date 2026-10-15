# Schema: Local Business

Generate complete LocalBusiness schema markup in JSON-LD format. This schema is essential for any business with a physical location or service area, enabling rich local search results, Google Maps integration, and Google Business Profile alignment.

## Command

`/schema local-business`

## When to Use

LocalBusiness schema belongs on every page that represents a physical business location. If a business has multiple locations, each location page gets its own LocalBusiness schema. This is the single most impactful schema type for businesses that serve local customers -- it directly influences local pack rankings, map results, and Knowledge Panel accuracy.

## Required Properties (Google)

- `@type`: "LocalBusiness" or a more specific subtype (see Subtypes section)
- `name`: Business name (must match Google Business Profile exactly)
- `address`: PostalAddress with `streetAddress`, `addressLocality`, `addressRegion`, `postalCode`, `addressCountry`
- `telephone`: Primary phone number in international format (e.g., "+1-555-555-5555")

## Recommended Properties

- `geo`: GeoCoordinates with `latitude` and `longitude` (crucial for map accuracy)
- `openingHoursSpecification`: Array of OpeningHoursSpecification objects with `dayOfWeek`, `opens`, `closes`. Handle special hours with `validFrom` and `validThrough`.
- `priceRange`: Dollar sign notation ("$", "$$", "$$$", "$$$$") or descriptive text
- `url`: URL of the location page
- `image`: Photos of the business location
- `areaServed`: GeoCircle, City, State, or AdministrativeArea objects defining service area
- `hasOfferCatalog`: OfferCatalog with service or product listings
- `aggregateRating`: AggregateRating with `ratingValue` and `reviewCount`
- `review`: Array of individual Review objects
- `menu`: URL to menu (for restaurants)
- `servesCuisine`: Cuisine type (for restaurants)
- `paymentAccepted`: Payment methods accepted
- `currenciesAccepted`: Currencies accepted
- `amenityFeature`: LocationFeatureSpecification for amenities (WiFi, parking, etc.)
- `hasMap`: URL to a map of the location
- `smokingAllowed`: Boolean for smoking policy
- `isAccessibleForFree`: Boolean for free entry

## Subtypes

Always use the most specific subtype available. Google recognizes these subtypes for enhanced rich results:

- **Food**: Restaurant, CafeOrCoffeeShop, Bakery, BarOrPub, FastFoodRestaurant, IceCreamShop, Winery, Brewery, Distillery
- **Health**: MedicalBusiness, Physician, Dentist, Pharmacy, Optician, VeterinaryCare, MedicalClinic, Hospital
- **Legal**: LegalService, Attorney, Notary
- **Financial**: FinancialService, BankOrCreditUnion, InsuranceAgency, AccountingService
- **Automotive**: AutoRepair, AutoDealer, AutoBodyShop, AutoWash, GasStation, MotorcycleDealer
- **Home Services**: Plumber, Electrician, HVACBusiness, Locksmith, RoofingContractor, HousePainter, MovingCompany
- **Lodging**: LodgingBusiness, Hotel, Motel, BedAndBreakfast, Hostel, Resort, Campground
- **Beauty**: BeautySalon, HairSalon, NailSalon, TattooParlor, DaySpa, HealthClub
- **Education**: EducationalOrganization, School, Preschool, HighSchool, CollegeOrUniversity
- **Retail**: Store, ClothingStore, ElectronicsStore, HardwareStore, BookStore, ShoeStore
- **Entertainment**: EntertainmentBusiness, MovieTheater, ComedyClub, NightClub, AmusementPark
- **Professional**: ProfessionalService, RealEstateAgent, TravelAgency, EmploymentAgency

## NAP Consistency

NAP (Name, Address, Phone) consistency is the bedrock of local SEO. The values in LocalBusiness schema MUST match exactly across:

1. Google Business Profile listing
2. Website header/footer
3. Schema markup on the page
4. Third-party directory listings (Yelp, Yellow Pages, etc.)

Even small discrepancies (e.g., "St." vs "Street", "LLC" included vs omitted) can confuse search engines and dilute local ranking signals.

## Opening Hours

Opening hours require careful formatting:

- Use 24-hour format: `"opens": "09:00"`, `"closes": "17:00"`
- For businesses open past midnight: set `closes` to the next-day time (e.g., `"closes": "02:00"`)
- For 24-hour businesses: `"opens": "00:00"`, `"closes": "23:59"`
- For closed days: omit that day from the array
- For special/holiday hours: use `specialOpeningHoursSpecification` with `validFrom` and `validThrough` dates

## Service Area Businesses

For businesses that serve customers at their location (plumbers, cleaners, mobile services), use `areaServed` instead of or in addition to `address`:

```json
"areaServed": [
  { "@type": "City", "name": "Austin", "sameAs": "https://en.wikipedia.org/wiki/Austin,_Texas" },
  { "@type": "City", "name": "Round Rock" }
]
```

## Common Mistakes

- **Wrong subtype**: Using "LocalBusiness" when a more specific type exists. Always use the most specific subtype.
- **Missing geo coordinates**: Without latitude/longitude, Google cannot accurately place the business on maps.
- **String opening hours**: Using a plain string like "Mon-Fri 9-5" instead of structured OpeningHoursSpecification objects.
- **Multiple locations in one schema**: Each location must have its own separate LocalBusiness schema on its own page.
- **Fake reviews in schema**: Google prohibits self-serving reviews in schema markup. Only include genuine third-party reviews.
- **Missing @id**: Without an @id, other schema on the site cannot reference this entity.

## Google Rich Result Eligibility

LocalBusiness schema contributes to:
- **Local Pack**: The map-based 3-pack in local search results
- **Knowledge Panel**: Business information panel in branded searches
- **Google Maps**: Business listing details
- **Local rich snippets**: Enhanced organic results with hours, ratings, price range
