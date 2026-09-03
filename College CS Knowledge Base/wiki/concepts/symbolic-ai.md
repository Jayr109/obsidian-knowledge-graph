---
title: "Symbolic AI"
type: concept
tags: [csce420, symbolic-ai, logic, expert-systems, knowledge-representation]
sources: [csce420-lecture-01-introduction]
course: CSCE 420
updated: 2026-08-25
---

Symbolic AI is the paradigm that dominated the field from the 1950s to the mid-1980s: represent knowledge as logical sentences over discrete symbols, and get intelligent behavior by applying inference rules to them. It is the tradition that produced theorem proving, expert systems, Prolog, and — in this course — everything in the [[Logical Inference]] and [[First-Order Logic]] material.

## Characterization

Lecture 1's summary slide lists three points:

- Symbolic logic, rule-based
- Theorem proving, expert systems
- **Issue: cannot deal with vague concepts; cannot learn from data**

Those two failures are precisely what the machine-learning era was built to fix, and they are why the [[History of AI]] pivots after the mid-80s.

## Worked Example From the Slide

The slide illustrates symbolic reasoning with a small train problem:

1. Train late (T) & no taxi at station (¬X) → John will be late for the meeting (L).
2. Train was late (T).
3. John was not late for the meeting (¬L).
4. **[Question]** Was there any taxi at the station?

Clause form on the right of the slide:

| # | Sentence | Clause |
|---|----------|--------|
| 1 | T ∧ ¬X → L | ¬T ∨ X ∨ L |
| 2 | T | T |
| 3 | ¬L | ¬L |
| 4 | conclusion | X |

Resolving 1 with 2 gives X ∨ L; resolving that with 3 gives X. So yes, there was a taxi. This is a preview of [[Resolution]] — the whole first-half logic unit is the machinery for doing this reliably.

## Why It Faded

The two stated issues compound. Vague concepts ("is this a cat?") have no clean symbolic definition, and hand-authoring rules does not scale — every new domain needs a new knowledge engineer. Machine learning inverted the pipeline: instead of encoding what you know, collect examples and let the system extract the regularity. See [[Machine Learning Paradigms]].

## Return

Symbolic AI is not dead in the course's telling. The "Future of AI" slide puts **combining symbolic AI and deep learning** first among directions, under the name [[Neurosymbolic AI]] — the bet being that deep nets supply the perception and grounding that symbols lacked, while symbols supply the reasoning and compositionality deep nets lack.

## See Also

- [[Logical Inference]]
- [[Resolution]]
- [[First-Order Logic]]
- [[Neurosymbolic AI]]
- [[History of AI]]
