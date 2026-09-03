---
title: "Effective Annual Rate"
type: concept
tags: [finance, interest-rates, effective-annual-rate, apr, compound-interest]
sources: [m03-mafia-loan, m03-payday-loan]
course: Corporate Finance and Valuation
updated: 2026-04-10
---

The Effective Annual Rate (EAR), also called the Effective Annual Yield or Annual Equivalent Rate, is the true annualized cost or return of an investment or loan after accounting for the effect of compounding. It is the only correct measure for comparing loans or investments with different compounding frequencies.

## Formula

```
EAR = (1 + periodic rate)^M − 1
```
where M is the number of compounding periods per year.

## Comparison: EAR vs. APR

**APR (Annual Percentage Rate):** `periodic rate × M` — simply scales the periodic rate without accounting for compounding. Required disclosure in many consumer lending contexts, but understates true cost when compounding is sub-annual.

**EAR:** accounts for compounding. This is the actual annual rate at which your balance grows (for a loan) or wealth grows (for an investment).

| Loan | Periodic Rate | M | APR | EAR |
|---|---|---|---|---|
| Mafia loan | 2%/week | 52 | 104% | ~180% |
| Payday loan | 15%/2-week | 26 | 390% | ~3,686% |

Note: the Mafia loan has a *lower* EAR than a typical payday loan despite sounding scarier, because the payday loan's biweekly rate is so much higher.

## Why EAR Matters

When comparing any two financial instruments, always convert to EAR first. APR figures are legally mandated disclosures but routinely understate the true cost of high-frequency-compounding loans (credit cards, payday loans, etc.).

## See Also

- [[Time Value of Money]]
- [[M3: Mafia Loan]]
- [[M3: Payday Loan]]
