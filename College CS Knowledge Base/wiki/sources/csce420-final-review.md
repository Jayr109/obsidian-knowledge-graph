---
title: "CSCE 420 Final Review"
type: source
tags: [csce420, exam, final, review, scope, study-guide]
sources: []
course: CSCE 420
exam: final
semesters: [Spring 2026]
updated: 2026-09-17
---

The instructor's **final-exam scope**, from his Spring 2026 review sessions on 04-13 and 04-15. The Canvas "Final Exam Review" page itself was not captured on video — he said *"you can just read through these, I won't go through each and every one"* — so this page records what he *said*, which is the higher-value half anyway.

> **This page is for the FINAL only.** Midterm scope lives on [[CSCE 420 Midterm Review]]. The two do not overlap: the final is **not cumulative**.

## Exam Logistics (Spring 2026, as stated)

- **University-designated final exam slot**: Tuesday May 5, 10:30–12:30. (Fall 2026's slot will differ — check your own schedule.)
- **Weight**: 30% of the grade.
- **Cheat sheet**: *"one page, so one sheet, two sides, just the paper."*
- **Practice exam** under Canvas Quick Links → Practice Exam → *final exam sample*. Already ingested: [[CSCE 420 Final Exam Practice]].
- The Final Exam Review page is under Canvas → Exams → *final exam review*.

## The Non-Cumulative Rule — Stated Three Times

- **02-27**: *"The final exam, well this is way ahead, but it'll not be cumulative. So everything after this will be on the final exam."*
- **04-13**: *"The final will not be cumulative. None of the questions from the midterm will be included in the final exam. And all of the materials that have been published after the midterm…"*
- The dividing line is the midterm's endpoint in the logic deck: **unification**. Everything from FOL resolution onward is final material.

## Scope at a Glance

| Deck | On the final? | What he said |
|---|---|---|
| slide03 Logic (post-unification) | **Yes — one question** | *"There'll be one question on … theorem proving"* — see note below |
| slide04 Planning | Yes | *"Some questions on planning"* |
| slide05 Uncertainty & Probability | Yes | *"Uncertainty and probability"* |
| slide06 Machine Learning | Yes, **minus SOM** | *"Self-organizing maps will not be on the exam"* |
| slide07 Deep Learning | Yes | Listed without exclusions |
| slide08 AI Ethics | **No** | *"AI ethics would also not be on the exam"* |
| slide01–02, slide03 through unification | **No** | Midterm material; not cumulative |

### Note on the logic question

The transcript reads: *"There'll be one question on post-todal theorem… propositional logic theorem proving."* The first phrase is a caption garble. Two readings:

- Taken literally, a **propositional** theorem-proving question — which would contradict "not cumulative," since propositional resolution was the *main part* of the midterm.
- More consistent with everything else he said: the **first-order** theorem-proving material that was explicitly *excluded* from the midterm (resolution with unification, factors and resolvents) — i.e. the post-midterm half of the logic deck.

**Prepare for the second reading, and be able to do the first.** Practically that means: run a resolution proof that requires [[Unification]] to resolve clauses — [[Resolvents and Factors]] — not just a propositional one. That skill subsumes the propositional case.

## Spoken Hints

1. **SOM is out.** *"One important thing is that self-organizing maps will not be on the exam — from the machine learning slides."* This is the one explicit exclusion inside an included deck. [[Self-Organizing Map]] can be skipped for the final; note the [[CSCE 420 Final Exam Practice]] page does have a SOM problem, so the practice exam is *wider* than the real one here.
2. **Ethics is out.** The whole of slide08.
3. **Read the review page yourself.** He did not walk it line by line as he did for the midterm. If you can get the Canvas page for your semester, capture it — it will have the same bold-verb objectives format as the midterm page.
4. **Homework 4** was due the Tuesday of the week after the review (Spring). The last homework covers the DL material, so its questions are the best guide to the DL portion of the exam.

## What the Final Deck Emphasized in the Sessions Themselves

The 04-13 and 04-15 lectures continued into CNNs and deep reinforcement learning after the review, and the material he chose to dwell on is a reasonable signal:

- **CNN internal representations** — the 4096-d hidden vector, nearest-neighbour retrieval on ImageNet, and the two-colour-dog example showing CNNs learn *superficial pixel patterns*, not human-like concepts.
- **t-SNE visualization** of ImageNet (Karpathy) — dimensionality reduction to see the data distribution; clusters by appearance, not function.
- **The ILSVRC arc**: AlexNet 2012 (8 layers, top-5 error collapse) → VGG (same architecture, more layers) → ResNet (152 layers, skip connections) → GoogLeNet (bottleneck) → DenseNet. Lesson: depth first, then *architecture*. Top-1 vs top-5 accuracy.
- **CNNs beyond vision** — spectrograms for speech — and their displacement by transformers (vision transformers).
- **Deep RL**: Q-function Q(s,a) as long-term value of an action in a state; value vs. policy function; model-free vs. model-based (learn δ(s,a) and R(s,a) or not); DQN structure — stacked frames → conv layers → FC → one output per joystick action; the training problem that the true Q target is unknown, solved by bootstrapping from rewards. See [[Deep Q-Network]] and [[Reinforcement Learning]].

## Post-Midterm KB Pages (the final's universe)

[[CSCE 420 Lecture 3 — Logic and Automated Theorem Proving]] (from [[Resolvents and Factors]] on: [[Resolution Strategies]], [[Answer Extraction]], [[Prolog]]) · [[CSCE 420 Lecture 4 — Planning]] · [[CSCE 420 Lecture 5 — Uncertainty and Probabilistic Reasoning]] · [[CSCE 420 Lecture 6 — Machine Learning]] · [[CSCE 420 Lecture 7 — Deep Learning]]

Excluded even though ingested: [[Self-Organizing Map]], [[CSCE 420 Lecture 8 — AI Ethics]].

## See Also

- [[CSCE 420 Midterm Review]]
- [[CSCE 420 Final Exam Practice]]
- [[CSCE 420]]
