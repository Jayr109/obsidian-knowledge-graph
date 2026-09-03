---
title: "Annuity"
type: concept
tags: [finance, time-value-of-money, annuity, present-value]
sources: [m03-annuity]
course: Corporate Finance and Valuation
updated: 2026-04-10
---

An annuity is a finite stream of equal periodic payments over N periods. Its present value is derived as the difference between two [[Perpetuity|perpetuities]], making it easy to remember and understand without memorizing a separate formula.

## Definition

An annuity pays a fixed amount PMT at the end of each period for exactly N periods, then stops.

## Derivation (Difference of Perpetuities)

1. **Perpetuity A:** first payment at time 1, paying PMT forever. PV_A = PMT / i.
2. **Perpetuity B:** first payment at time N+1, paying PMT forever. PV as of time N = PMT/i. PV today = (PMT/i) / (1+i)^N.
3. **Annuity = A − B:** for periods 1 through N, both perpetuities pay PMT; after period N, they cancel. Net: PMT for N periods only.

**Preferred form (shows the logic):**
```
PV = PMT/i  −  PMT / [i × (1+i)^N]
```

**Textbook form (equivalent after algebra):**
```
PV = PMT × [1 − 1/(1+i)^N] / i
```

## Key Insight

The instructor emphasizes: you only need two formulas — `PV = PMT/i` (perpetuity) and `PV = FV/(1+i)^N` (discounting). The annuity formula follows automatically. Memorizing it as a separate fact misses the underlying structure.

## See Also

- [[Perpetuity]]
- [[Time Value of Money]]
- [[M3: Annuity]]
