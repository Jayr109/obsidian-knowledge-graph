---
title: "Machine Learning"
type: concept
tags: [csce420, machine-learning, generalization, data-deluge]
sources: [csce420-lecture-06-machine-learning]
course: CSCE 420
updated: 2026-09-01
---

**Machine learning is improving performance in a task through experience** — spanning rote memory at one end to learning complex strategy at the other. The lecture dates its rise bluntly: it **has become a dominant force in AI since the mid 1990s**.

For the three-way paradigm split, see [[Machine Learning Paradigms]]; this page covers the deck's framing of *why* and *what it costs*.

## Four Advantages

1. **Fault tolerance**
2. **No need for a complete specification to begin with**
3. **Learning from data**
4. **Superhuman performance in some cases**

The second is the deep one. [[Symbolic AI]] required someone to write down the rules in advance; the [[Frame Problem]] showed how badly that scales. Learning sidesteps the specification burden entirely.

## Why Now: The Data Deluge

- Scientific instruments and data-acquisition devices
- The internet and the web
- **All sectors of society producing and digitizing data** — including your phone

And the complementary shortage: **not enough human expertise or human power** to make sense of it.

## Milestones Cited

| Year | Event |
|---|---|
| 2011 | IBM Watson beats human Jeopardy champions |
| 2012 | Google's artificial brain learns to find cat videos on YouTube |
| 2015– | DeepMind: Atari 2600, AlphaGo, AlphaStar |
| 2018 | **ACM Turing Award** to deep learning pioneers |
| 2022– | OpenAI: ChatGPT |

See [[Game AI Milestones]] for the game-playing thread in detail.

## What It Takes

The deck is explicit that this is a mathematical subject: **linear algebra, calculus, probability and statistics, differential geometry, numerical methods.**

## High-Dimensional Data

A $50 \times 50$ image is a **2,500-dimensional vector** — one *point* in 2,500-dimensional space. Real data is typically 10,000, a million, or more dimensions. This reframing of an image as a point is what makes geometric methods applicable, and it is why the [[Curse of Dimensionality]] bites so hard.

## The Closing Caution

> **ML is good at solving problems, but not at posing problems** (Choe and Mann, 2012).

A pointed limitation from the instructor's own work: the problem formulation still comes from humans.

## See Also

- [[Machine Learning Paradigms]]
- [[Supervised Learning Issues]]
- [[Unsupervised Learning]]
- [[Curse of Dimensionality]]
- [[Deep Learning]]
- [[CSCE 420]]
