---
title: "Perpetuity"
type: concept
tags: [finance, time-value-of-money, perpetuity, present-value, bonds]
sources: [m03-perpetuity, m03-annuity]
course: Corporate Finance and Valuation
updated: 2026-04-10
---

A perpetuity is a financial instrument that pays a fixed amount (PMT) at regular intervals forever. Its present value formula is the single most important building block in time-value-of-money analysis: `PV = PMT / i`.

## Definition

A perpetuity is an infinite stream of equal periodic payments. There is no maturity date — payments continue indefinitely.

**Historical example:** British consol bonds issued in 1927 to refinance WWI debt. Investors paid £1,000 and received £40 per year (4%) forever, with payments passing to heirs in perpetuity.

## Formula Derivation

The payment equals the invested principal times the interest rate:
```
PMT = PV × i
```
Solving for PV:
```
PV = PMT / i
```
This is an eighth-grade algebra step. The formula comes directly from the definition of interest.

**Example:** £40 annual payment at 4% → PV = 40 / 0.04 = £1,000.

## Why It Matters

The perpetuity formula is the foundation for the [[Annuity]] formula. An annuity is the *difference* between two perpetuities:
- Perpetuity 1: pays from time 1 forever → PV = PMT/i
- Perpetuity 2: pays from time N+1 forever → PV = (PMT/i) / (1+i)^N
- Annuity = Perpetuity 1 − Perpetuity 2

## See Also

- [[Annuity]]
- [[Time Value of Money]]
- [[M3: Perpetuity]]
- [[M3: Annuity]]
