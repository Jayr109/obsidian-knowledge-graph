---
title: "M3: Mafia Loan"
type: source
tags: [finance, interest-rates, effective-annual-rate, apr, compound-interest]
sources: [m03-mafia-loan]
course: Corporate Finance and Valuation
updated: 2026-04-10
---

This transcript uses a Mafia loan-sharking scenario to illustrate the difference between the periodic interest rate, the APR, and the [[Effective Annual Rate]] (EAR). The going rate for loan sharks ("vigorish" or "vig") is almost always 2% per week.

## Scenario

You borrow $100,000 from Tony Soprano. Each week you owe 2% vig on the outstanding principal. If you fail to pay vig, it compounds into principal (compound interest, Mafia style). After 52 weeks of non-payment, you owe:
```
FV = 100 × (1.02)^52 ≈ $280,000
```
Interest paid: $180,000 on a $100,000 principal → interest per dollar = 1.80 → EAR = 180%.

## Key Formulas

**Effective Annual Rate:**
```
(1 + periodic rate)^M = 1 + EAR
EAR = (1 + 0.02)^52 − 1 ≈ 1.80 = 180%
```

**Annual Percentage Rate (APR):**
```
APR = periodic rate × M = 0.02 × 52 = 1.04 = 104%
```

## EAR vs. APR

- **EAR** accounts for compounding — it represents the true annual cost.
- **APR** is the simple product of rate × periods; it ignores compounding.
- A 2% weekly rate has APR = 104% but EAR = 180%.

## Discussion Point

The instructor notes the payday loan comparison (see [[M3: Payday Loan]]): the Mafia charges a *lower* EAR than payday lenders. Students are asked to explain why.

## See Also

- [[Effective Annual Rate]]
- [[Time Value of Money]]
- [[M3: Payday Loan]]
