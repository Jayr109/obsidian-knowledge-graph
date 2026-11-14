---
title: "CSCE 420 Spring 2026 — 03-23 Decision Trees, Entropy"
type: source
tags: [csce420, lecture-recording, spring-2026, decision-tree-learning, restaurant-dataset, occams-razor, dtl-algorithm, choose-attribute, entropy, information-theory]
sources: []
course: CSCE 420
semester: Spring 2026
date: 2026-03-23
deck: slide06
exam: final
updated: 2026-09-17
---

Spring 2026 lecture, 50 min. Decision tree learning end to end: the restaurant dataset, why a concise tree, the DTL recursion traced, and entropy defined and computed on the dataset — stopping just before information gain. Slides 06:36–52. Spring's HW4 previewed.

## Framing

*"Machine learning is really good at solving problems, but it doesn't come up with its own problems. Language models do come up with problems, but they're limited by the entire collection of human knowledge. Ask ChatGPT or Claude to come up with something entirely new — the results are not very promising."* Enabling factors: big data from the early-1990s internet, GPGPU/CUDA a decade ago, cloud compute.

## The Restaurant Dataset

Twelve examples, ten attributes — Alternate, Bar, Fri/Sat, Hungry, **Patrons** (none/some/full), Price, Raining, Reservation, Type, WaitEstimate — target **WillWait**. *"Factors that might lead to a decision even in your everyday life."*

### The spouse and nemesis attributes

Thought experiment: add a **Spouse** column whose answer *exactly* matches WillWait. *"Now you don't need any of these other ones. You just ask your spouse: should we wait?"* One node. Then a **Nemesis** column whose answer is always the *opposite* — *"it's very systematic, so you can immediately tell what your answer would be"* — also one node, with the labels flipped. **Both are maximally informative.** An attribute is valuable when it cleanly separates positives from negatives, regardless of direction.

The real tree puts **Patrons** at the root: None → No, Some → Yes, Full → test Hungry. **6 of 12 examples are decided by the first question** — *"how convenient is that."* At most four attributes are ever tested.

## What a Tree Represents

**A disjunction of conjunctions** — one conjunction per root-to-Yes path. He wrote out the four Yes paths (Patrons=Some; Patrons=Full ∧ Hungry ∧ Type=French; …Thai ∧ Fri/Sat; …Burger) and OR-ed them. **The No leaves need no clauses**: plug Patrons=None into every conjunction and each fails, so the whole disjunction is False. Verified for Hungry=No the same way.

## Why Not Memorize?

The trivial tree makes every example a leaf — a depth-10 tree with 12 defined leaves and vast numbers of undefined ones. *"Not able to deal with missing attribute values or new situations. Very incomplete."* And some attributes barely matter.

**Occam's razor**: the most likely hypothesis is the simplest consistent with the observations. His analogy: **heliocentric vs. geocentric** — *"the geocentric system can give you really high precision, but it's not generalizable."* For trees: as few tests as possible; shallow depth. This preference **is** the inductive bias of decision tree learning.

## Choosing the Attribute — Patrons vs. Type, by Hand

Split the 12 into positives {1,3,4,6,8,12} and negatives {2,5,7,9,10,11}, then test each attribute:

- **Patrons**: None → {7, 11}, all negative — *"unanimous vote, No."* Some → {1, 3, 6, 8}, all positive. Full → {4, 12} positive, {2, 5, 9, 10} negative — mixed, needs more tests.
- **Type**: French → 1 yes / 1 no; Italian → split; Thai → 2/2; Burger → 2/2. **Every branch is exactly 50-50.** *"You don't get any answer. You've just reduced your data."*

After Patrons, run the **same procedure on only the six remaining rows** (Full branch) and **Hungry** comes out best — Hungry=No gives an immediate answer.

## The DTL Algorithm, Traced

`DTL(examples, attributes, default)`, recursive:

| Condition | Return |
|---|---|
| examples empty | **default** — *"that's when the default is useful"*; his own: *"I usually don't like to wait"* |
| all examples same class | that class — e.g. DTL on {7, 11} returns No |
| attributes empty | **majority value** — you ran out of tests with mixed examples left |
| otherwise | recurse |

Recursion: `best ← ChooseAttribute(attributes, examples)`; make `best` the root; for each value vᵢ of `best`, call `DTL(examplesᵢ, attributes − best, Majority(examples))` and attach the returned subtree under branch vᵢ. He traced it: Patrons chosen; branch None → DTL({7,11}, 9 attrs, default No) → hits condition 2 → leaf No; branch Some → leaf Yes; branch Full → a genuine subtree because it is undecided. **The default passed down is the parent's majority.**

*"Everything depended on ChooseAttribute. Now the question is how that is computed."*

## Entropy

Poll 10 people: 5–5 is **uncertain**; poll 2 and get 2–0: **certain**. *"You want the entropy to be high when uncertain, low when certain."* For classes yes/no:

**Entropy(E) = − P(yes) log₂ P(yes) − P(no) log₂ P(no)**

- Whole dataset: 6/12 each → −½·log₂½ − ½·log₂½ = ½ + ½ = **1.0** — the maximum.
- A pure branch (4 yes, 0 no): −1·log₂1 − 0·log₂0. *"log₂ 0 is undefined, but it's always multiplied by 0, so we treat that as 0."* Result **0.0**.
- Since P(no) = 1 − P(yes), entropy is a function of P(yes) alone: **0 at both ends, peaking at 1.0 when P(yes) = 0.5.**

**The punchline before information gain**: after splitting on **Type**, every branch still has entropy **1.0** — *"you haven't reduced your entropy."* After **Patrons**, two branches are at 0. *"Here you reduce the entropy quite a bit."* That difference, weighted by branch size, is information gain — next lecture. See [[Decision Tree Learning]].

## See Also

- [[CSCE 420 Spring 2026 — 03-20 Supervised, Unsupervised, RL Issues]]
- [[CSCE 420 Spring 2026 — 03-25 Information Gain, Neural Networks Intro]]
- [[Decision Tree Learning]]
- [[CSCE 420 Lecture 6 — Machine Learning]]
- [[CSCE 420]]
