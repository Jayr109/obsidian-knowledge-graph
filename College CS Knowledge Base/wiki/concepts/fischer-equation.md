---
title: "Fischer Equation"
type: concept
tags: [finance, interest-rates, inflation, real-rate, nominal-rate, macroeconomics]
sources: [m04-fischer-1, m04-fischer-2]
course: Corporate Finance and Valuation
updated: 2026-04-10
---

The Fischer Equation (named for economist Irving Fischer) relates nominal interest rates, real interest rates, and expected inflation. It is the essential tool for converting between the quoted (nominal) rate you observe and the real rate of return on purchasing power.

## Exact Fischer Equation

```
1 + r_nominal = (1 + r_real)(1 + π_expected)
```

Expanding:
```
r_nominal = r_real + π + (r_real × π)
```

The cross-product term `r_real × π` is the difference between the exact and approximate forms.

## Approximate Fischer Equation (Textbook)

```
r_nominal ≈ r_real + π
```

This omits the cross-product term and is what most textbooks show (e.g., equations 6-2 and 6-3 in the course text). It is acceptable for small rates but can cause meaningful errors when both rates are large.

## Solving for Real Rate (Most Common Use in Practice)

Since nominal rates are observable and inflation estimates are available, the real rate is usually calculated from the nominal rate:

**Exact:**
```
r_real = (1 + r_nominal) / (1 + π_expected) − 1
```

**Approximate:**
```
r_real ≈ r_nominal − π_expected
```

## Error Analysis

With r_nominal = 10.21%, π = 7%:
- Exact r_real = 3.00%
- Approximate r_real = 3.21%
- Error: +0.21 percentage points

On a $2 million investment, this 0.21% error overstates real annual income by $4,200.

## Real vs. Nominal Rates — Definitions

| Term | Definition |
|---|---|
| Real interest rate | Rate at which purchasing power grows; what rate would be with zero inflation |
| Nominal interest rate | Quoted rate; affected by both real rate and inflation expectations |

The equilibrium real rate is determined by the supply and demand for loanable funds. The nominal rate adds inflation expectations on top.

## See Also

- [[Time Value of Money]]
- [[M4: Fischer Equation — Part 1]]
- [[M4: Fischer Equation — Part 2]]
