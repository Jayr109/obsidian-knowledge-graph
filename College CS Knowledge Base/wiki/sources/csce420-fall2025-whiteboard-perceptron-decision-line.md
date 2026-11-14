---
title: "CSCE 420 Fall 2025 — Whiteboard: Perceptron Decision Line"
type: source
tags: [csce420, recording, video, whiteboard, perceptron, decision-boundary, xor, linear-separability, fall-2025]
sources: []
course: CSCE 420
semester: Fall 2025
date: 2025-11-10
exam: final
updated: 2026-09-17
---

A 14-minute whiteboard recording from the **Fall 2025** offering, dated 11/10/2025 on the screen clock (the export named the file `dubbed.mp4`; archived as `raw/CSCE420_Fall2025_Whiteboard_Perceptron_2025-11-10.mp4`). It is the derivation the Spring 2026 recap on 03-30 assumes — turning a perceptron's threshold rule into the equation of a line and reading the output off the plot. Transcribed with faster-whisper large-v3; the board was verified frame by frame.

> **Why it exists.** It appears to have been recorded to replace a lost or unclear in-class derivation — it opens with *"Is that visible? It's not very visible. This is a problem"* and zooming the camera. Deck 06 material; final-exam scope.

## Setup on the Board

Perceptron with **bias input −1** and weight **w₀**, inputs **x₁, x₂** with weights **w₁, w₂**, one output. Recap: with w₁ = w₂ = 1 and a suitable w₀ it implements **AND**; slight changes give **OR** and **NOT** (NOT has one input plus the bias). *"With these three perceptron unit types you can implement your modern-day computer."*

**Two questions posed** (answered later in the deck):
1. Can a single unit implement **any** logical function — e.g. XOR or equivalence? He wrote the XOR truth table (0 0→0, 0 1→1, 1 0→1, 1 1→0): *"It seems that you may be able to learn it… but we will see that these cannot be represented using a single perceptron."*
2. Here the weights were **assigned by hand**. *"How do you learn these weights?"*

## The Derivation — Decision Rule to Line

**Decision rule**: (−1)·w₀ + x₁w₁ + x₂w₂ **> 0 → output 1**; **≤ 0 → output 0**.

Rearranging the boundary w₁x₁ + w₂x₂ − w₀ = 0, step by numbered step as on the board:

| Step | Manipulation | Result |
|---|---|---|
| ① | start | w₁x₁ + w₂x₂ − w₀ > 0 |
| ② | subtract w₁x₁ from both sides | w₂x₂ − w₀ > −w₁x₁ |
| ③ | add w₀ | w₂x₂ > −w₁x₁ + w₀ |
| ④ | divide by w₂ (**assuming w₂ > 0**) | **x₂ > −(w₁/w₂)·x₁ + w₀/w₂** |

*"Here's the tricky part"*: dividing by w₂ **flips the inequality if w₂ < 0**. He assumed w₂ > 0 and noted the flip.

Treat x₁ as x and x₂ as y: without the inequality this is **y = mx + b** with **slope −w₁/w₂** and **y-intercept w₀/w₂**. Draw that line on the x₁–x₂ plane. See [[Perceptron]].

## Reading the Output From the Plot

Given trained weights and a new input **(a, b)**: plug **a** into the line function to get **a′** (the line's height at x₁ = a). The decision is simply **compare b with a′**:

- **b > a′** (the point lies **above** the line) → output **1**.
- A second input **(c, d)** below the line: d ≤ d′ → output **0**.

*"Any input point that happens on or below that line would give you the output of 0, and anything above would give you 1."* (Sides swap when w₂ < 0.) This is the geometric fact behind **linear separability**: one unit = one line = one half-plane, so XOR's diagonal classes cannot be separated — [[Neural Networks]] covers the fix (a hidden layer).

## See Also

- [[Perceptron]]
- [[Neural Networks]]
- [[CSCE 420 Spring 2026 — 03-30 Perceptron Recap, Gradient Descent, Backprop I]]
- [[CSCE 420 Lecture 6 — Machine Learning]]
- [[CSCE 420]]
