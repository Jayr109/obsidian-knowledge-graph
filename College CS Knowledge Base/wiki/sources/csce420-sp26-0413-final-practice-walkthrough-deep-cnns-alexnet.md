---
title: "CSCE 420 Spring 2026 — 04-13 Final Practice Walkthrough, Deep CNNs, AlexNet"
type: source
tags: [csce420, lecture-recording, spring-2026, final-exam, practice-exam, exam-format, spiral-dataset, depth, alexnet, imagenet, convolution, kernel, feature-map, channels, max-pooling, stride, top-5-error, receptive-fields, learned-features]
sources: []
course: CSCE 420
semester: Spring 2026
date: 2026-04-13
deck: slide07
exam: final
updated: 2026-09-17
---

Spring 2026 lecture, 50 min, week 14. Opens with a **walkthrough of the final practice exam** and the exam rules, then finishes the "why deeper" spiral demo and covers AlexNet in detail — convolution mechanics, channels, pooling, the two-GPU split, top-1 vs top-5 error, and what the kernels learn. Slides 07:28–45.

> **Final-exam scope, stated here.** *"The final will not be cumulative. None of the questions from the midterm will be included. All of the material published after the midterm exam."* See [[CSCE 420 Final Review]] and [[CSCE 420 Final Exam Practice]].

## Final Practice Exam, Question by Question

| Q | Topic | What he said to know |
|---|---|---|
| 1 | Propositional logic theorem proving | *"basically just the resolution proof"* |
| 2 | Planning | the axioms besides possibility and effect axioms — *"pretty straightforward"* |
| 3 | Bayesian inference | causal vs. **diagnostic** knowledge; which is easier; which is one-to-one vs. one-to-many |
| 4 | Belief-network construction | Cavity, Catch, Toothache added in that order — which arrows are needed? Think **cause vs. effect** and conditional independence |
| 5 | Decision tree learning | draw the partial tree for attribute 1 vs. attribute 2, *"similar to your homework"* |
| 6 | Perceptrons | what each layer can represent: hidden layer = **linear boundaries**; next layer **combines them into nonlinear boundaries** (the vowel example) |
| 7 | Backprop rule | **watch the indices**: k = output, j = hidden, i = input. δ_k = error × derivative. Hidden units have no direct target — *"how is it computed? That's the question."* |
| 8+ | Deep learning | CNN's best application (vision); how deep learning differs from classical ML; **what DQN outputs** (Q-values) — *"the deep-learning questions on the real exam will be more substantial than these"* |

**Format and rules**: same as the midterm — two pages front and back; **one cheat sheet, one sheet, two sides, paper only**. Most problems have **at least two sub-questions**, so partial credit is possible (*"if you don't get one right, you get 5 out of 10, not 0 or 10"*). Some questions require written solutions or explanation — the decision-tree and decision-boundary ones.

## Why Deeper — Spiral Demo Finished

- **No hidden layer**: a single linear boundary; ~50% error on the spiral.
- **One hidden layer, 8 units**: each hidden unit a linear boundary; the combination is *"not too bad"* but misclassifies both ways.
- **Two hidden layers**: second-layer units immediately show **nonlinear** boundaries (*"no longer a straight line, because it's combining three strong units"*); the spiral is solved, and repeatably.
- **Six layers**: very low error; the top layers have *"very complex boundaries."* Odd shapes appear in regions with **no training data** — *"there's no error for input from that region."*

Two lessons: **the learned concept is not what humans see** — it does not extrapolate the spiral outward; and **complexity of boundaries grows with depth**, each layer combining the previous layer's boundaries. See [[Deep Learning]].

## Current Trends (last intro slide)

Deep CNNs → deep RL (DQN on Atari, AlphaGo) → deep RNNs with **LSTM** for language and speech → **attention** → **transformers** → generative AI (LLMs, diffusion for images and video). He added **agents**: systems that run your code, read the errors, optimize, and commit to GitHub — *"becoming a very powerful framework."*

## AlexNet (Krizhevsky, Sutskever, Hinton, 2012)

Three ingredients: the **CNN architecture** (LeNet beefed up with more layers), **GPU** computation, and **ImageNet** data — 1.2 million images, 1,000 classes. Training = feed an image, get 1,000 outputs, compare to the label, backpropagate; repeat 1.2 million times.

### Convolution, worked

Input: **224×224×3** (a student asked what "size" meant — it is the resolution; 3 = RGB planes). First conv layer: **48 feature maps**. Each pixel of a feature map looks at an **11×11×3** sub-region of the input and **every pixel in that map shares the same weights — the kernel**. 48 kernels → 48 response images.

Computing one value: overlay the kernel on the sub-image, multiply **element-wise**, sum. His example: all products zero except 2 × (−4) = **−8**. Then **slide** the window one step and repeat. *"It's just iteration in a for-loop."*

- Student: *"Is the weight shown on the diagram?"* — the kernel **is** the weights; they are learned by backprop; the number on the diagram is the current kernel size.
- **Stride**: skip more than one step per slide.
- **Channels** = the feature maps (48 here).
- **Max pooling**: take the max in each small block to shrink the map (average pooling also exists) — *"all of this can be very computationally intensive."*

**Deeper layers stack channels**: conv-2 has 128 maps, each with a kernel of **5×5×48** — it looks at all 48 previous maps at once; conv-3: 192 maps, kernel **3×3×128**; these weight blocks are **tensors**. Finally a **2048-d vector**, densely connected to another dense layer, then **1,000 outputs**.

**Two-GPU split**: the model was cut into two parallel pathways because each half *"barely fit"* on one GPU; information crosses over only at certain layers and merges at the output. See [[Convolutional Neural Networks]].

## Top-1 vs. Top-5 Error

| Metric | Correct when… | AlexNet |
|---|---|---|
| **Top-1** | the highest output is the true class | 37.5% error |
| **Top-5** | the true class is among the 5 highest outputs | **15.3–17%** error |

*"Pretty bad, right? We're used to 1% or less."* But the best non-CNN entry had **26%** top-5 error — a ~10-point gap. 2013: everyone switched to CNNs (NYU, NUS; Oxford's VGG entered both a CNN and a traditional model and *"witnessed themselves"* the CNN winning). 2014: all top-10 were CNNs; GoogLeNet **6.6%**.

## What the Kernels Learn

Plot each 11×11×3 first-layer kernel as a colour image: **oriented light/dark bars** at different angles and frequencies, plus **red–green and blue–yellow colour-opponent** patterns — exactly the **receptive fields** measured in cat visual cortex. Middle layers: composites of angles, curves, partial circles. Top layers: coherent object parts — honeycomb, a cube-like structure. *"Very similar to what we observe in the biological visual system."*

Top-5 outputs on test images: mite → mite, black widow, cockroach, starfish (*"the categories are similar to the true class"*); leopard → leopard, then jaguar (*"I personally can't tell them apart"*). Top-1 misses that are arguably right: **grille labelled convertible**, **Dalmatian labelled cherry** — *"the humans were probably instructed: what is the most prominent thing in this image?"* A student thought the "jaguar" example was a cheetah.

## See Also

- [[CSCE 420 Spring 2026 — 04-10 NEAT Demos, Deep Learning Intro]]
- [[CSCE 420 Spring 2026 — 04-15 Final Review Posted, CNN Representations, Deep RL, DQN]]
- [[CSCE 420 Final Review]]
- [[Convolutional Neural Networks]]
- [[CSCE 420 Lecture 7 — Deep Learning]]
- [[CSCE 420]]
