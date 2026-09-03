---
title: "CAPM"
type: concept
tags: [finance, capm, cost-of-equity, beta, equity-risk-premium, systematic-risk, discounting]
sources: [m13-integrating-concepts-part2, m12-free-cash-flow]
course: Corporate Finance and Valuation
updated: 2026-08-25
---

The Capital Asset Pricing Model (CAPM) estimates the cost of equity — the return investors require for bearing a stock's systematic risk. It is the standard input for the r_e term in [[WACC]].

## Formula

```
r_e = r_f + β × ERP
```

An asset's required return is the risk-free rate plus a premium scaled by how much systematic (non-diversifiable) risk it carries. Diversifiable risk earns no premium, because investors can eliminate it by holding a portfolio.

## The Three Inputs

| Input | Meaning | How to source it |
|---|---|---|
| **r_f** | Risk-free rate | U.S. Treasury par yield curve; **match maturity to project life** |
| **β** | Systematic risk relative to the market | Financial data providers (Yahoo Finance, Barron's) |
| **ERP** | Expected excess return of the market over r_f | A **forward-looking** estimate |

### Risk-free rate

Match the Treasury maturity to the life of the project being valued. Interpolate linearly when the exact maturity is unavailable — a 4-year project uses the average of the 3-year and 5-year Treasury rates.

### Beta

β measures co-movement with the market: β = 1 moves with the market, β > 1 amplifies it, β < 1 damps it. Beta is an *estimate* that drifts over time, so use the most recent available figure rather than a stale one.

### Equity risk premium

Use a forward-looking ERP, **not** a long-run historical average. A reliable monthly estimate is published by Aswath Damodaran (NYU Stern) at `pages.stern.nyu.edu/~adamodar/`, derived from analyst earnings forecasts for the S&P 500.

## Role in Valuation

CAPM supplies the cost of equity, which [[WACC]] blends with the after-tax cost of debt to produce the discount rate applied to [[Free Cash Flow]] in a DCF. Errors in β or ERP propagate straight into the discount rate and therefore into valuation — CAPM inputs are typically the least precise part of a DCF.

## See Also

- [[WACC]]
- [[Free Cash Flow]]
- [[Corporate Finance and Valuation]]
