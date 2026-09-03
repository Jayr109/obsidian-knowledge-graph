---
title: "Opening Range Breakout"
type: concept
tags: [concept, ORB, opening-range, breakout, momentum]
sources: []
updated: 2026-04-09
---

The Opening Range Breakout (ORB) is a momentum strategy framework that defines a price range from the early minutes of a session, then trades the breakout direction when price exits that range with conviction.

## Definition

The "opening range" is the high and low established during a defined early-session window. Common windows: first 5 minutes, first 15 minutes, first 30 minutes. Once price breaks out of this range, the expectation is that momentum continues in the breakout direction — at least long enough to reach a defined target.

## How It Is Used Here

Two strategies use ORB-based logic:

**[[15M ORB Retest]] (MNQ1):**
- Opening range = first 15-minute candle from 8:30 AM CST.
- Breakout = 5-minute close above/below the range.
- Entry = retest of range after breakout (not the breakout itself).
- This is a retest variant — lower risk than chasing the breakout, but requires patience.

**[[7AM Zone and Session Levels]] (MES1):**
- Reference zone = 7:00–7:15 AM CST 15-minute candle (pre-market).
- Breakout = close 5–10 points outside the zone after 8:30 AM.
- Entry = retest into the zone at the top, bottom, or midpoint.
- Longer time horizon from zone formation to breakout than a standard ORB.

## Retest Entry Logic

Both strategies use retest entries rather than direct breakout entries. Rationale:
- Avoids chasing extended moves.
- Provides a defined reference point (the range boundary) for stop placement.
- If the breakout is real, price typically retests the broken range before continuing.

## Key Distinctions

- A wick pierce of the range does **not** constitute a breakout — a candle close is required (in the MNQ1 strategy) or a close with 5–10 pt clearance (in the MES1 strategy).
- A failed retest (price breaks back through the range in the opposite direction) invalidates the setup.

## See Also

- [[15M ORB Retest]] — MNQ1 ORB strategy
- [[7AM Zone and Session Levels]] — MES1 zone-based ORB variant
- [[Failed Breakout]] — the inverse pattern; when breakouts fail and reverse
- [[Session Levels]] — levels that add confluence to ORB entries
