---
title: "CNN Architectures"
type: concept
tags: [csce421, cnn, lenet, alexnet, vggnet, googlenet, resnet, inception, residual, imagenet]
sources: [csce421-t09-cnn]
course: CSCE 421
updated: 2026-10-20
---

The ImageNet-era architectures, as [[CSCE 421 T09 — Convolutional Neural Networks|T09]] presents them. The deck repeats one chart four separate times — the **ILSVRC winners** by depth — because that progression *is* the argument:

```
shallow  ->  8 layers  ->  8 layers  ->  19 layers  ->  22 layers  ->  152 layers
             AlexNet       ZFNet        VGG           GoogLeNet      ResNet
```

Each architecture is best understood as the answer to a problem the previous one exposed.

## LeNet-5 (LeCun et al., 1998)

> Conv filters were **5x5, applied at stride 1**. Subsampling (pooling) layers were **2x2 applied at stride 2**.

The template — alternating conv and pooling, then fully connected layers. Everything after this is the same skeleton, deeper.

## AlexNet (Krizhevsky et al., 2012)

```
[227x227x3] INPUT
[55x55x96]  CONV1: 96 11x11 filters at stride 4
...
```

The result that started the era: a CNN won ILSVRC by a wide margin. Note the **11x11 filters at stride 4** — large and coarse, which the next architecture argues against.

## VGGNet (Simonyan & Zisserman, 2014)

> **Small filters, deeper networks.** 8 layers (AlexNet) → **16–19 layers** (VGG16Net). **Only 3x3 CONV.**

T09 poses the question directly: *"Why use smaller filters? (3x3 conv)"*

Because stacking them is strictly better. Three 3x3 layers have the same **receptive field** as one 7x7 layer (3 → 5 → 7, as the receptive-field slides show), but:

| | one 7x7 | three 3x3 |
|---|---|---|
| receptive field | 7 | 7 |
| parameters (per channel pair) | $49C^2$ | $3 \times 9C^2 = 27C^2$ |
| nonlinearities | 1 | **3** |

**Fewer parameters and more nonlinearity for the same field of view.** Slide 97 tabulates VGG's memory and parameter cost layer by layer, which makes the other lesson visible: most *memory* sits in the early conv layers, most *parameters* in the late FC layers.

## GoogLeNet (Szegedy et al., 2014)

The **Inception module** applies parallel filter operations to the same input — multiple filter sizes plus pooling — and concatenates the results, so the network does not have to commit to one scale per layer.

The naive version explodes in cost, so the deck shows the *"Inception module with **dimension reduction**"*: 1x1 convolutions inserted before the expensive 3x3 and 5x5 paths to cut channel depth first. This is where T09's earlier remark pays off —

> (btw, **1x1 convolution layers make perfect sense**) — each filter has size 1x1x64, and performs a 64-dimensional dot product

A 1x1 conv touches no spatial extent but mixes and compresses **channels**, which is exactly what a bottleneck needs.

## ResNet (He et al., 2015)

### The problem

> What happens when we continue stacking deeper layers on a "plain" convolutional neural network?

The 56-layer network performs **worse than the 20-layer one** — and critically, worse on **training** error too. So it is not [[Overfitting]]. A deeper network can always represent a shallower one (make the extra layers identity), so this is an **optimization** failure: gradient descent cannot find that solution.

### The fix

> **Use network layers to fit a residual mapping instead of directly trying to fit a desired underlying mapping.**

A residual block computes

$$\text{output} = F(x) + x$$

where $x$ arrives on an **identity** shortcut. If the optimal transformation for a block is "do nothing," the network only has to drive $F(x) \to 0$ — far easier than learning an identity through several nonlinear layers. The shortcut also lets gradient flow backward unattenuated, which addresses the vanishing-gradient problem from [[Activation Functions]] architecturally rather than by changing the nonlinearity.

Depths of **34, 50, 101, or 152** layers for ImageNet; ResNet-50 and up use a *"bottleneck layer to improve efficiency (similar to GoogLeNet)."*

## Identity Mappings (He et al., ECCV 2016)

A follow-up asking two empirical questions on ResNet-110 / CIFAR-10. The results are unusually clean.

**Question 1: "What if shortcut mapping $h \ne$ identity?"**

| shortcut | error |
|---|---|
| $h(x) = x$ | **6.6%** |
| $h(x) = 0.5x$ | 12.4% |
| $h(x) = \text{gate}\cdot x$ | 8.7% |

Conv shortcuts and dropout shortcuts are also worse. T09's conclusion: **"$h$ = identity: don't block signal."** Even scaling by $0.5$ nearly doubles the error — because it attenuates the gradient at every one of 110 blocks, compounding to near-nothing.

**Question 2: "What if post activation $\sigma$ = identity?"**

Comparing **post-activation** against **pre-activation**:

```
pre-activation block:   BN -> ReLU -> weight -> BN -> ReLU -> weight -> addition
```

Pre-activation keeps the shortcut path completely clean and enables **1001-layer ResNets**.

## The Bridge to Transformers

T09's final slide links pre-activation directly to **pre-normalization** in *"Attention is all you need"* (Vaswani et al., 2017) and GPT-2. The same design choice reappears in [[CSCE 421 T10 — Attention, Transformers, and Large Language Models|T10]] as

$$Z = Y(\mathrm{LayerNorm}[X]) + X$$

So the residual-plus-norm block developed here for vision is the block [[Transformers]] are built from. The deck ends on vision and begins the next one on language with the same structure intact.

## See Also

- [[Convolutional Neural Networks]]
- [[Convolution]]
- [[Batch Normalization]]
- [[Transfer Learning]]
- [[Transformers]]
- [[Deep Learning]]
- [[CSCE 421]]
