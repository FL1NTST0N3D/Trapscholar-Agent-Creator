# Schema: Event

Generate Event schema markup in JSON-LD format. This schema enables event rich results in Google Search with dates, locations, ticket prices, and registration links, making events discoverable through both organic search and Google Events.

## Command

`/schema event`

## When to Use

Event schema belongs on any page that describes a specific event with a defined date and time. This includes conferences, concerts, workshops, webinars, meetups, sporting events, festivals, fundraisers, classes, and any other scheduled gathering -- whether physical, virtual, or hybrid. Each individual event occurrence should have its own schema (a recurring weekly meetup needs separate schema for each occurrence, or use EventSeries).

## Required Properties (Google)

- `@type`: "Event" (or subtype: BusinessEvent, ChildrensEvent, ComedyEvent, CourseInstance, DanceEvent, DeliveryEvent, EducationEvent, ExhibitionEvent, Festival, FoodEvent, Hackathon, LiteraryEvent, MusicEvent, PublicationEvent, SaleEvent, ScreeningEvent, SocialEvent, SportsEvent, TheaterEvent, VisualArtsEvent)
- `name`: Event title
- `startDate`: ISO 8601 datetime with timezone (e.g., "2024-09-15T19:00:00-05:00")
- `location`: Place (physical), VirtualLocation (online), or both (hybrid)

## Required for Physical Events

```json
"location": {
  "@type": "Place",
  "name": "Austin Convention Center",
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "500 E Cesar Chavez St",
    "addressLocality": "Austin",
    "addressRegion": "TX",
    "postalCode": "78701",
    "addressCountry": "US"
  }
}
```

## Required for Virtual Events

```json
"location": {
  "@type": "VirtualLocation",
  "url": "https://zoom.us/j/123456789"
},
"eventAttendanceMode": "https://schema.org/OnlineEventAttendanceMode"
```

## Required for Hybrid Events

```json
"location": [
  {
    "@type": "Place",
    "name": "Austin Convention Center",
    "address": { ... }
  },
  {
    "@type": "VirtualLocation",
    "url": "https://livestream.example.com/event"
  }
],
"eventAttendanceMode": "https://schema.org/MixedEventAttendanceMode"
```

## Recommended Properties

- `endDate`: ISO 8601 datetime when the event ends
- `description`: Detailed event description
- `image`: Event image or promotional graphic (at least 720px wide)
- `performer`: Person or Organization performing at the event
- `organizer`: Person or Organization hosting the event (include `url`)
- `eventStatus`: Current status of the event:
  - `https://schema.org/EventScheduled` (default, confirmed)
  - `https://schema.org/EventCancelled` (cancelled)
  - `https://schema.org/EventPostponed` (postponed, new date TBD)
  - `https://schema.org/EventMovedOnline` (moved from physical to virtual)
  - `https://schema.org/EventRescheduled` (rescheduled with new date -- include `previousStartDate`)
- `offers`: Offer or array of Offer objects for tickets:
  - `price`: Ticket price (use "0" for free events)
  - `priceCurrency`: ISO 4217 currency code
  - `availability`: InStock, SoldOut, PreOrder
  - `url`: Ticket purchase URL
  - `validFrom`: When tickets go on sale
- `eventAttendanceMode`: OnlineEventAttendanceMode, OfflineEventAttendanceMode, MixedEventAttendanceMode
- `previousStartDate`: Original date if the event was rescheduled
- `doorTime`: When doors open (ISO 8601 datetime)
- `maximumAttendeeCapacity`: Max number of attendees
- `remainingAttendeeCapacity`: Remaining spots available
- `isAccessibleForFree`: Boolean for free events
- `inLanguage`: Language of the event
- `typicalAgeRange`: Target age range (e.g., "18-", "12-17", "all ages")

## Event Series and Recurring Events

For recurring events (weekly meetups, monthly workshops), use EventSeries as a container:

```json
{
  "@type": "EventSeries",
  "name": "Weekly JavaScript Meetup",
  "subEvent": [
    { "@type": "Event", "name": "JS Meetup - March 15", "startDate": "2024-03-15T18:30:00-05:00", ... },
    { "@type": "Event", "name": "JS Meetup - March 22", "startDate": "2024-03-22T18:30:00-05:00", ... }
  ]
}
```

Alternatively, create individual Event pages for each occurrence and link them via `superEvent` pointing to the series page.

## Event Status Changes (COVID-era Patterns)

Google specifically supports event status changes. When an event is cancelled, postponed, or moved online:

1. **Do NOT delete the event page** -- update the schema with the new status
2. Set `eventStatus` to the appropriate value
3. For rescheduled events, keep `previousStartDate` and update `startDate`
4. For moved-online events, change `location` to VirtualLocation and set `eventAttendanceMode`

## Common Mistakes

- **Missing timezone in dates**: "2024-09-15T19:00:00" is ambiguous. Always include timezone offset: "2024-09-15T19:00:00-05:00".
- **Using Event for non-events**: Product launches, blog post publications, and business milestones are not events unless there is a scheduled gathering people can attend.
- **Missing location for physical events**: Google requires a complete address, not just a venue name.
- **Free event with no price**: For free events, set `"price": "0"` and `"isAccessibleForFree": true`. Do not omit the price entirely.
- **Deleting cancelled events**: Update the status to EventCancelled instead of removing the page and schema.
- **Past events with no status update**: Remove or clearly mark past events. Do not leave outdated event schema on pages indefinitely.

## Google Rich Result Eligibility

Event schema enables:
- **Event rich results**: Date, time, location, and ticket info in search results
- **Google Events**: Listings in the Google Events experience (search for "events near me" or "concerts this weekend")
- **Event carousel**: Horizontal scrollable event cards for venue and performer searches
- **Knowledge Panel events**: Upcoming events shown in artist/venue Knowledge Panels
- **Google Maps events**: Event listings on venue pages in Google Maps
