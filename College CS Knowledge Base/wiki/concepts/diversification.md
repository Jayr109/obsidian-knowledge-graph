---
title: "Diversification"
type: concept
tags: [finance, risk, diversification, portfolio, volatility, correlation]
sources: [m07-diversification]
course: Corporate Finance and Valuation
updated: 2026-04-10
---

Diversification is the practice of combining multiple assets in a portfolio to reduce overall risk ([[Volatility]]) without sacrificing expected return. It works because the random fluctuations in individual asset returns are imperfectly correlated — they tend to cancel out when combined.

## The Core Principle

When returns are not perfectly correlated, combining stocks reduces portfolio variance. In the extreme case, with perfectly uncorrelated assets, diversification eliminates all idiosyncratic risk.

**Key result demonstrated empirically in the course:** With the right portfolio weights, there always exists a combination of risky stocks that has *lower volatility* than the least volatile individual stock in the portfolio.

## Demonstrated Example (Tesla, NVIDIA, Ford, ExxonMobil)

| Portfolio | Contents | Volatility |
|---|---|---|
| Tesla alone | — | ~70% (annualized) |
| 2-stock | Tesla + NVIDIA | Lower than Tesla |
| 3-stock | + Ford | Lower than 2-stock |
| 4-stock | + ExxonMobil | ~= ExxonMobil alone |
| 50/50 (weighted) | 50% ExxonMobil + 50% (Tesla, NVIDIA, Ford equal-weight) | *Lower than ExxonMobil alone* |

The last result is striking: adding three *more volatile* stocks to ExxonMobil with a 50% ExxonMobil weight produces a portfolio *less volatile* than ExxonMobil by itself.

## Why It Works

Random idiosyncratic fluctuations in individual stocks are uncorrelated — a random bad week for Tesla says nothing about a random bad week for ExxonMobil. When combined in a portfolio, these uncorrelated fluctuations cancel each other. Only **systematic risk** (market-wide fluctuations that hit all stocks simultaneously) cannot be diversified away.

## Investment Implication

- Hold as many stocks as possible in your portfolio.
- The more stocks you add, the more idiosyncratic risk you eliminate.
- Diversification is "free" — it reduces risk without reducing expected return.
- Money managers stress diversification for this reason.

## Portfolio Return Formula

For a portfolio with weights w_1, w_2, ..., w_n:
```
r_portfolio = w_1 × r_1 + w_2 × r_2 + ... + w_n × r_n
```
Equal weights: `r_portfolio = (r_1 + r_2 + ... + r_n) / n`

## See Also

- [[Volatility]]
- [[M7: Diversification]]
- [[M7: Calculating Volatility]]
