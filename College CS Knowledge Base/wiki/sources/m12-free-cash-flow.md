---
title: "M12: Free Cash Flow"
type: source
tags: [finance, free-cash-flow, valuation, accounting, ebit, wacc, capital-budgeting]
sources: [m12-free-cash-flow]
course: Corporate Finance and Valuation
updated: 2026-09-13
---

This transcript defines [[Free Cash Flow]] as a concept rather than a formula, then walks through each adjustment in the FCF equation from EBIT, explaining the *why* behind each term. The instructor also notes why interest tax shields are excluded from FCF (they are captured in WACC instead, to avoid double-counting).

## Conceptual Definition

**Free cash flow** = the cash a firm generates in a period that is *free for distribution to investors*. If FCF is negative, the firm must raise cash from investors or draw down reserves.

FCF is calculated **as if the firm had no debt** — the interest tax deduction is excluded from FCF and captured separately in the discount rate (WACC). Including it in both would double-count it.

## FCF Formula

```
FCF = EBIT × (1 − t)
    + Depreciation & Amortization   [add back non-cash expenses]
    − Change in Gross Fixed Assets  [subtract actual capex]
    − Change in Net Working Capital [subtract non-cash earnings / cash tied up in operations]
```

## Explanation of Each Adjustment

**EBIT × (1 − t):** Approximates after-tax operating income assuming no debt. Using the tax rate on EBIT is an approximation; the tax code's accelerated depreciation rules make the exact figure more complex.

**+ D&A:** Depreciation and amortization reduce EBIT but are non-cash. To go from earnings to cash, add them back. Same logic applies to asset impairments and other non-cash charges.

**− ΔGFA (change in gross fixed assets):** Capital expenditures on property, plant & equipment are real cash outflows not captured in EBIT. Must subtract them.

**− ΔNWC (change in net working capital):** NWC = (Receivables + Inventory + Other current assets) − (Payables + Accrued expenses + Other current liabilities). Key components:
- *Accounts receivable increases:* Revenue booked but cash not yet received → subtract.
- *Inventory increases:* Cash spent on inventory before it is sold (not yet in EBIT) → subtract.
- *Accounts payable increases:* Expense recognized but cash not yet paid → add back (reduces subtraction).

## Formula Is Not Exhaustive

The formula covers the most common adjustments. Always reason from the concept: "Is this cash the firm can distribute to investors, or not?" Examples of items not in the standard formula:
- Purchase of patents/IP → subtract (cash out, not in EBIT)
- Unrealized gains → subtract from income (non-cash income)
- Residual value of equipment at project end → add (cash in, not in EBIT)

## See Also

- [[Free Cash Flow]]
- [[Net Present Value]]
- [[M11: Importance of Accounting]]
- [[M10: NPV Rule Is Superior]]
- [[CAPM]]
- [[WACC]]
