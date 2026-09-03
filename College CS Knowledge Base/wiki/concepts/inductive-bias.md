---
title: "Inductive Bias"
type: concept
tags: [csce420, inductive-bias, ockhams-razor, model-selection, overfitting]
sources: [csce420-lecture-06-machine-learning]
course: CSCE 420
updated: 2026-09-01
---

Given the same training data, many hypotheses fit it. **The selection of one hypothesis (model) over another is called an inductive bias.**

## The Setup

The deck shows one set of data points (a) and three different curves (b), (c), (d) all passing through or near them. Each is consistent with the evidence; nothing in the data alone chooses among them. Candidate biases:

- **Exact match to training data**
- **Prefer an imprecise but smooth approximation**

Neither is "correct" — they are different prior commitments about what kind of function the world is likely to contain.

## Why Some Bias Is Unavoidable

Without a bias, learning cannot generalize at all: infinitely many functions agree with any finite sample and disagree everywhere else. A learner that refuses to prefer among them has learned nothing about novel input. **The bias is not a defect to be removed but the mechanism that makes generalization possible.**

## Ockham's Razor

The specific bias the deck endorses for [[Decision Tree Learning]]:

> **The most likely hypothesis is the simplest one that is consistent with all observations.**

Preferring short trees to tall ones. In decision-tree terms: make as **few tests as possible** before reaching a decision, so the tree stays shallow.

This is implemented, not merely stated — the `CHOOSE-ATTRIBUTE` function using [[Entropy and Information Gain|information gain]] is what operationalizes the preference for short trees. The deck asks precisely this as a review question: *how does Choose-Attribute contribute to the inductive bias?*

## See Also

- [[Decision Tree Learning]]
- [[Entropy and Information Gain]]
- [[Supervised Learning Issues]]
- [[Machine Learning Paradigms]]
- [[CSCE 420]]
