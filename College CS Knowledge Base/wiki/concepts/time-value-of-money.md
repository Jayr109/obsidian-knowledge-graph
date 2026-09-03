---
title: "Time Value of Money"
type: concept
tags: [finance, time-value-of-money, present-value, future-value, discounting]
sources: [m03-annuity, m03-perpetuity, m03-mafia-loan, m03-payday-loan]
course: Corporate Finance and Valuation
updated: 2026-04-10
---

Time Value of Money (TVM) is the foundational principle of finance: a dollar today is worth more than a dollar in the future because money available today can be invested to earn a return. All valuation in finance reduces to discounting future cash flows back to the present at an appropriate interest rate.

## Core Formulas

Only two formulas are truly foundational; everything else is derived from them:

**1. Present Value (discounting):**
```
PV = FV / (1 + i)^N
```

**2. Perpetuity:**
```
PV = PMT / i
```

All other TVM formulas (annuity, growing perpetuity, annuity due, etc.) are algebraic combinations of these two.

## Derived Formulas

**Annuity PV** (difference of two perpetuities):
```
PV = PMT/i − PMT / [i × (1+i)^N]
   = PMT × [1 − 1/(1+i)^N] / i
```

**Future Value:**
```
FV = PV × (1 + i)^N
```

## Interest Rate Conventions

| Concept | Formula | Notes |
|---|---|---|
| Periodic rate | Given directly | e.g., 2% per week |
| APR | periodic rate × M | Ignores compounding |
| EAR / EFF | (1 + periodic rate)^M − 1 | True annual cost |

APR understates the true cost when compounding is more frequent than annually. The [[Effective Annual Rate]] is the correct metric for comparison.

**Example:** A 2% weekly rate has APR = 104% but EAR = 180% (see [[M3: Mafia Loan]]).

## Applications in This Course

- [[Perpetuity]] — infinite constant cash flows
- [[Annuity]] — finite constant cash flows
- [[Net Present Value]] — sum of discounted project cash flows
- [[Fischer Equation]] — adjusting rates for inflation

## See Also

- [[Perpetuity]]
- [[Annuity]]
- [[Effective Annual Rate]]
- [[Net Present Value]]
- [[Fischer Equation]]
