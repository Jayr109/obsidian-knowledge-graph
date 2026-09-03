---
title: "WACC"
type: concept
tags: [finance, wacc, cost-of-capital, capm, capital-structure, discounting, valuation]
sources: [m13-integrating-concepts-part2, m12-free-cash-flow]
course: Corporate Finance and Valuation
updated: 2026-08-25
---

The Weighted Average Cost of Capital (WACC) is the blended required return on a firm's total capital, weighting the after-tax cost of debt and the cost of equity by their market-value shares. WACC is the appropriate discount rate for a project's [[Free Cash Flow]] when the project's risk matches the firm's overall risk and is financed with the firm's existing debt/equity mix.

## Formula

```
WACC = (E/V) × r_e + (D/V) × r_d × (1 − t)
```

| Symbol | Meaning |
|---|---|
| E | Market value of equity |
| D | Market value of debt (book value often used as proxy if firm is not in distress) |
| V | Total firm value = E + D |
| r_e | Cost of equity (typically from [[CAPM]]) |
| r_d | Cost of debt (pre-tax; e.g., interest rate on firm's borrowing) |
| t | Corporate tax rate |

The `(1 − t)` factor on r_d reflects the interest tax shield: interest is tax-deductible, so the true after-tax cost of debt is lower than the stated rate.

## Why (1 − t) Belongs in WACC, Not FCF

[[Free Cash Flow]] is computed as if the firm has no debt (unlevered net income), so the interest tax shield is excluded from the FCF numerator. Capturing it once in WACC (the denominator of the DCF) avoids double-counting. This is the standard WACC-based DCF approach.

## Computing the Cost of Equity (CAPM)

The cost of equity r_e is normally estimated with the Capital Asset Pricing Model:

```
r_e = r_f + β × ERP
```

Match the risk-free rate's maturity to the project life, use a recent β, and use a **forward-looking** equity risk premium rather than a historical average. See [[CAPM]] for how to source each input.

## Capital Structure Weights

Use **market values**, not book values:
- Equity: use market capitalization from a financial data provider.
- Debt: use total debt from the balance sheet as a proxy for market value of debt (acceptable unless the firm is in financial distress, in which case market value of debt < book value).
- If preferred stock exists, add a third term: `(P/V) × r_p`.

## When to Use Firm WACC vs. Project-Specific WACC

| Situation | Use |
|---|---|
| Project risk ≈ firm's overall risk | Firm WACC |
| Project has meaningfully different risk profile | Project-specific WACC (e.g., comparable pure-play firm's beta) |

Example: a packaging company evaluating a new packaging product → firm WACC is appropriate. If that same company were evaluating an unrelated biotech venture, a different WACC would be needed.

## All WACC Inputs Are Point-in-Time

Beta, market cap, debt levels, Treasury rates, and ERP estimates all change continuously. A WACC computed today may differ meaningfully from one computed six months ago. Always use the most current data available.

## See Also

- [[CAPM]]
- [[Free Cash Flow]]
- [[Net Present Value]]
- [[Diversification]]
- [[M13: Integrating Concepts, Part 2]]
- [[M12: Free Cash Flow]]
