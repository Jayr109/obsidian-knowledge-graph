---
title: "M7: Calculating Volatility"
type: source
tags: [finance, risk, volatility, standard-deviation, stock-returns, excel]
sources: [m07-calculating-volatility]
course: Corporate Finance and Valuation
updated: 2026-04-10
---

This transcript is a walkthrough of how to estimate a stock's [[Volatility]] (standard deviation of returns) using historical weekly data downloaded from Yahoo Finance, demonstrated with Tesla as the example.

## Data Collection

- **Source:** Yahoo Finance → Historical Data tab → Adjusted Closing Price
- **Frequency:** Weekly preferred (daily is too noisy; monthly requires too much history for an adequate sample)
- **Period:** 3 years of weekly data (~156 observations) — reasonable compromise between sample size and recency
- **Column used:** Adjusted Close (corrects for dividends); Volume is discarded

## Calculation Steps

1. **Compute weekly returns:** `r_t = (Adj Close_t / Adj Close_{t-1}) − 1`
2. **Apply Excel's `STDEV.S` function** to the return series (sample standard deviation, not population)
3. **Annualize:** multiply by `√52` (square root of periods per year)

```
Weekly volatility × √52 = Annual volatility
```

**Tesla result (circa Nov 2019 – Nov 2022):** weekly vol ≈ 10 percentage points; annualized ≈ **70%** — extremely volatile.

## Data Choices

| Choice | Rationale |
|---|---|
| Weekly not daily | Daily returns too noisy |
| Weekly not monthly | Monthly requires 5+ years of history |
| 3-year window | Balances sample size vs. company-change risk |
| Adjusted close not close | Dividends affect total return |

## See Also

- [[Volatility]]
- [[Diversification]]
- [[M7: Diversification]]
