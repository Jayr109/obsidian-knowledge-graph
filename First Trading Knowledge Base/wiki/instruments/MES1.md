---
title: "MES1"
type: instrument
tags: [instrument, futures, S&P500, micro, MES1]
sources: []
updated: 2026-04-09
---

MES1 is the continuous front-month contract for the Micro E-mini S&P 500 futures, traded on the CME Group exchange. It is 1/10th the size of the standard E-mini S&P 500 (ES) and is the primary instrument for small-account futures trading of the S&P 500 index.

## Contract Specs

- **Underlying:** S&P 500 Index
- **Multiplier:** $5 per index point
- **Tick size:** 0.25 points = $1.25 per tick
- **Exchange:** CME Globex
- **Session:** Electronic trading nearly 24 hours (Sunday 5 PM – Friday 4 PM CT, 1-hour daily break)
- **Margin:** Low relative to ES; accessible for small accounts

## Strategies Used

- [[1H Wick Rejection]] — 1H false breakout / liquidity sweep strategy, active all electronic hours
- [[7AM Zone and Session Levels]] — Pre-market zone + session high/low strategy, 8:30 AM – 3:00 PM CST

## Characteristics for Trading

- Less volatile than MNQ1 on a point basis; more stable for stop placement.
- Highly correlated with ES and SPY.
- Session levels from Asian and London hours are frequently tested during the US open.
- The 7:00–7:15 AM CST candle is used as a pre-market reference zone.

## See Also

- [[MNQ1]] — Micro E-mini Nasdaq-100, often traded alongside MES1
- [[1H Wick Rejection]] — shared strategy with MNQ1
- [[7AM Zone and Session Levels]] — MES1-specific zone strategy
- [[Session Levels]] — Asian and London levels central to the MES1 zone strategy
