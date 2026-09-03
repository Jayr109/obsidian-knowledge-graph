---
title: "Overview"
type: overview
tags: [overview, synthesis]
sources: []
updated: 2026-04-09
---

This knowledge base documents a personal day trading system focused on Micro E-mini futures — [[MNQ1]] (Nasdaq-100) and [[MES1]] (S&P 500). The core thesis is momentum trading via price action setups: zone/level identification, breakout confirmation, and retest entry. All strategies target 3:1 R/R where applicable and close positions by end of day.

## Current State

Three strategies are documented, covering both instruments across all electronic trading hours. Two core concepts underpin all three strategies: [[Failed Breakout]] (liquidity sweeps and wick rejections) and [[Opening Range Breakout]] (momentum via breakout + retest). Session-level tracking ([[Session Levels]]) adds confluence to the MES1 strategy.

## Thesis

Price action around identifiable zones — whether formed by prior candle ranges, opening ranges, or session extremes — produces high-probability reversals and continuations. The entry edge comes not from predicting direction but from waiting for confirmation (a close, a failed test, or a candle-by-candle filter) before committing to a trade.

## Key Themes

- **Zone-based trading:** All strategies use a defined price zone as the structural anchor (prior 1H candle, 15M ORB, 7AM zone).
- **Retest entry:** Entries are taken on retests of broken zones, not on the initial breakout. This reduces chasing and defines risk clearly.
- **Confirmation candles:** Strategies require a bar close (or extra confirmation candle) before entering, filtering out noise and repaints.
- **Session context:** Asian and London session levels are tracked as liquidity pools that the US session frequently targets.

## Instruments

- [[MNQ1]] — Micro E-mini Nasdaq-100; two strategies
- [[MES1]] — Micro E-mini S&P 500; two strategies

## Strategies

- [[1H Wick Rejection]] — 1H false breakout on both instruments; active all electronic hours
- [[15M ORB Retest]] — 5M entry off 15M opening range; MNQ1 only; US session
- [[7AM Zone and Session Levels]] — Pre-market zone + session levels; MES1 only; US session

## Concepts

- [[Failed Breakout]] — liquidity sweeps, stop hunts, wick rejections
- [[Opening Range Breakout]] — momentum via early-session range definition
- [[Session Levels]] — Asia/London highs and lows as confluence points

## Open Questions

- Which strategy has the highest historical win rate and Sharpe ratio?
- Does the 1H wick rejection perform differently across Asia, London, and US sessions?
- Can ML feature engineering identify conditions where each strategy underperforms (to filter trades)?

## See Also

- [[index]] — full catalog of all pages
