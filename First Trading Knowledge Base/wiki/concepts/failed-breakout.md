---
title: "Failed Breakout"
type: concept
tags: [concept, price-action, liquidity, failed-breakout, wick-rejection]
sources: []
updated: 2026-04-09
---

A failed breakout occurs when price pierces beyond a known level or range — triggering stop orders and breakout traders — but then reverses back inside the range, trapping those who entered on the breakout. It is also called a liquidity sweep, stop hunt, or wick rejection.

## Mechanics

Markets consolidate around identifiable levels (prior highs/lows, candle ranges, session extremes). Stop-loss orders cluster just beyond these levels. When price briefly exceeds these levels, it triggers a cascade of stops (adding momentum) and entices breakout traders to enter. If the move cannot sustain, price reverses sharply, leaving trapped traders who must exit at a loss — accelerating the reversal.

## How to Identify

- A candle wick extends beyond a clearly defined prior high or low.
- The candle **closes back inside** the prior range or body (not just inside the full wick zone).
- Volume may spike at the wick extreme (stop triggering) then dry up on the reversal.

## Application in Strategies

**[[1H Wick Rejection]]:** The primary setup is a 1H candle that wicks beyond the prior 1H candle's range but closes back inside the prior candle's body. Entry is taken in the direction of the reversal with the wick as the invalidation point.

The close-back-inside-the-body requirement is stricter than a close inside the full range — it filters out ambiguous wicks and increases the probability of a sustained reversal.

## Relationship to Liquidity

Failed breakouts are a consequence of liquidity engineering: market makers or large participants drive price into stop clusters, fill their own orders at favorable prices, then reverse. Understanding this explains why the entry is taken after the close back inside — at that point, the liquidity has been swept and the reversal is underway.

## See Also

- [[1H Wick Rejection]] — strategy built on this concept
- [[Session Levels]] — levels where liquidity sweeps frequently occur
- [[Opening Range Breakout]] — a related breakout concept (successful breakouts vs. failed ones)
