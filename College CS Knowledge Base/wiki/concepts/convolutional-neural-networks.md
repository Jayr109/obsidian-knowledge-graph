---
title: "Convolutional Neural Networks"
type: concept
tags: [csce420, cnn, alexnet, imagenet, receptive-fields]
sources: [csce420-lecture-07-deep-learning]
course: CSCE 420
updated: 2026-09-01
---

Deep convolutional networks are the architecture that made [[Deep Learning]] credible for vision. The lecture's case study is **AlexNet**.

## AlexNet (Krizhevsky et al., 2012)

- Applied to the **ImageNet** competition: 1.2 million images, 1,000 classes
- **60 million parameters** and **650,000 neurons**
- Top-1 error **37.5%**, top-5 error **17.0%**
- **Trained with backprop** — see [[Backpropagation]]

Nothing about the learning rule was new. What changed was scale, data, and the convolutional architecture.

## What the Network Learns

This is the part that matters conceptually:

- **First convolutional layer kernels resemble mammalian receptive fields** — oriented **Gabor patterns** and **color opponency** (red-green, blue-yellow).
- **Higher layers represent progressively more complex features.**

The first point is the striking one. Nobody designed those filters; they emerged from gradient descent on a classification objective, and they match what neuroscience finds in early visual cortex. This is the empirical support for the [[Deep Learning]] claim that learned representations can replace hand-designed features — and it connects back to [[Foundations of AI]]'s neuroscience thread.

Internal inspection also shows that test images sit closest, in hidden-representation space, to training images that are **semantically** similar rather than merely pixel-similar.

## Depth and Architecture

- **Depth inflation: deeper is better** — the trend that gave the field its name
- But **not just depth; architecture also matters**
- There is a three-way trade among **computation, performance, and memory** (model size)

## Beyond Vision

ConvNets apply to **speech recognition** by taking the **spectrogram and treating it as a 2D image**. The deck notes the state of the art has since moved to [[Transformers]].

That substitution — represent a non-image signal as an image, then reuse the vision architecture — is a recurring move in deep learning, and it is why architectural advances transfer across domains.

## See Also

- [[Deep Learning]]
- [[Backpropagation]]
- [[Neural Networks]]
- [[Transformers]]
- [[CSCE 420]]
