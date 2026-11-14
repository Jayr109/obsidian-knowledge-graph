---
title: "CSCE 420 Spring 2026 — 03-25 Information Gain, Neural Networks Intro"
type: source
tags: [csce420, lecture-recording, spring-2026, information-gain, decision-trees, learning-curve, overfitting, neural-networks, brain-facts, activation-functions, sigmoid, tanh, threshold, layers, weight-indexing]
sources: []
course: CSCE 420
semester: Spring 2026
date: 2026-03-25
deck: slide06
exam: final
updated: 2026-09-17
---

Spring 2026 lecture, 50 min. Information gain computed on the restaurant data, the remaining decision-tree issues, and the first half of neural networks — brain facts, activation functions, the threshold-absorption trick, architectures, and the weight-index convention. Slides 06:52–78.

## Information Gain, Worked

**Gain = initial entropy − weighted resulting entropy**, where each branch's entropy is weighted by the fraction of examples that went down it. *"The easiest thing is to look at how many samples came this way."*

**Patrons**: initial 1.0. None → 2/12 × 0; Some → 4/12 × 0; Full → 6/12 × Entropy(2+, 4−). For P(+) = 1/3 he read *"about 0.8"* off the entropy curve (exact: 0.918). Resulting ≈ 0.4 (exact 0.459); **gain ≈ 0.6** (exact 0.541). *"You start from high uncertainty, end in low uncertainty, and you can quantify how much information you gained in the middle."*

**Type**: every branch is 50-50, entropy 1.0 each; weights 2/12 + 2/12 + 4/12 + 4/12 = 1 → resulting **1.0**, **gain 0**. *"You went from 1.0 and ended up with the same uncertainty. Type is perhaps the worst attribute to check."*

`ChooseAttribute` = compute gain for every remaining attribute on the **current subset** and take the max. After Patrons, run it on the six Full-branch rows and Hungry wins. See [[Decision Tree Learning]].

## Decision Tree Issues

- The Thai branch tests Fri/Sat — *"maybe there's a happy hour at the Thai restaurant."* Trees can be **wrong on new examples** that resemble nothing in training.
- **Learning curve**: ~10 training samples → ~80% on unseen inputs; ~100 → approaching 99%. Introduces **training / validation / test** sets: adjust the model on training data only, measure on data never used for training.
- **Noise** and **overfitting** to it; **missing attribute values**; **many-valued or continuous attributes** blow up the branching factor.
- **Inductive bias of DTL**: it prefers a short tree, and `ChooseAttribute` is what implements that preference.

## Neural Networks — Brain Facts

Neuroscience *"will not appear on the exam — this is just for fun."* Cortex 1–2 mm thick (~1.6 mm), ~2.5 sq ft flattened; **~100 billion neurons, ~150 trillion connections, ~2,000 per neuron — very sparse.** Energy: **10⁻¹⁶ J per operation vs. 10⁻⁶ J** for a computer — *"10 orders of magnitude worse than the brain."* He looked up current LLM sizes live — hundreds of billions to ~1 trillion parameters — *"so we should be proud of ourselves; we are at least 100-fold better."*

Brain vs. computer: densely connected, massively parallel, entirely nonlinear, **asynchronous — "probably the most different thing; we don't have any central clock"** — fault-tolerant, adaptive. Perception, cognition, motor control are *"nowadays done by deep learning"*; regulation of bodily functions is not.

## Activation Functions

| Function | Output range | At input 0 |
|---|---|---|
| Step (threshold T) | {0, 1} | — |
| Sign | {−1, +1} | — |
| **Sigmoid** 1/(1+e⁻ˣ) | (0, 1) | **0.5** |
| **tanh** | (−1, 1) | **0** |

A steeper multiplier on x makes the sigmoid sharper. Both sigmoid and tanh have derivatives expressible **in terms of themselves** — used next lecture.

**Absorbing the threshold** — derived on the board: step_T(x) = step₀(x − T). Subtract T from both sides of the inequality x > T and you get x − T > 0. *"You don't need to worry about what the threshold is"* — it becomes an ordinary weight on a constant input. See [[Neural Networks]].

### A student asked: where is the threshold in a sigmoid?

*"There isn't one — it's a soft threshold, and it's arbitrary, application-dependent."* His example: a stock model outputs yes = 0.9, no = 0.1 → buy. Another stock: yes = 0.3, no = 0.19. By the rule *yes > no* you'd buy — *"I would be uncomfortable, because the values themselves are too low."* **Treat the output as confidence.** *"The model itself doesn't have any fixed threshold. If you say 'below 0.85, say no,' that's an artificial threshold you're imposing."*

## Architectures

Supervised vs. unsupervised; **feed-forward** (one direction) vs. **recurrent** (loops). He traced several routes from a unit back to itself — direct, via one neighbor, via two — *"you can go around infinitely many hops."* RNNs *"play a very important role in modern deep learning"*; this course mostly does feed-forward.

**Counting layers: do not count the input layer.** *"Input is just static; there's no computation. We only count layers that have computation."* A perceptron is a **one**-layer network; input + hidden + output is **two**.

Single layer → **perceptron learning rule**, step activation. Multi-layer → **backpropagation** (gradient descent), sigmoid/tanh/linear/ReLU.

## Weight-Index Convention

For output unit *i* receiving input *j*, the weight is **W_ij — output index first**. *"We think of this connection weight as belonging to the output side."* The threshold becomes input a₀ = −1 (or 1) with weight W_i0 = T, using the absorption result above. Perceptron activation and learning rule continue 03-27.

## See Also

- [[CSCE 420 Spring 2026 — 03-23 Decision Trees, Entropy]]
- [[CSCE 420 Spring 2026 — 03-30 Perceptron Recap, Gradient Descent, Backprop I]]
- [[Decision Tree Learning]]
- [[Neural Networks]]
- [[CSCE 420]]
