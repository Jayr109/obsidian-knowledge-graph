---
title: "CSCE 420 Spring 2026 — 04-08 HW4 Walkthrough, Genetic Algorithms, Neuroevolution"
type: source
tags: [csce420, lecture-recording, spring-2026, hw4, information-gain-code, scikit-learn, decision-tree, perceptron-code, gradient-descent-code, xor-three-units, cnn-colab, genetic-algorithms, fitness-function, diversity, crossover, neuroevolution, sane, mario]
sources: []
course: CSCE 420
semester: Spring 2026
date: 2026-04-08
deck: slide06
exam: final
updated: 2026-11-04
---

Spring 2026 lecture, 50 min. The first 30 minutes walk through **Spring's HW4** (belief networks + machine learning + a Colab CNN); the rest finishes genetic algorithms — design issues, GA-evolved network weights, SANE — and starts the MarI/O neuroevolution video. Slides 06:135–145.

> **HW4 here is Spring 2026's, and its problem numbers do not match Fall's.** The user's own sheet is [[CSCE 420 Homework 4 — Probability, Learning, Deep Learning]], which drops the scikit-learn and gradient-descent programming problems described below.

## HW4 — Written Problems

| # | Topic | Ask |
|---|---|---|
| 1–3 | Belief networks | build a small network; give an example of **intercausal** inference; order the nodes {wildfire, smoking, lightning, …} for a good network |
| 4 | Decision trees | 14 examples, **6 yes / 8 no** (not 50-50); every attribute binary → two branches. Draw the root subtree using B, C, or E as the first test |
| 5 | Information gain | initial entropy, weighted resulting entropy, subtract; which attribute to test first |
| 9 | Perceptrons | can XOR be built from **three** perceptron units? *"It's very important to understand how to count the perceptron units"* — input nodes don't count; 2 hidden + 1 output = 3, so only two layouts are possible. Playground's diagonal dataset is essentially ¬XOR |
| 10 | Gradient descent | a degree-4 error function of one weight; find dE/dW |

## HW4 — Code (`ml.ipynb`, sections navigable via the notebook outline)

- **`my_log`**: must return **0 when the argument is 0** instead of raising — *"we must take care of the val = 0 case."*
- **`entropy(pos, neg)`**: (10, 10) → 1.0; (0, 20) or (20, 0) → 0.
- **`info_gain(before, after)`**: before = `[6, 6]`; after = list of per-branch `[pos, neg]`, e.g. `[[0,2],[4,0],[2,4]]` for a 3-way split. *"This is how you pass the resulting split."*
- **scikit-learn `DecisionTreeClassifier`**: X = list of rows, Y = targets, `clf.fit(X, Y)`. Reading the plot: `X0` is the **first** attribute; `X0 <= 0.5` means attribute = 0 (left branch), else 1; `value = [3, 1]` means **3 samples of class 0, 1 of class 1**. On his dataset the root tested attribute 1 and then attribute 4 (`X3`). You must paste in the homework's own table and interpret the tree the same way.
- **Perceptron**: 4 samples, targets 0111 (OR); **bias input −1.0**; stop when error < 0.01. Implement: activate output, compute error, adjust weights. `plot_decision_boundary` shades the input plane like TensorFlow Playground (yellow = 1, purple = 0). His demo boundary looked flipped — *"maybe this is actually reversed, I'm not exactly sure."*
- **Gradient descent**: replace the quadratic `E(w)` with the homework's degree-4 polynomial and rewrite `dE(w)` from your written answer. Behaviour by α, from w₀ = 4: **0.001** stalls after 100 iterations; **0.1** reaches the minimum; **0.9** *"jumps to the other side of the curve"* but still converges.
- **Deep learning (Colab)** — *the only part where ChatGPT/generative AI is allowed*: have it generate a **LeNet variant** for MNIST (e.g. two conv layers, 5×5 receptive field, 25 channels), then generate analysis code to show kernel shapes and the 25 feature-map activations.

## Genetic Algorithms — Design Issues

*"The genome is the collection of all the chromosomes — earlier papers just said chromosomes."* GAs resemble hill climbing (good random solutions propagate), parallelize naturally, and handle **delayed reward** — *"a very good approach for reinforcement learning in general."*

**The fitness function is the most important decision.** *"Genetic algorithms are very good at exploiting any hole in your thinking… just like a genie."* His genie story: wish to be rich with a beautiful spouse → wake up a drug lord in a mansion with gunfire outside. GAs will also exploit **bugs in your code** to score high.

Other issues: representation; **selection** (pure ranking vs. a diversity rule); reproduction. **Diversity collapse** is the big one — *"the good ones tend to become very similar, the gene pool decreases, and in the end they won't be able to reach a higher fitness."* Crossover strategy: where to cut, one cut or many, two parents or three. Theory: Holland's book, but *"not too much theoretical understanding about why it works so well."* Landscape crevices ≈ hill-climbing spikes. Open questions: combining learning with evolution; **culture** is not encoded in genes yet drives civilization.

## GA on Neural-Network Weights

Encode all weights of a network as one genome. Red parent + green parent → offspring with red weights on one part, green on the rest. Evaluate → select high performers → mate → back into the pool.

### Student questions

- *"Does each chromosome map to one node or one network?"* — **One whole network.** Worked example: a light-seeking robot with 2 light inputs, 2 hidden, 2 wheel outputs → **8 weights (W₁…W₈)** = one genome. If the network does well, the entire genome is kept.
- *"Where do you cut?"* — Partial solutions combine: W₁, W₂ from parent 1 = the left-light-sensor **module**; the rest from parent 2. *"It makes sense to cut there, but we don't care about that — you could cut in the middle of the module. That whole thing is random."*

**SANE** (Moriarty & Miikkulainen — *"my advisor, Risto Miikkulainen"*): chromosomes encode **individual neurons** that compete and are assembled into networks; a neuron's fitness is credited from the networks it joined. One of the first successful **neuroevolution** methods. See [[Genetic Algorithms]].

## MarI/O Video (SethBling)

A network evolved for 24 hours plays *Super Mario World* Donut Plains 1 with no prior knowledge — *"it didn't even know that pressing right would make the player go toward the end of the level."* Inputs = simplified tile grid (white = standable, black = moving objects); outputs = the 8 controller buttons; hidden neurons *"popped up"* during evolution; one fixed-value input is the bias. Generation 0 mostly stands still. Continues 04-10 with NEAT.

## See Also

- [[CSCE 420 Spring 2026 — 04-06 Demos, Autoencoders, SRN, Genetic Algorithms]]
- [[CSCE 420 Spring 2026 — 04-10 NEAT Demos, Deep Learning Intro]]
- [[Genetic Algorithms]]
- [[Perceptron]]
- [[CSCE 420 Lecture 6 — Machine Learning]]
- [[CSCE 420]]
