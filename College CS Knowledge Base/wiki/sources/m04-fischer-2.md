---
title: "M4: Fischer Equation — Part 2"
type: source
tags: [finance, interest-rates, inflation, real-rate, nominal-rate, fischer-equation]
sources: [m04-fischer-2]
course: Corporate Finance and Valuation
updated: 2026-04-10
---

This transcript derives the exact [[Fischer Equation]] relating nominal rates, real rates, and expected inflation, and shows that the approximation given in most textbooks (r_nominal ≈ r_real + π) can produce meaningful errors in practice.

## Derivation

To earn a 3% real return on $100 with 7% expected inflation, you need the nominal FV to equal:
```
Nominal FV = PV × (1 + r_real) × (1 + π_expected)
           = 100 × 1.03 × 1.07 = $110.21
```
So the nominal rate must be 10.21%.

**Exact Fischer Equation:**
```
1 + r_nominal = (1 + r_real)(1 + π_expected)

r_nominal = r_real + π + (r_real × π)
```

The cross-product term `r_real × π` is omitted in the textbook approximation. This is sometimes acceptable but can matter.

**Approximate Fischer Equation (textbook):**
```
r_nominal ≈ r_real + π
```

**Solving for real rate (exact, more commonly used in practice):**
```
r_real = (1 + r_nominal) / (1 + π_expected) − 1
```

## Error Analysis

With r_nominal = 10.21% and π = 7%:
- Exact r_real = 3.00%
- Approximate r_real = 10.21% − 7% = 3.21% → overstates real rate by 0.21%

On a $2M retirement account, overestimating the real rate by 0.21% means overestimating real income by $4,200/year — enough for a "nice vacation."

## See Also

- [[Fischer Equation]]
- [[M4: Fischer Equation — Part 1]]
- [[Time Value of Money]]
