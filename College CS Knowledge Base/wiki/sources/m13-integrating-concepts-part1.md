---
title: "M13: Integrating Concepts, Part 1"
type: source
tags: [finance, free-cash-flow, capital-budgeting, depreciation, nwc, sunk-cost, amcor, worked-example]
sources: [m13-integrating-concepts-part1]
course: Corporate Finance and Valuation
updated: 2026-04-21
---

Worked demo that builds a complete [[Free Cash Flow]] forecast for a four-year project at Amcor, a packaging company. Brings together sunk cost identification, incremental investment classification, depreciation scheduling, inflation-adjusted revenues, and net working capital treatment in one spreadsheet model.

## The Amcor Problem Setup

**Project:** New RFID-tagged packaging product line  
**Key numbers:**
- $10M already spent on R&D → **sunk cost, ignore**
- $6.67M marketing expenses (immediate) → incremental, fully tax-deductible, goes above unlevered net income line
- $24M fixed asset purchase → incremental capex, goes below net income line
- 5-year DDB depreciation schedule (table 12.8, p. 334 of textbook), asset used for 4 years
- Sell assets at end of year 4 for $7M
- Year 1 (today's dollars): $60M sales, $25M COGS, $9M operating expenses
- Inflation: 7% in year 1, then 3% thereafter
- NWC: $5M immediate investment, then 10% of sales per year, fully recovered at project end
- Tax rate: 24%

## Sunk Cost Treatment

The $10M R&D is already incurred and non-recoverable regardless of whether the project proceeds. It is excluded from the FCF model entirely. Only incremental cash flows — those that differ between "do project" and "don't do project" — belong in the analysis.

## Income Statement Layout Convention

Expenses and cash outflows are coded as **negative numbers** throughout the model. This makes summing rows unambiguous (EBITDA = SUM of sales + COGS + OpEx), eliminating the need for long +/− formulas. Standard accounting statements code expenses as positive; this model diverges from that for modeling convenience.

## Depreciation Schedule

Assets are classified by the IRS as 5-year property. DDB percentages from table 12.8 are applied to the $24M initial tax basis each year:

```
Depreciation_t = DDB_percentage_t × 24M
Tax_basis_end_t = Tax_basis_end_{t-1} − Depreciation_t
```

The depreciation charges flow directly into the income statement as tax deductions (coded negative). The remaining tax basis at the end of year 4 is **not zero** because the 5-year schedule only partially depreciated the asset in four years.

## Asset Disposal (End of Year 4)

- **Cash inflow:** $7M (sale price)
- **Tax basis at end of year 4:** ~$4M (from depreciation schedule)
- **Capital gain:** $7M − $4M = $3M → taxed at 24%
- **FCF treatment:** Record the $7M cash inflow from sale. The capital gain is already embedded in that $7M, not additional cash. To avoid double-counting, subtract the gain-on-sale from FCF (since taxes on it reduce the net cash received).

## Inflation Adjustment for Operating Revenues

Sales, COGS, and operating expenses are given in today's dollars. Nominal values in each year are:
```
Nominal_t = Real_today × ∏(1 + π_s) for s=1..t
```
Year 1: multiply by (1 + 7%). Years 2–4: multiply by (1 + 3%) per year.

## Net Working Capital

NWC level in each year = 10% × sales (nominal). The **change** in NWC goes into FCF, not the level:
- Increases in NWC → cash outflows (like buying inventory)
- At project end: NWC recovers fully → cash inflow

Immediate NWC investment of $5M at year 0 is a cash outflow.

## From Unlevered Net Income to FCF

```
Unlevered Net Income = EBIT × (1 − t)       [ignores interest tax shield]
+ Depreciation (add back non-cash charge)
− Change in NWC
− Capex (purchase of fixed assets)
+ Proceeds from asset sale
− Capital gain on sale (already in proceeds, avoid double-count)
= Free Cash Flow
```

Why ignore interest? Interest tax savings are captured in the cost of capital (WACC). Including them here would double-count.

## See Also

- [[Free Cash Flow]]
- [[M13: Integrating Concepts, Part 2]]
- [[M12: Free Cash Flow]]
- [[Net Present Value]]
- [[WACC]]
