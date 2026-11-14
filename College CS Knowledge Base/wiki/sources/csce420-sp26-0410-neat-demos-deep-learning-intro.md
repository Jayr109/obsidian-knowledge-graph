---
title: "CSCE 420 Spring 2026 — 04-10 NEAT Demos, Deep Learning Intro"
type: source
tags: [csce420, lecture-recording, spring-2026, neat, neuroevolution, deep-learning, visual-cortex, hierarchy, function-approximation, sine, hidden-unit-shapes, extrapolation, hyperplane, vowel-classification, representation-learning, history, neocognitron, alexnet, lstm, dqn, spiral]
sources: []
course: CSCE 420
semester: Spring 2026
date: 2026-04-10
deck: slide06, slide07
exam: final
updated: 2026-09-17
---

Spring 2026 lecture, 50 min, end of week 13. NEAT competitive-coevolution demos close the ML deck; then Deck 07 (Deep Learning) opens: the brain's visual hierarchy, what hidden units compute in function approximation, n-dimensional decision boundaries, a vowel-classification example, and the road from rule-based systems to end-to-end deep learning. Slides 06:145–end, 07:1–28.

> Spring's **HW3 solutions** were posted this day, and the HW4 notebook uploaded.

## NEAT — Neuroevolution of Augmenting Topologies

Stanley & Miikkulainen (Ken Stanley was in the same graduate program; later UCF → Uber AI → OpenAI). Unlike fixed-architecture neuroevolution, **neurons and connections can be created and removed**, so evolved networks have different topologies.

**Robot-duel demo** (linked from Resources → *Neuroevolution demos*): 8 inputs = 4 directional food sensors + 4 directional opponent sensors, plus an **energy-difference sensor**, a **boundary sensor**, and a **bias**; 2 outputs = angle and thrust. Moving costs energy, food restores it, and the higher-energy robot wins a collision.

Emergent behaviours he narrated: default topologies (inputs wired straight to outputs) show *"nothing much of any intelligence"*; a **standoff** where nothing moves so nothing changes; a red robot **teasing** yellow into approaching; a robot that **waits and conserves energy** while the other wastes it on food, then wins; the most complex network **cautiously** circling, grabbing the last food, and using the energy edge to finish the fight. *"A lot of these very interesting behaviors can emerge in evolutionary simulation."* End of Deck 06.

## Deep Learning — Motivation From the Brain

Retina → **lateral geniculate nucleus** (mid-brain) → **V1** (back of the head). V1 neurons are tuned to **orientation**, **direction of motion** (won't fire for the same edge moving the other way), and **binocular disparity** (stereo depth). V2 handles **subjective contours** — the Kanizsa triangle, *"no actual edges, but we tend to see a triangle."* Simple features build into complex ones up to anterior inferior temporal cortex, where face-specific neurons live — the **"grandmother cell."**

Thorpe's timing figure: retina ~20–40 ms, V1 40–60 ms, … prefrontal decision, premotor, motor, down the spinal cord — **~200–250 ms** for a whole recognize-and-press cycle. *"Pretty slow."* The hierarchy is the inspiration for **depth**.

## What Hidden Units Compute — Function Approximation

Beyond decision boundaries, networks do **regression**. Learn y = sin x from sampled (x, y) pairs over [−2π, 2π] at step 0.1.

- **1 → 2 hidden → 1** with sigmoid hidden units: each hidden trace is sigmoid-shaped; the sum is *"pretty bad."*
- **1 → 20 → 3 → 1**: the output matches sin *"perfectly."* Second-layer unit traces: one has ups and downs, one is a different bumpy curve, one is **monotonically decreasing** — combined they produce the output.
- Each hidden unit contributes a sigmoid that is **increasing or decreasing** depending on the **sign of its outgoing weight**, and **shifted left or right by its bias weight**.

**Extrapolation fails.** Outside the training range the units still respond, but the output *"would be nothing like the actual sine function"* — it saturates or dies down. *"Outside of your training regime the results would be very inaccurate."*

## Decision Boundaries in n Dimensions

Two inputs → a line. Three inputs (x, y, z) with weights (A, B, C): w · x compared to a threshold is the **equation of a plane**; (A, B, C) is the **surface normal**, and the **bias weight sets the distance from the origin**. Four inputs → a 3-D **hyperplane**, and so on. See [[Neural Networks]].

## Vowel Classification — Combining Boundaries

Dataset: two formant features **F1, F2** extracted from waveforms of confusable words (heed, hid, head, had, hod, hood, who'd, …), 10 classes. Network: 2 → **7 hidden** → 10 outputs. Each hidden unit is a **linear boundary** in the F1–F2 plane; the output unit for *head* connects strongly to the hidden units whose boundaries enclose the *head* region and weakly to the rest. One boundary can serve **several** classes. *"The first layer learns decision-boundary primitives; the second layer learns how to combine them to carve out the region."*

TensorFlow Playground reminder: the 2 → 4 → 2 → 1 network; hover a connection to see its value, **blue = positive, orange = negative**; the first layer is all linear boundaries, the second combines them into something *"bounded."*

## Deep Learning Defined, and Its Place

Complex neural models with **hundreds of millions to billions of parameters**, **hierarchical layer-over-layer representation** — *"that's where 'deep' comes from"* — trained with the **same simple gradient rule**. Enablers: **lots of data** (high-dimensional inputs need many samples — the **curse of dimensionality**) and **GPUs** — NVIDIA *"pivoted very well"* from 3-D games.

| Era | Human designs… | Learned from data |
|---|---|---|
| Rule-based | the whole program | nothing |
| Classic ML | hand-designed **features** | feature → output mapping |
| Representation learning | — | features **and** mapping |
| **Deep learning** | — | **multiple levels** of features, simple → complex, **end-to-end** |

*"Humans got lazy — they didn't want to hand-design these features."* See [[Deep Learning]].

## History, His Gloss

Hinton's deep belief networks (~2006, *"mostly theoretical"*); Andrew Ng and Google Brain's YouTube-cat detector; **Schmidhuber** — superhuman results in competitions, co-inventor of **LSTM**, *"the cutting-edge technology for sequences before transformers"*, and the **vanishing-gradient** problem in deep stacks; **DeepMind 2013 DQN** learning Atari from raw frames → AlphaGo; **ICLR** founded 2013; the 2012 **AlexNet** breakthrough as a beefed-up LeNet. **Fukushima's Neocognitron (1980, *Biological Cybernetics*)**: neurons look at a small **receptive field** rather than the whole previous layer — the direct ancestor of CNNs, five years before backprop arrived. Invariant to scale, rotation, translation. See [[Convolutional Neural Networks]], [[Deep Q-Network]].

## Why Deeper? — Spiral Teaser

Playground's **spiral** dataset: a shallow network can't do much; add layers and *"higher layers combine the boundaries from the previous layer, so it can get much more complex."* Left running at the end; revisited 04-13.

## See Also

- [[CSCE 420 Spring 2026 — 04-08 HW4 Walkthrough, Genetic Algorithms, Neuroevolution]]
- [[CSCE 420 Spring 2026 — 04-13 Final Practice Walkthrough, Deep CNNs, AlexNet]]
- [[Deep Learning]]
- [[Genetic Algorithms]]
- [[CSCE 420 Lecture 7 — Deep Learning]]
- [[CSCE 420]]
