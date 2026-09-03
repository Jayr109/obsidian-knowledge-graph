---
title: "Net Present Value"
type: concept
tags: [finance, capital-budgeting, npv, investment-rules, valuation, discounted-cash-flow]
sources: [m10-npv-rule-is-superior, m12-free-cash-flow, m13-integrating-concepts-part2]
course: Corporate Finance and Valuation
updated: 2026-04-21
---

Net Present Value (NPV) is the sum of all discounted future cash flows from an investment minus the initial outlay. It is the only investment decision rule that directly measures the degree to which a project increases or decreases the value of a firm. The **NPV Rule** says: invest in projects with positive NPV; of mutually exclusive projects, choose the one with the highest NPV.

## Definition

```
NPV = −Initial Investment + Σ [FCF_t / (1 + r)^t]
```
where `FCF_t` is [[Free Cash Flow]] in period t and r is the discount rate (typically WACC).

## The NPV Rule

**Accept:** if NPV > 0 (project increases firm value)
**Reject:** if NPV < 0 (project destroys value)
**Mutually exclusive projects:** choose the one with highest NPV

## Why NPV Is Superior

The course makes a strong case that NPV is not just *a* good rule — it is the *only* correct rule:

| Rule | What It Measures | Problem |
|---|---|---|
| **NPV** | Net value created | — (gold standard) |
| IRR | Rate of return | Can conflict with NPV for mutually exclusive projects |
| Payback Period | How fast you get your money back | Ignores time value of money entirely |
| Profitability Index | NPV per dollar invested | Approximation useful only under capital constraints |

**IRR vs. NPV for mutually exclusive projects:** A bigger project with a lower rate of return may create more total value than a smaller project with a higher rate of return. IRR picks the wrong one; NPV picks correctly. Example: building a shopping district (low IRR, high NPV) vs. an apartment complex (high IRR, low NPV) on the same parcel.

**Payback period:** The instructor is blunt — "financial managers who know what they are doing generally do not use the payback period as a decision rule." It fails to account for time value and can lead to rejecting long-term value-creating projects.

## Profitability Index (Capital Rationing Context)

When capital is constrained (cannot fund all positive-NPV projects), rank by NPV per dollar invested:
```
PI = NPV / Initial Investment
```
Use PI as a quick heuristic only. For rigorous capital rationing, enumerate all feasible project combinations and select the one with maximum total NPV.

## Connection to Free Cash Flow

NPV analysis requires projecting [[Free Cash Flow]] for each period, then discounting at the appropriate risk-adjusted rate. See [[M12: Free Cash Flow]] for how FCF is constructed from accounting data.

## See Also

- [[Free Cash Flow]]
- [[Time Value of Money]]
- [[M10: NPV Rule Is Superior]]
- [[M12: Free Cash Flow]]
