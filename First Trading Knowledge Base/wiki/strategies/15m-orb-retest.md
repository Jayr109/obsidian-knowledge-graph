---
title: "15M ORB Retest"
type: strategy
tags: [strategy, ORB, opening-range-breakout, MNQ1, futures, momentum, 5M, 15M]
sources: []
updated: 2026-04-09
---

A momentum strategy on MNQ1 that uses the first 15-minute candle after the 8:30 AM CST open as a reference range, then waits for a breakout on the 5-minute chart and a subsequent retest of that range before entering in the breakout direction.

## Setup Rules

1. At 8:30 AM CST, mark the high and low of the first 15-minute candle (the opening range), including wicks.
2. Switch to the 5-minute chart to monitor for breakout.

## Entry Conditions

1. A 5-minute candle must **close** above the 15M range high (bullish breakout) or below the 15M range low (bearish breakout). Close required — not just a wick pierce.
2. After the breakout close, wait for price to **retest back into** the 15M range.
3. Enter in the direction of the original breakout on the retest.
   - Bullish breakout: enter long when price pulls back into or near the top of the 15M range.
   - Bearish breakout: enter short when price pulls back into or near the bottom of the 15M range.

## Risk Management

- **Stop loss:** Above the most recent 5-minute swing high (for shorts) or below the most recent 5-minute swing low (for longs) — the swing must predate the current candle and be against the trend.
- **Take profit:** 3:1 R/R ratio.
- **Break even:** Move stop to break even once trade is sufficiently in profit.
- **Time window:** 8:30 AM – 3:00 PM CST. Close all positions at end of day regardless of P&L.

## Key Characteristics

- Applied to [[MNQ1]] only (though the ORB concept is general).
- Two-timeframe approach: 15M for range, 5M for entry.
- Momentum direction is confirmed by the breakout candle close; entry is on the retest (lower-risk entry point vs. chasing the breakout).
- Uses [[Opening Range Breakout]] as the core concept.

## Risk Notes

- If price breaks out and retests but immediately continues through the range in the wrong direction, the setup is invalid.
- Avoid entries during significant pre-market news events that distort the opening range.
- The 5M swing high/low used for the stop must be **before** the current entry candle — using a more recent pivot will result in a stop that is too tight.

## See Also

- [[Opening Range Breakout]] — the underlying concept
- [[MNQ1]] — the instrument this strategy is applied to
- [[1H Wick Rejection]] — complementary strategy using 1H false breakouts
- [[7AM Zone and Session Levels]] — analogous zone-based strategy for MES1
