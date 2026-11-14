---
title: "Dropout"
type: concept
tags: [csce421, dropout, regularization, ensemble, data-augmentation, early-stopping]
sources: [csce421-t09-cnn]
course: CSCE 421
updated: 2026-10-20
---

Dropout regularizes a network by randomly deleting units during training. [[CSCE 421 T09 — Convolutional Neural Networks|T09]] introduces it alongside early stopping and data augmentation as one instance of a single pattern — **add randomness while training, average it out at test time** — which [[Batch Normalization]] also belongs to.

## The Mechanism

> In each forward pass, **randomly set some neurons to zero**. Probability of dropping is a hyperparameter; **0.5 is common.**

(Srivastava et al., *"Dropout: A simple way to prevent neural networks from overfitting"*, JMLR 2014.)

A fresh random mask is drawn on **every** forward pass, so no two training steps use quite the same network.

## Why Deleting Units Helps

T09 gives two justifications, and they are genuinely different arguments.

**Redundant representation.** *"Forces the network to have a redundant representation; prevents co-adaptation of features."* If a unit might vanish at any moment, no other unit can depend on it being present. A network cannot build a brittle chain where one feature is only meaningful in combination with one specific partner — it has to spread the evidence around.

**Ensemble.** *"Dropout is training a large ensemble of models that share parameters."* Each random mask defines a different sub-network. With $n$ units there are $2^n$ possible masks, and training touches a different one each step. Averaging many models is a classic variance reduction; dropout gets it without training them separately.

## Test Time

The randomness has to go — a deployed model must be deterministic. T09 frames it as wanting to *"average out the randomness"* and *"approximate the integral"*:

$$y = \int p(z)\, f(x, z)\, dz$$

over the mask $z$. Evaluating $2^n$ sub-networks is impossible, so the standard approximation is to use the **full network** with activations scaled by the keep probability, so each unit's expected contribution matches what it was during training.

(Modern implementations do the scaling during *training* instead — "inverted dropout" — so test time is the plain network with nothing to adjust. Same expectation either way.)

## The Pattern It Belongs To

T09 states this twice, on separate slides, which signals the emphasis:

> **Training: add some kind of randomness. Testing: average out randomness (sometimes approximate).**
>
> Examples: **Dropout**, **Batch Normalization**, **Data Augmentation**, DropConnect

This is the most useful thing to carry from the regularization block. Batch norm's train/test asymmetry — minibatch statistics while training, running averages at test — looks like an implementation detail until you see it as the same noise-injection mechanism. [[Batch Normalization]]'s hedged claim that it *"acts as a form of regularization in a funny way"* is explained by this membership.

## The Other Two

**Early stopping.** Train/validation curves diverge; stop where validation accuracy turns over rather than at convergence. The cheapest regularizer there is, and a direct application of [[Model Selection]]'s validation split.

**Data augmentation.** Transform each training image before the loss is computed — horizontal flips, random crops and scales. T09 gives the ResNet recipe: *"pick random L in range [256, 480]; resize training image, short side = L; sample random 224 x 224 patch."* The network never sees the same image twice, which manufactures training data from a fixed dataset.

## Relation to Weight Penalties

[[Regularization]] as introduced in [[CSCE 421 T04 — Overfitting and Regularization|T04]] attacks [[Overfitting]] by **penalizing large weights** — a deterministic term added to the loss. Dropout attacks the same problem by **injecting noise** instead. Both shrink the effective capacity of the model without removing parameters, and they are routinely used together.

## See Also

- [[Regularization]]
- [[Batch Normalization]]
- [[Overfitting]]
- [[Model Selection]]
- [[Convolutional Neural Networks]]
- [[CSCE 421]]
