---
title: "Transfer Learning"
type: concept
tags: [csce421, transfer-learning, finetuning, pretraining, imagenet, feature-reuse]
sources: [csce421-t09-cnn]
course: CSCE 421
updated: 2026-10-20
---

Transfer learning reuses a network trained on one large dataset as the starting point for a different, usually smaller task. [[CSCE 421 T09 — Convolutional Neural Networks|T09]] presents it as the standard answer to *"I don't have ImageNet-scale data"* — which is almost everyone.

## Why It Works

The reason is visible in what a [[Convolutional Neural Networks|CNN]] learns. T09 labels the layer stack with an axis:

```
  FC-1000          More specific   <- task-dependent: "which of these 1000 classes"
  FC-4096
  Conv-512
  ...
  Conv-64          More generic    <- edges, colors, textures
  Image
```

Early layers learn **edges, colors and simple textures** — properties of natural images in general, not of ImageNet's particular 1000 categories. Those are worth keeping no matter what the new task is. Only the top of the stack is specific to the original labels.

This is the same hierarchy [[Deep Learning]] describes as *pixels → edges → object parts → objects*.

## The Procedure

T09 gives three regimes on a VGG stack:

**1. Train on ImageNet.** Or download someone else's weights, which is what actually happens.

**2. Small dataset, $C$ classes.** *"Freeze these"* — every convolutional layer — and *"reinitialize this and train"* — only the final `FC-C`. The network becomes a fixed feature extractor with a fresh [[Softmax Regression|softmax]] classifier on top. You are training a linear model on learned features.

**3. Bigger dataset.** Freeze fewer layers and finetune more of the stack, with the caveat T09 states explicitly:

> **Lower learning rate when finetuning; 1/10 of original LR is good.**

Pretrained weights are already near a good solution. A full-size learning rate would destroy them in the first few steps.

## The Decision Table

Slide 89, organized on the two dimensions that actually matter:

| | **very similar** dataset | **very different** dataset |
|---|---|---|
| **very little data** | Use linear classifier on top layer | *"You're in trouble…"* — try a linear classifier from **different stages** |
| **quite a lot of data** | Finetune a few layers | Finetune a **larger number** of layers |

Two readings worth having:

**More data → finetune more.** Finetuning adds trainable parameters, so it needs data to avoid [[Overfitting]]. With very little data, training only the last layer is the right call for exactly the capacity-control reasons in [[Model Selection]].

**Less similar → go deeper down the stack.** The awkward cell is little data *and* a very different domain (medical scans, satellite imagery). The suggestion to take features from *earlier* stages follows from the generic/specific axis: if the late layers encode ImageNet-specific concepts that don't transfer, the generic early ones might still.

## Where This Leads

T09 covers transfer learning for vision, but the pattern generalizes and is the dominant paradigm in [[Large Language Models]]. [[CSCE 421 T10 — Attention, Transformers, and Large Language Models|T10]] describes the same two-phase structure in its own vocabulary:

> A large model is first **pre-trained using unlabelled data** and then **fine-tuned using supervised learning** based on a much smaller set of labelled data. A model with broad capabilities that can subsequently be fine-tuned for specific tasks is called a **foundation model**.

T10 also gives the parameter-efficient version, **LoRA**, where the pretrained weights are frozen entirely and small low-rank matrices are trained alongside — the logical extreme of *"freeze these."*

## See Also

- [[Convolutional Neural Networks]]
- [[CNN Architectures]]
- [[Large Language Models]]
- [[Model Selection]]
- [[Overfitting]]
- [[Deep Learning]]
- [[CSCE 421]]
