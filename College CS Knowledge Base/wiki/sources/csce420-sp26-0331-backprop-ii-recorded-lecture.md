---
title: "CSCE 420 Spring 2026 — 03-31 Backprop II, Recorded Lecture"
type: source
tags: [csce420, lecture-recording, spring-2026, backpropagation, hidden-layer-delta, delta-rule, batch-vs-online, train-validation-test, local-minima, momentum, nettalk, lenet, cnn, alvinn, autoencoder]
sources: []
course: CSCE 420
semester: Spring 2026
date: 2026-03-31
deck: slide06
exam: final
updated: 2026-09-17
---

Spring 2026, **pre-recorded 50-min lecture** posted in place of the cancelled Wednesday 04-01 class (the file is stamped Tuesday 03-31). Completes the backpropagation derivation — the hidden-unit delta — then the algorithm, training issues, four historical applications, and autoencoders. Slides 06:95–115. No students present, so no Q&A.

## Recap: Output-Weight Update

For W_ij (output i, hidden j) the update needs two things: **a_j** on the input side and **δ_i** on the output side, where δ_i = err_i · g′(in_i) and err_i = t_i − o_i comes straight from the dataset's target column.

## The Hidden-Unit Delta — Derived

For W_jk (hidden j, input k): a_k is known, g′(in_j) is computable, but **there is no target for a hidden unit** — *"we don't have something directly computable from the dataset."* Expanding o_i = g(Σ_j W_ij · g(Σ_k W_jk a_k)) gives nested sigmoids, *"very difficult to reduce directly."*

**Trick**: chain through a_j as the intermediate variable: ∂E/∂W_jk = (∂E/∂a_j)(∂a_j/∂W_jk).

- **Easy factor** ∂a_j/∂W_jk: let f = Σ_k W_jk a_k; then ∂a_j/∂W_jk = g′(f) · a_k — *"the only term that survives is the one that contains W_jk."*
- **Hard factor** ∂E/∂a_j — stated, not derived (*"a little bit beyond the scope of this course"*): **err_j = Σ_i δ_i W_ij**. Multiply each output delta by the weight connecting j to it, and sum. *"You have some hint of what kind of error this neuron is contributing to."*

**Define δ_j = err_j · g′(in_j)**, exactly parallel to δ_i. Then **ΔW_jk = α · δ_j · a_k**. (He briefly wrote a stray minus sign, then removed it: the minus from −∂E/∂W and the minus inside the error cancel.)

*"The deltas get propagated backwards through the connection weights — that's why it's called backpropagation."*

**Generalizes to any depth.** With layers indexed i, j, k, l, m top-down, updating W_kl needs only **a_l** (the input side) and **δ_k**, which is built from the δ's **one level up**. *"All of the values to update this connection are available right here at the input side and one level up."* See [[Backpropagation]].

## The Algorithm

1. Pick an (input, target) pair from the dataset.
2. Feed forward: activate hidden layer(s), then output.
3. At the output, compute err_i = t_i − o_i, then δ_i.
4. Update the output-layer weights.
5. Move down one layer: backpropagate the δ's through the weights to get err_j, multiply by g′ to get δ_j, multiply by the input to update. Repeat until the input layer is reached.
6. Next sample; repeat.

## Training Issues

**Batch vs. online.** *Online*: apply ΔW immediately after each sample. *Batch*: compute ΔW for every sample, accumulate, apply once — optionally normalizing by 1/N. (He labelled them backwards on the board, then corrected: *"big mix-up."*)

**Train / validation / test.** Training and validation are **both used during training**: the training set directly updates the weights; the validation set checks accuracy on data *"not used in updating the weights"* — *"it's important that it's just used for checking accuracy."* The test set is held out entirely. *"There's a fine difference between these three sets, but you need to be aware of the main differences."*

**Slowness**: near a minimum the slope is shallow, so steps shrink toward zero — *"very, very, very slow."*

**Local minima**: from w₀ the descent settles where ∂E/∂w ≈ 0 and *"you can't actually go over here to reach the global minimum."*

**Momentum**: add a fraction of the **previous** step: ΔW_ij(t) = α δ_i a_j + β · ΔW_ij(t−1). *"If you have been moving very fast in the previous steps, it'll give you enough movement to go over this bump."* Also speeds convergence.

## Applications — Pre-2012

| System | Year | Architecture | Task |
|---|---|---|---|
| **NETtalk** (Sejnowski & Rosenberg) | 1986–87 | feed-forward, 7-letter sliding window | phoneme for the **middle letter** — resolves the s/z sound from local context |
| **LeNet** (LeCun) | ~1989–98 | conv layers → fully-connected → 10 outputs | handwritten digits; kernels slide across the image to build **feature maps** |
| **ALVINN** (CMU NavLab) | late 1980s | camera + rangefinder → hidden → **45 steering outputs** | highway driving for tens of miles |

He showed LeNet's demo via the Wayback Machine: invariance to scale, tilt, translation, aspect ratio, stroke thickness, noise, *"very creative"* styles. *"If you hear anyone say gradient-based learning, it's just a descendant of backpropagation."* 2012 = *"year zero of the deep-learning revolution."* See [[Convolutional Neural Networks]].

## Autoencoders

Copy the input column into the target column and train — the network learns to reproduce its input. Technically **self-supervised**: *"the task itself becomes a supervised learning task, although the target is just the same as the input."*

**Compression**: a 10×10 image → 100 inputs → **3 hidden units** → 100 outputs. Anything that reproduces the training images through that bottleneck has reduced each image to 3 real numbers; the decoder weights expand it back. Continues 04-06 with "embeddings." See [[Autoencoders]].

## See Also

- [[CSCE 420 Spring 2026 — 03-30 Perceptron Recap, Gradient Descent, Backprop I]]
- [[CSCE 420 Spring 2026 — 04-06 Demos, Autoencoders, SRN, Genetic Algorithms]]
- [[Backpropagation]]
- [[Neural Networks]]
- [[CSCE 420]]
