---
title: "1H Wick Rejection"
type: strategy
tags: [strategy, price-action, futures, MNQ1, MES1, wick-rejection, failed-breakout]
sources: []
updated: 2026-04-09
---

A price action strategy applied to the 1H chart on MNQ1 and MES1 during all electronic trading hours. It targets failed breakout moves where a candle's wick pierces beyond the prior candle's range but the candle body closes back inside — signaling a liquidity sweep and rejection.

## Setup Rules

1. After each 1H candle closes, mark its full range: body open/close and both wicks (high and low).
2. Observe the following candle as it develops.

## Entry Conditions

**Long (Bearish prior candle → bullish reversal):**
- Prior 1H candle is bearish (close < open).
- Current candle's wick goes **below** the prior candle's low.
- Current candle **closes back inside** the prior candle's body.
- Enter long at the **bottom of the current candle's body** (close, since it's the lower end of a bearish close candle — or open if bullish close).
- Stop loss: just below the current candle's wick low.
- Take profit: top of the prior candle's body (prior candle's open, the high of the body).

**Short (Bullish prior candle → bearish reversal):**
- Prior 1H candle is bullish (close > open).
- Current candle's wick goes **above** the prior candle's high.
- Current candle **closes back inside** the prior candle's body.
- Enter short at the **top of the current candle's body**.
- Stop loss: just above the current candle's wick high.
- Take profit: bottom of the prior candle's body (prior candle's open).

## Key Characteristics

- Applies to both [[MNQ1]] and [[MES1]].
- Active during all electronic trading hours (no time filter).
- No fixed R/R ratio — TP and SL are defined by candle structure.
- Core pattern: [[Failed Breakout]] / liquidity sweep — market hunts stops beyond a prior range then reverses.

## Risk Notes

- The wick that triggers the entry must pierce **beyond** the prior candle's range (not just touch).
- Closing back inside the body is the confirmation — a close merely inside the full wick range (but not the body) is not a valid signal.
- False signals are most common during low-volume overnight sessions.

## See Also

- [[Failed Breakout]] — the underlying price action concept
- [[MNQ1]] — Micro E-mini Nasdaq-100 futures
- [[MES1]] — Micro E-mini S&P 500 futures
- [[15M ORB Retest]] — complementary ORB strategy used on MNQ1
- [[7AM Zone and Session Levels]] — complementary zone strategy used on MES1
