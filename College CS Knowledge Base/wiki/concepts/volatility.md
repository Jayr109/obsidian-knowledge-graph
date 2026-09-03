---
title: "Volatility"
type: concept
tags: [finance, risk, volatility, standard-deviation, stock-returns, portfolio]
sources: [m07-calculating-volatility, m07-diversification]
course: Corporate Finance and Valuation
updated: 2026-04-10
---

Volatility, in finance, is the standard deviation of periodic returns on a financial asset. It is the primary measure of total risk for a stock or portfolio. A high-volatility stock has highly unpredictable returns; a low-volatility stock's returns are more stable.

## Definition

For a series of returns r_1, r_2, ..., r_T:
```
σ = STDEV.S(r_1, ..., r_T)   [sample standard deviation]
```

This gives volatility in the same units as the return period (e.g., weekly vol for weekly returns).

## Annualization

To convert from weekly volatility to annual:
```
σ_annual = σ_weekly × √52
```

More generally:
```
σ_annual = σ_period × √(periods per year)
```

This follows from the assumption that returns are i.i.d. across periods (variance scales linearly, so standard deviation scales with the square root).

## Estimating Historical Volatility — Procedure

1. Download 3 years of weekly adjusted closing prices (Yahoo Finance or similar).
2. Compute weekly returns: `r_t = Adj_Close_t / Adj_Close_{t-1} − 1`.
3. Apply `STDEV.S` to the return series.
4. Multiply by `√52` to annualize.

**Data choices:**
- Weekly (not daily): daily returns are too noisy.
- 3 years (not monthly): monthly data requires 5+ years for adequate sample size.
- Adjusted close: incorporates dividend reinvestment for total return.

**Tesla example (Nov 2019–Nov 2022):** weekly vol ≈ 10%; annualized ≈ 70%. Extremely volatile.

## Volatility and Diversification

Portfolio volatility is always less than the weighted-average volatility of its components when stocks are not perfectly correlated. See [[Diversification]] for the key result: with the right weights, a portfolio of stocks can achieve lower volatility than the *least* volatile stock in the portfolio.

## See Also

- [[Diversification]]
- [[M7: Calculating Volatility]]
- [[M7: Diversification]]
