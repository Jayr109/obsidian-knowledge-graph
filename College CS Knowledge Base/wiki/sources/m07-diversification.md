---
title: "M7: Diversification"
type: source
tags: [finance, risk, diversification, portfolio, volatility, correlation]
sources: [m07-diversification]
course: Corporate Finance and Valuation
updated: 2026-04-10
---

This transcript demonstrates [[Diversification]] using an Excel-based portfolio analysis with four stocks — Tesla, NVIDIA, Ford, and ExxonMobil — over Oct 2019–Oct 2022. It shows numerically and visually that combining stocks reduces portfolio volatility below the volatility of individual holdings.

## Portfolio Construction

Stocks chosen to span different sectors:
- **Tesla** — EV / high-growth tech (very high volatility)
- **NVIDIA** — AI semiconductors (also high volatility)
- **Ford** — traditional auto (moderate volatility)
- **ExxonMobil** — oil & gas (lowest volatility of the four)

Portfolio returns computed as weighted average of individual stock returns. Instructor uses equal weights for simplicity, but notes real portfolios often use different weights (e.g., 60/40).

## Key Finding

As stocks are added to the portfolio, volatility (measured by `STDEV.S`) falls:

| Portfolio | Composition |
|---|---|
| 2-stock | Tesla + NVIDIA |
| 3-stock | + Ford |
| 4-stock | + ExxonMobil |

The "magic of diversification": a portfolio that is **50% ExxonMobil + 50% (equal-weight Tesla, NVIDIA, Ford)** achieves *lower* volatility than ExxonMobil alone — even though the three added stocks are *all more volatile* than ExxonMobil.

## Why Diversification Works

Random fluctuations in individual stock returns are **uncorrelated** — when Tesla randomly drops, the others are unlikely to drop for the same reason. These idiosyncratic fluctuations cancel out in the portfolio, reducing total variance without reducing expected return. This is the fundamental argument for holding many stocks.

## Takeaway

With the right portfolio weights, there always exists a combination of stocks with lower risk than the least risky individual stock. This is why money managers stress diversification and advocate for holding as many stocks as feasible.

## See Also

- [[Diversification]]
- [[Volatility]]
- [[M7: Calculating Volatility]]
