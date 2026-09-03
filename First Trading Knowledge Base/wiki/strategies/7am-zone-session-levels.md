---
title: "7AM Zone and Session Levels"
type: strategy
tags: [strategy, MES1, futures, session-levels, zone, momentum, 15M, Asia, London]
sources: []
updated: 2026-04-09
---

A zone-based momentum strategy on MES1 that combines a pre-market 7:00–7:15 AM CST reference zone with untested Asian and London session highs/lows. A confirmed breakout at 8:30 AM triggers an entry on the retest of the zone, with a 3:1 R/R target.

## Setup Rules

1. Mark all **untested highs and lows** from the Asian session (6:00 PM – 3:00 AM ET) and London session (3:00 AM – 11:30 AM ET).
2. At 7:00 AM CST, mark the 15-minute candle from 7:00–7:15 AM, including full range with wicks. This is the reference zone.
3. Wait for 8:30 AM CST to observe the breakout.

## Breakout Condition

A candle must **close** 5–10 points outside the 7AM zone. This is a forcible exit — a wick pierce alone is insufficient.

## Entry Conditions

Once a breakout close is confirmed, wait for price to retest back into the 7AM zone. Three valid entry points:

1. **Top of zone** — used for longs after a bullish breakout; look for a failed move to the downside (price dips into zone but fails to break below).
2. **Bottom of zone** — used for shorts after a bearish breakout; look for a failed move to the upside.
3. **Midpoint of zone** — valid for either direction; requires only that price reaches the midpoint, even on a wick (no close required at midpoint).

**Confirmation rule:** For top/bottom entries, wait one candle after price touches the entry level to confirm it holds. Enter on the **next** candle after the level is respected. For midpoint entries, enter on the next candle after midpoint is touched.

## Risk Management

- **Stop loss:** 5–12 points, scaled to the size of the 7AM zone. Keep under 12 points when possible.
- **Take profit:** 3:1 R/R.
- **Time window:** 8:30 AM – 3:00 PM CST. Close all positions at end of day.

## Key Characteristics

- Applied to [[MES1]] only.
- Session levels (Asian/London highs and lows) provide confluence — entries near untested session levels carry higher conviction.
- The 7AM zone functions similarly to an ORB, but it is pre-market and requires a larger confirmed breakout (5–10 pts).
- Uses [[Session Levels]] and [[Opening Range Breakout]] concepts together.

## Risk Notes

- A breakout of only 1–4 points is ambiguous; wait for the full 5-point minimum close outside the zone.
- If price breaks out, retests, and immediately fails through the zone in the opposite direction, the setup is void.
- Large 7AM zones (>10 pts) may push the stop loss above 12 points — reduce size or skip the trade.

## See Also

- [[Session Levels]] — Asian and London high/low tracking
- [[Opening Range Breakout]] — core breakout concept
- [[MES1]] — the instrument this strategy is applied to
- [[1H Wick Rejection]] — complementary false-breakout strategy
- [[15M ORB Retest]] — analogous ORB strategy for MNQ1
