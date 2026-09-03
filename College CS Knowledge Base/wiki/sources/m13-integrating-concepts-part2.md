---
title: "M13: Integrating Concepts, Part 2"
type: source
tags: [finance, wacc, capm, beta, cost-of-capital, npv, amcor, worked-example, damodaran]
sources: [m13-integrating-concepts-part2]
course: Corporate Finance and Valuation
updated: 2026-04-21
---

Continuation of the Amcor worked example from [[M13: Integrating Concepts, Part 1]]. Computes the [[WACC]] from Yahoo Finance and Barron's data, then discounts the FCF forecast to arrive at NPV. Demonstrates the full capital budgeting pipeline end-to-end.

## Choosing the Discount Rate

The Amcor project is a new packaging product at a packaging company — risk profile is essentially identical to the firm as a whole. Therefore we use the **firm's WACC** rather than a project-specific cost of capital. If the project had a very different risk profile (e.g., a packaging company entering biotech), a project-specific rate would be required.

## Finding the Inputs (as of Nov 15, 2022)

### Beta
- Yahoo Finance did not show beta for Amcor at the time of recording.
- **Barron's** showed β = **0.93**.
- Beta is an estimate and changes over time — values will differ on any date other than Nov 15, 2022.

### Market Value of Equity
- From Yahoo Finance market cap: **$17,727M**

### Book Value of Debt (proxy for market value)
- Yahoo Finance → Financials → Balance Sheet → Total Debt (latest quarter): **$6,983M** (in thousands in the filing; converted to millions)
- No preferred stock → only debt and equity in capital structure
- Assumption: firm is not in distress, so book ≈ market value of debt

### Capital Structure Weights
```
Total Firm Value (V) = E + D = 17,727 + 6,983 = 24,710M
%E = 17,727 / 24,710
%D = 6,983 / 24,710
```

### Risk-Free Rate
- Source: U.S. Treasury par yield curve
- No 4-year rate available → linearly interpolate between 3-year and 5-year:
  - 3-year: 4.00%, 5-year: 4.24%
  - **r_f = (4.00 + 4.24) / 2 = 4.12%**

### Equity Market Risk Premium (ERP)
- Do NOT use a long-run historical average — that is a common mistake; it is backward-looking.
- Use a **forward-looking** estimate. Recommended source: **Aswath Damodaran (NYU Stern)**, who publishes a monthly ERP estimate derived from S&P 500 analyst earnings growth forecasts and current valuations.
  - URL: `pages.stern.nyu.edu/~adamodar/`
  - ERP as of Nov 2022: **4.59%**

### Cost of Debt
- Given in problem: **5%** (firm's line of credit rate)

## CAPM: Cost of Equity

```
r_e = r_f + β × ERP
    = 4.12% + 0.93 × 4.59%
    ≈ 8.39%
```

## WACC Formula

```
WACC = (%E × r_e) + (%D × r_d × (1 − t))
```

The `(1 − t)` term reflects the tax deductibility of interest. This tax shield is captured here in the discount rate, **not** in the FCF numerator (to avoid double-counting).

## NPV Calculation

Each period's FCF (from Part 1) is discounted:
```
PV(FCF_t) = FCF_t / (1 + WACC)^t
NPV = Σ PV(FCF_t)
```

The resulting NPV is positive → project increases firm value → accept the project.

This is the correct decision rule: maximize firm value by accepting all positive-NPV projects.

## Key Takeaways

1. **When to use firm WACC vs. project WACC:** Use firm WACC only when the project's risk matches the firm's overall risk. Divergent risk profiles require a project-specific rate.
2. **Beta sourcing:** Yahoo Finance may not always have beta; Barron's and other financial data providers are valid alternatives.
3. **Forward-looking ERP:** Damodaran's monthly estimate is preferable to historical averages for capital budgeting.
4. **All inputs are point-in-time estimates:** Beta, market cap, debt, Treasury rates, and ERP all change. The WACC and NPV computed here are valid for Nov 15, 2022 only.

## See Also

- [[WACC]]
- [[M13: Integrating Concepts, Part 1]]
- [[Net Present Value]]
- [[Free Cash Flow]]
- [[Diversification]]
