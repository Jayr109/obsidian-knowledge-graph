---
title: "CSCE 420 Fall 2026 — 09-18 minmax.ipynb Walkthrough"
type: source
tags: [csce420, lecture-recording, fall-2026, minimax, game-playing, hw2, minmax-ipynb]
sources: []
course: CSCE 420
semester: Fall 2026
date: 2026-09-18
exam: midterm
updated: 2026-09-18
---

A 3 min 44 s in-class screen recording (Fall 2026, the user's section, [[Yoonsuck Choe]], captured 2026-09-18 at ~10:50 AM) in which the instructor walks through `minmax.ipynb`, the starter notebook for [[CSCE 420 Homework 2 — Game Playing, Logic]] Problem 3. Archived as `raw/CSCE420_HW1_Minimax_Explanation/` (video, faster-whisper transcript, `words.json`, and 15-second frames). The recording's filename says "HW1", but the content is the **HW2** alpha-beta starter — the same code as `raw/CSCE420_HW2_Fall2026_minmax.ipynb`, verified line for line against the frames.

> First real run of the video-ingest pipeline. Transcript quality was clean; ffmpeg scene detection at 0.20 found **zero** cuts on a notebook screen recording, so frames were pulled at a fixed 15 s interval instead and cropped to the notebook pane.

## What the Notebook Contains

- **Constants** `MAX = 99999`, `MIN = -99999` — the stand-ins for ±∞.
- **Game tree as a nested list**, the same LISP-style representation as the HW1 `dfs.ipynb` ([[CSCE 420 Homework 1 — Search]]): `Game_tree = [[7, [3, 8, 1], [15, 9]], [12, [17, 13]]]`. Two top-level elements = two MIN children of the MAX root; the first MIN node has three children (leaf 7, MAX node `[3, 8, 1]`, MAX node `[15, 9]`); the second has two (leaf 12, MAX node `[17, 13]`). Leaves can sit at different depths.
- **`minmax_decision(tree)`** — the slide version (loop over children calling `minmax_value(i, "min")`, keep the max) is left in as a comment; the live version is one line, `return minmax_value(tree, "max")`.
- **`minmax_value(tree, node_type, indent="")`** — recursive, with **three cases** the instructor circled and numbered on screen:
  1. **Leaf** — `type(tree) == int` → return the value.
  2. **MAX node** — start `max_v = MIN`, call `minmax_value(child, "min")` on each child, keep the largest.
  3. **MIN node** — start `min_v = MAX`, call `minmax_value(child, "max")` on each child, keep the smallest.

  *"Everything is kind of symmetric."* The node type is a **parameter** — the tree itself does not know whether a node is MAX or MIN; the caller alternates it on every recursive call.
- **`indent`** exists only to print the call structure. Each recursive call adds two spaces so the printed `CALL` / `returns` lines show the recursion depth.

## The Printed Trace

Running `minmax_decision(Game_tree)` prints the full call tree; the root returns **12**:

```
CALL max [[7, [3, 8, 1], [15, 9]], [12, [17, 13]]]
  CALL min [7, [3, 8, 1], [15, 9]]
    CALL max returns 7
    CALL max [3, 8, 1]        -> returns 8
    CALL max [15, 9]          -> returns 15
    - min [...] returns 7
  CALL min [12, [17, 13]]
    CALL max returns 12
    CALL max [17, 13]         -> returns 17
    - min [...] returns 12
  - max [...] returns 12
```

He annotated it live: the root MAX call makes two MIN calls (one per top-level element, circled blue and red); the first MIN call makes three recursive calls (7, `[3, 8, 1]`, `[15, 9]`). Each `CALL` line is one node visited — exactly the bookkeeping an alpha-beta implementation needs in order to show which nodes were skipped.

## What It Means for HW2 Problem 3

Stated in the notebook header, not on the sheet: *"You can consider modifying it to keep track of the solution path."* The alpha-beta version is this same three-case recursion with α and β threaded through the parameters and an early `return` inside each `for` loop — the [[Alpha-Beta Pruning]] Max-Value / Min-Value procedure literally. The printed trace is also how to *show* that a cut happened: a pruned child never produces a `CALL` line.

## See Also

- [[CSCE 420 Homework 2 — Game Playing, Logic]]
- [[Minimax]]
- [[Alpha-Beta Pruning]]
- [[CSCE 420 Spring 2026 — 02-04 Alpha-Beta Pruning]]
- [[CSCE 420 Homework 1 — Search]]
- [[CSCE 420]]
