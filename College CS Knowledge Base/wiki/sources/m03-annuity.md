---
title: "M3: Annuity"
type: source
tags: [finance, time-value-of-money, annuity, perpetuity, present-value]
sources: [m03-annuity]
course: Corporate Finance and Valuation
updated: 2026-04-10
---

This lecture transcript derives the present value of an [[Annuity]] from first principles, showing that an annuity is simply the difference between two perpetuities. The key insight is that the only formulas you truly need are the perpetuity formula and the basic present value formula — all other time-value-of-money formulas follow from these two.

## Derivation Outline

The instructor constructs the annuity PV formula in three steps:

1. **First perpetuity:** starts paying at time 1, forever. PV = PMT / i.
2. **Second perpetuity:** starts paying at time N+1, forever. PV as of time N = PMT / i. PV today = (PMT / i) / (1+i)^N.
3. **Subtract:** Cash flows of the first perpetuity minus cash flows of the second perpetuity yield exactly a finite stream of N payments — an annuity.

**Annuity PV (difference-of-perpetuities form):**
```
PV = PMT/i  −  PMT / [i × (1+i)^N]
```

**Annuity PV (textbook form, equivalent after algebra):**
```
PV = PMT × [1 − 1/(1+i)^N] / i
```

Both forms are equivalent; the instructor prefers the difference-of-perpetuities form because it directly communicates the underlying logic.

## Key Takeaway

The only formulas you need for time value of money are:
- **Perpetuity:** `PV = PMT / i`
- **Present value discounting:** `PV = FV / (1+i)^N`

Everything else — annuities, growing perpetuities, etc. — is a derived combination.

## See Also

- [[Annuity]]
- [[Perpetuity]]
- [[Time Value of Money]]
- [[M3: Perpetuity]]
