---
title: "Batch Normalization"
type: concept
tags: [csce421, batch-normalization, layer-normalization, normalization, regularization, training, exam-final]
sources: [csce421-t09-cnn]
course: CSCE 421
updated: 2026-10-20
---

Batch normalization standardizes the activations entering a layer to zero mean and unit variance across the current minibatch, then lets the network rescale them with two learned parameters. [[CSCE 421]] introduces it in [[CSCE 421 T09 — Convolutional Neural Networks|T09]] with the line *"you want zero-mean unit-variance activations? just make them so."*

> **Exam note:** Ji stated in class on 2026-10-07 that **the final exam will contain a question on batch normalization**, and that it is **not** on the midterm.

## The Problem It Solves

[[Gradient Descent]] applies one learning rate to every weight. T09 states the consequence:

- Same learning rate applied to all weights
- **Large weights dominate updates**
- **Small weights oscillate (or diverge)**

Normalizing the *inputs* fixes this for the first layer only. The insight of batch norm is to ask *"what if we think of this as a new input?"* at every layer — each layer's input is the previous layer's output, so the same argument applies all the way down. T09 frames the goal as **maintaining variance across depth**.

## The Computation

For a minibatch $X$ of shape $N \times D$, compute statistics **per feature, across the batch**:

$$\mu_j = \frac{1}{N}\sum_{i=1}^{N} x_{ij}, \qquad \sigma_j^2 = \frac{1}{N}\sum_{i=1}^{N}(x_{ij}-\mu_j)^2$$

$$\hat{x} = \frac{x - \mu}{\sqrt{\sigma^2 + \epsilon}}$$

The lecture notes this is *"a vanilla differentiable function"* — it backpropagates like any other layer, which is what makes it usable mid-network rather than only as preprocessing.

## The Learnable Scale and Shift

Forcing every layer to zero mean and unit variance is too rigid — a sigmoid or tanh fed strictly unit-variance input is pinned to its linear region. So batch norm adds two learned parameters per feature:

$$y = \gamma\,\hat{x} + \beta$$

T09's framing: *"allow the network to squash the range if it wants to."* The critical observation is on the same slide —

$$\gamma = \sqrt{\sigma^2}, \quad \beta = \mu \quad \Longrightarrow \quad y = x$$

**the network can learn to recover the identity mapping.** Batch norm therefore costs nothing in expressiveness: if normalizing was a bad idea for some layer, that layer can undo it.

## Train vs Test — the part that gets examined

This asymmetry is the most testable fact about batch norm.

| | Statistics used |
|---|---|
| **Training** | $\mu, \sigma$ computed from the **current minibatch** |
| **Test** | a **fixed** $\mu, \sigma$, typically a **running average** collected during training |

T09 is explicit: *"at test time BatchNorm layer functions differently… The mean/std are not computed based on the batch."*

The reason is not efficiency — it is correctness. At test time you may be classifying a **single** example, and there is no batch to take statistics over. Worse, if you did use batch statistics, **a given input's prediction would depend on which other inputs happened to be batched with it**, which is unacceptable for deployment.

## Where It Goes, and the Shapes

> Usually inserted **after** Fully Connected or Convolutional layers, and **before** the nonlinearity.

```
FC -> BN -> tanh -> FC -> BN -> tanh -> ...
```

| Network type | $x$ | $\mu, \sigma$ | $\gamma, \beta$ |
|---|---|---|---|
| Fully connected | $N \times D$ | $1 \times D$ | $1 \times D$ |
| Convolutional | $N \times C \times H \times W$ | $1 \times C \times 1 \times 1$ | $1 \times C \times 1 \times 1$ |

For ConvNets (*"Spatial Batchnorm"*, `BatchNorm2D`) statistics are taken per **channel**, pooled over batch *and* both spatial dimensions — because a convolutional filter is applied identically at every spatial position, so all its outputs belong to the same distribution.

## Benefits

T09's list, verbatim:

- Improves gradient flow through the network
- Allows **higher learning rates**
- Reduces the strong dependence on **initialization**
- *"Acts as a form of regularization in a funny way, and slightly reduces the need for dropout, maybe"*

## Why It Regularizes

The hedged last point is explained by a pattern T09 states twice:

> **Training: add some kind of randomness. Testing: average out randomness.**
>
> Examples: [[Dropout]], **Batch Normalization**, Data Augmentation, DropConnect

Which minibatch an example lands in is random, so its normalized value is random too — the network cannot rely on any exact activation value. That is noise injection, the same mechanism dropout uses. **The train/test asymmetry is not a wart; it is the regularizer.**

## Layer Normalization

The same formula with the statistics taken along the other axis — **per sample, across features** ($\mu,\sigma$ of shape $N \times 1$) rather than per feature across the batch ($1 \times D$). Two consequences T09 states:

> **Same behavior at train and test!** Can be used in recurrent networks.

Because it never looks at other samples, there is no train/test gap and no dependence on batch size. This is why [[Transformers]] use LayerNorm rather than BatchNorm — see [[CSCE 421 T10 — Attention, Transformers, and Large Language Models|T10]], where transformer layers are built as $Z = \mathrm{LayerNorm}[Y(X) + X]$.

## See Also

- [[Convolutional Neural Networks]]
- [[Dropout]]
- [[Regularization]]
- [[Activation Functions]]
- [[Gradient Descent]]
- [[Transformers]]
- [[CSCE 421]]
