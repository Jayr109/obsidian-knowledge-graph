---
title: "CSCE 420 Spring 2026 — 03-30 Perceptron Recap, Gradient Descent, Backprop I"
type: source
tags: [csce420, lecture-recording, spring-2026, perceptron, linear-separability, tensorflow-playground, gradient-descent, backpropagation, delta-rule, sigmoid-derivative, hidden-layer]
sources: []
course: CSCE 420
semester: Spring 2026
date: 2026-03-30
deck: slide06
exam: final
updated: 2026-09-17
---

Spring 2026 lecture, 50 min. The 03-27 lecture on perceptrons **was not recorded** (*"I'm very sorry"*), so this opens with a recap. Then the TensorFlow Playground demo, gradient descent from first principles, and the backpropagation derivation for output-layer weights, stopping at the hidden-layer problem. Slides 06:78–95.

> **Schedule note.** The Wednesday 04-01 class was cancelled — he was flying to NYU and worried about TSA delays — and replaced by a **pre-recorded lecture**. That recording is the odd **Tuesday 03-31** transcript. See [[CSCE 420 Spring 2026 — 03-31 Backprop II, Recorded Lecture]].

## Perceptron Recap (covering the lost 03-27 lecture)

- The weights set the **slope and intercept** of the decision line; the sign of w₂ decides which side outputs 1. Plug in (a, b) above the line → 1; (c, d) on or below → 0. Procedure: plug in the input, compute the right-hand side b′, compare to the actual b.
- **The bias weight matters**: with w₀ = 0 *"you can only adjust the angle of the decision line"* — it must pass through the origin.
- **Linear separability**: perceptrons learn separable datasets; non-separable ones (XOR) are impossible for a single unit.
- **Perceptron learning rule**: W_ij ← W_ij + α · a_j · err_i, with err_i = t_i − o_i. *"If the input was 0, this weight is not updated regardless of the error. If the error is 0, none of the weights are updated."*

## TensorFlow Playground Demo

The background shading **is** the network's decision rule — look up any pixel to read the output for that input. With no hidden layer the boundary is a line; the diagonal ±/∓ dataset (XOR-like) cannot be separated *"however you try."*

- **Two hidden units**: each contributes a linear boundary; error drops from 0.5 but misclassifies the corners.
- **Eight hidden units**: low error. **Regenerate** resamples from the same distribution — errors move around.
- **The circle dataset needs a minimum of three hidden units**: *"you need to form a closed contour."* Two straight boundaries cannot enclose a region.
- The **spiral** is *"very tough"* — more later.

**History**: Rosenblatt's perceptron rule; **Minsky and Papert** proved single-layer networks are limited; *"it had to wait 15–20 years before an algorithm was developed to train all of these weights, not just the top layer."* That algorithm is **backpropagation = gradient descent.**

## Why Hidden Weights Are the Problem

The perceptron rule works for output weights W_ij because the **target t_i is known** — you can compute err_i. For a hidden weight W_jk, *"what should be the target value for that hidden unit? There's nothing that tells you. This is precisely what was not known."*

## Gradient Descent, From One Weight

Total error E is a function of the weights — the dataset is fixed, so *"the only thing you can change to reduce the error is the connections."* With one weight, plot E(w). At w₀ the slope is positive → move **left** (negative direction); at w₁ the slope is negative → move right. So the direction is **−1 × dE/dw**, and the **magnitude is |dE/dw|**. *"As you approach the minimum, your step size becomes smaller and smaller — the slope converges to zero."*

Multiple weights: ΔW_n = −α ∂E/∂W_n, a vector of partials. See [[Gradient Descent]].

## Backprop for Output Weights — Derived

**Indices**: output *i*, hidden *j*, input *k*. Error for one sample: **E = ½ Σᵢ (tᵢ − oᵢ)²**, with oᵢ = g(Σⱼ W_ij aⱼ). (Optionally also sum over the N samples — *"cumbersome; you can adjust later."*)

**∂E/∂W_ij**, step by step:
1. **Drop the sum over other output units.** A student asked why. Because o₁, o₂, … other than oᵢ *"do not include W_ij anywhere in their computation"* — their partials with respect to W_ij are zero.
2. Chain rule on the square: ½ · 2 · (tᵢ − oᵢ) · ∂(tᵢ − oᵢ)/∂W_ij; the 2 and ½ cancel. tᵢ is a constant → its derivative is 0.
3. ∂oᵢ/∂W_ij = g′(inᵢ) · ∂(Σⱼ W_ij aⱼ)/∂W_ij, and *"the only term that includes W_ij is W_ij aⱼ — all the others become zero"* → **aⱼ**.

**Result: ∂E/∂W_ij = −(tᵢ − oᵢ) · g′(inᵢ) · aⱼ.**

*"How is this different from the perceptron rule? The only thing that changed is this derivative."* Error × input, times g′.

**Define δᵢ = errᵢ · g′(inᵢ)** — everything on the output side of the connection. *"This will become a very important value later on."* Then **ΔW_ij = α · aⱼ · δᵢ**.

**Sigmoid shortcut**: g′(x) = g(x)(1 − g(x)), so g′(inᵢ) = **oᵢ(1 − oᵢ)** — *"you don't have to do extra computation."* A similar identity exists for tanh.

## The Hidden-Layer Setup

For W_jk, expand aⱼ = g(Σₖ W_jk aₖ) inside oᵢ = g(Σⱼ W_ij aⱼ) — *"nested sigmoid functions, very difficult to derive directly."* Two of the three factors are known (g′ at the hidden unit, and the input aₖ); the missing piece is the hidden unit's error term, which the recorded lecture derives. See [[Neural Networks]].

## See Also

- [[CSCE 420 Spring 2026 — 03-25 Information Gain, Neural Networks Intro]]
- [[CSCE 420 Spring 2026 — 03-31 Backprop II, Recorded Lecture]]
- [[Neural Networks]]
- [[Gradient Descent]]
- [[CSCE 420]]
