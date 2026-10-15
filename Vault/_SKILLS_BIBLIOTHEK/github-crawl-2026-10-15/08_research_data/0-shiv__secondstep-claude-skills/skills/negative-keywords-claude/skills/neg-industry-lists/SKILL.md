# Pre-Built Industry Negative Keyword Lists

## Command: /negatives lists

Access battle-tested negative keyword lists for 15 industries. Each list contains 50-200 terms curated from thousands of account audits. These are the terms that waste money in virtually every account within that industry.

## Why Pre-Built Lists Matter

Starting from zero with negative keywords means you pay for the education. Every irrelevant click teaches you one more word to block — but at $2-15 per click, those lessons are expensive. Pre-built industry lists give you a head start by covering the most common waste patterns seen across thousands of accounts in your industry.

These lists are NOT a replacement for ongoing search term mining. They are a foundation. Your account will have unique waste patterns that no generic list can predict. But these lists typically eliminate 40-60% of common waste on day one.

## Available Industry Lists

### 1. E-Commerce (150+ terms)
File: `lists/ecommerce-negatives.txt`
Covers: free shipping competitor expectations, DIY/craft terms, wholesale/bulk mismatches, return/refund seekers, coupon hunters for other stores, job seekers in retail, product review-only intent.
Key patterns blocked: "free", "DIY", "wholesale", "bulk", "coupon code for [competitor]", "jobs", "careers", "how to make", "homemade", "recipe", "tutorial"

### 2. Legal Services (100+ terms)
File: `lists/legal-negatives.txt`
Covers: law school/career seekers, pro bono/free legal aid, DIY legal forms, legal definitions/research, entertainment (TV shows, movies about law), government/court information lookups.
Key patterns blocked: "law school", "paralegal jobs", "free legal advice", "legal definition of", "law and order", "how to file", "pro bono", "legal aid", "public defender"

### 3. Healthcare (100+ terms)
File: `lists/healthcare-negatives.txt`
Covers: medical school/career seekers, home remedies, symptom lookup (not appointment intent), medical research/academic, insurance information, government health programs, veterinary.
Key patterns blocked: "nursing jobs", "medical school", "home remedy", "symptoms of", "wikipedia", "NIH", "CDC", "veterinary", "for dogs", "for cats"

### 4. SaaS / Software (100+ terms)
File: `lists/saas-negatives.txt`
Covers: open source alternatives, free/freemium seekers, developer job searches, tutorial/course seekers, crack/pirate terms, API documentation lookups, student/academic users.
Key patterns blocked: "open source", "free alternative", "developer jobs", "tutorial", "crack", "torrent", "github", "stackoverflow", "salary", "interview questions"

### 5. Real Estate (100+ terms)
File: `lists/real-estate-negatives.txt`
Covers: real estate agent career seekers, rental (when selling), foreclosure/short sale (when not specializing), Zillow/Redfin lookers, real estate exam/license, virtual tours only, neighborhood research.
Key patterns blocked: "real estate license", "agent salary", "Zillow", "rent" (if selling), "foreclosure", "section 8", "public housing", "how to become agent"

### 6. Home Services (100+ terms)
File: `lists/home-services-negatives.txt`
Covers: DIY tutorials, tool/supply shopping, career seekers, licensing/certification, competitor reviews, insurance claims, warranty lookups, code/regulation research.
Key patterns blocked: "how to", "DIY", "tutorial", "tools needed", "plumber salary", "contractor license", "home warranty", "insurance claim"

### 7. Education (80+ terms)
Covers: free course seekers, scholarship scams, accreditation research, teacher job searches, campus maps/directions only, textbook shopping, student loan refinancing.
Key patterns blocked: "free course", "scholarship", "accreditation", "teacher jobs", "campus map", "textbook", "student loan"

### 8. Finance / Financial Services (90+ terms)
Covers: banking job seekers, free financial calculators, government program lookups, crypto/speculative, academic finance research, regulatory information.
Key patterns blocked: "bank teller jobs", "free calculator", "FDIC", "SEC filing", "cryptocurrency", "bitcoin", "finance degree"

