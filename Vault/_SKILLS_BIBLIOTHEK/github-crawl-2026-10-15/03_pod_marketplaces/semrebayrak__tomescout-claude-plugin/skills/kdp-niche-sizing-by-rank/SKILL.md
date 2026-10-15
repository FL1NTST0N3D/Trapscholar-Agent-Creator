---
name: kdp-niche-sizing-by-rank
description: Estimate how much the top books in an Amazon niche sell, and what a book at that rank would earn, from the Best Sellers Rank figures the author reads on Amazon, with the TomeScout sales-from-rank and royalty tools. Use when an author asks whether a genre, trope or topic sells, how much competing books sell, or which niche to write next.
---

# KDP niche sizing by rank

## Collect the ranks
Ask the author to search the niche on Amazon.com and note the "Best Sellers Rank" of 5–10 top results: the overall store rank, such as "#4,512 in Kindle Store", and whether each book is Kindle or print.

## Estimate sales
Run `bsr_to_sales` for each rank, then summarise:
- the range of monthly units for a typical top-10 book, using the middle of the pack rather than the #1 outlier,
- how many of the top 10 sell more than about 5 units a day,
- with the author's royalty per sale from `royalty_calculator`, the monthly royalty range for a book at the median rank.

## Honesty rules
- Rank-to-sales figures come from public models. Always show the range and the confidence, and say that Kindle ranks also reflect Kindle Unlimited borrows.
- One reading can be a one-day spike, so suggest checking the same books on a few different days.
- Never promise sales. A niche with a few weak top books is an opportunity; one dominated by big-name authors needs a sharper angle.
