---
title: "Free Cash Flow"
type: concept
tags: [finance, free-cash-flow, accounting, ebit, capital-budgeting, valuation, wacc]
sources: [m12-free-cash-flow, m11-importance-of-accounting, m13-integrating-concepts-part1]
course: Corporate Finance and Valuation
updated: 2026-04-21
---

Free Cash Flow (FCF) is the cash a firm or project generates in a given period that is available for distribution to investors. It is computed starting from EBIT and adjusting for taxes, non-cash items, capital expenditures, and changes in working capital — always ignoring the interest tax shield, which is captured separately in the discount rate (WACC).

## Conceptual Definition

"Free" means free for distribution: FCF is the net cash the firm could theoretically hand to all investors (debt and equity holders combined) in a period. If FCF < 0, the firm must raise cash from investors or draw down reserves to operate.

## Formula

```
FCF = EBIT × (1 − t)
    + Depreciation & Amortization
    − Change in Gross Fixed Assets (CapEx)
    − Change in Net Working Capital
```

## Why Each Adjustment

| Adjustment | Direction | Reason |
|---|---|---|
| EBIT × (1−t) | Starting point | After-tax operating income as if firm had no debt |
| + D&A | Add back | Non-cash expense in EBIT; does not reduce cash |
| − ΔGFA | Subtract | Actual cash outflow for capex not in EBIT |
| − ΔNWC | Subtract | Accounts receivable growth = revenue not yet received; inventory growth = cash spent before EBIT |
| (ΔNWC partially offset) | | Accounts payable growth adds back because expense recognized before cash paid |

**Net Working Capital:**
```
NWC = Receivables + Inventory + Other Current Assets
    − Payables − Accrued Expenses − Other Current Liabilities
```

## Why Interest Tax Shields Are Excluded

Including the tax deduction on interest in FCF *and* in the discount rate (WACC) would double-count it. The standard approach: exclude from FCF, capture in WACC. This lets you value the firm as if all-equity financed, then account for debt tax benefits in the discount rate.

## Formula Is Not Exhaustive

The FCF formula covers the most common items. Always reason from the concept when unusual items appear:
- Cash out not in EBIT → subtract (e.g., patent purchases)
- Cash in not in EBIT → add (e.g., equipment residual value at project end)
- Non-cash income in EBIT → subtract (e.g., unrealized gains)
- Non-cash expense in EBIT → add back (e.g., asset impairments)

## See Also

- [[Net Present Value]]
- [[M12: Free Cash Flow]]
- [[M11: Importance of Accounting]]
