---
title: "MNQ1"
type: instrument
tags: [instrument, futures, Nasdaq, micro, MNQ1]
sources: []
updated: 2026-04-09
---

MNQ1 is the continuous front-month contract for the Micro E-mini Nasdaq-100 futures, traded on the CME Group exchange. It is 1/10th the size of the standard E-mini Nasdaq-100 (NQ) and is the primary instrument for small-account futures trading of the Nasdaq index.

## Contract Specs

- **Underlying:** Nasdaq-100 Index
- **Multiplier:** $2 per index point
- **Tick size:** 0.25 points = $0.50 per tick
- **Exchange:** CME Globex
- **Session:** Electronic trading nearly 24 hours (Sunday 5 PM – Friday 4 PM CT, 1-hour daily break)
- **Margin:** Low relative to NQ; accessible for small accounts

## Strategies Used

- [[1H Wick Rejection]] — 1H false breakout / liquidity sweep strategy, active all electronic hours
- [[15M ORB Retest]] — Opening range breakout strategy, 8:30 AM – 3:00 PM CST on the 5M chart

## Characteristics for Trading

- Highly correlated with NQ and QQQ.
- Volatile during US open (8:30 AM CST) and major macro events.
- London session (3:00 AM – 11:30 AM ET) often sets directional bias before US open.

## See Also

- [[MES1]] — Micro E-mini S&P 500, often traded alongside MNQ1
- [[1H Wick Rejection]] — shared strategy with MES1
- [[15M ORB Retest]] — MNQ1-specific ORB strategy
- [[Session Levels]] — Asian and London levels used for confluence