### 9. Automotive (85+ terms)
Covers: DIY repair, car enthusiast/hobby, salvage/junkyard, racing/performance (for standard dealers), car history/models research, insurance quotes, driving school.
Key patterns blocked: "how to fix", "junkyard", "salvage", "racing", "car history", "driving school", "insurance quote", "recall"

### 10. Travel / Hospitality (90+ terms)
Covers: travel blog/vlog research, visa/passport government info, flight tracking, travel insurance comparison, hostel/budget (for luxury), travel jobs, study abroad.
Key patterns blocked: "travel blog", "visa requirements", "flight tracker", "travel insurance", "hostel", "backpacking", "travel agent jobs"

### 11. Restaurants / Food Service (70+ terms)
Covers: recipe seekers, food delivery app searches, restaurant jobs, food photography, cooking classes, food safety/regulation, franchise information.
Key patterns blocked: "recipe", "cooking", "food delivery app", "restaurant jobs", "waiter salary", "food handler", "franchise cost"

### 12. B2B / Professional Services (85+ terms)
Covers: template/DIY seekers, job hunters, academic research, free tool seekers, industry association lookups, certification/training.
Key patterns blocked: "template", "free tool", "jobs", "salary", "certification", "training course", "association", "conference"

### 13. Staffing / Recruiting (80+ terms)
Covers: resume writing (not recruiting), career advice content, unemployment/government services, gig economy platforms, self-employment, freelance platforms.
Key patterns blocked: "resume template", "career advice", "unemployment benefits", "gig economy", "freelance", "self employed", "Upwork", "Fiverr"

### 14. Insurance (90+ terms)
Covers: government insurance programs, insurance job seekers, claim filing how-to, insurance exam/licensing, competitor rate comparisons (broad), insurance fraud.
Key patterns blocked: "Medicaid", "Medicare", "insurance agent salary", "how to file claim", "insurance exam", "insurance fraud"

### 15. Fitness / Wellness (75+ terms)
Covers: free workout seekers, home exercise (for gyms), nutrition/diet research, fitness certification, bodybuilding competition, injury/medical terms.
Key patterns blocked: "free workout", "home exercise", "diet plan", "personal trainer salary", "bodybuilding competition", "physical therapy"

## Universal Negatives (applies to ALL industries)

File: `lists/universal-negatives.txt`

These 50 terms waste money in virtually every industry:
- Job/career terms: jobs, careers, salary, hiring, employment, resume, interview, internship
- Free/cheap: free, torrent, crack, pirate, bootleg
- Academic: essay, thesis, dissertation, research paper, wikipedia, scholarly
- Complaints: scam, fraud, lawsuit, complaint, ripoff, BBB
- Information-only: definition, meaning, wiki, history of, origin of
- Government: government, .gov, federal, state program

## How to Use Industry Lists

### Step 1: Select Your Industry
```bash
/negatives lists saas
```

### Step 2: Review the List
Every term in the list should be reviewed before adding. Some terms that waste money in 95% of accounts in your industry might be relevant to YOUR specific business.

### Step 3: Customize
- Remove terms that are actually relevant to your business
- Add your own terms discovered through search term mining
- Adjust match types based on your keyword structure

### Step 4: Apply
- Add universal negatives first (account level or shared list)
- Add industry negatives second (campaign level or shared list)
- Add custom negatives third (ad group or campaign level)

## List Update Frequency

Industry lists are updated quarterly based on aggregate search term data from audits. Each update includes:
- New waste terms discovered across accounts
- Removed terms that no longer cause waste (search behavior changes)
- Match type adjustments based on conflict frequency data

## Integration with Other Skills

- `/negatives mine` compares mined terms against industry lists to identify gaps
- `/negatives conflicts` checks industry list terms against your active keywords
- `/negatives report` includes industry list coverage in the coverage score
- `/negatives cross-campaign` uses industry lists as baseline for shared negative lists
