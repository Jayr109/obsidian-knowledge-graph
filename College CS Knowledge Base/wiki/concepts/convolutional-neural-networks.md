---
title: "Convolutional Neural Networks"
type: concept
tags: [csce420, csce421, cnn, alexnet, imagenet, receptive-fields, stride, padding, pooling, weight-sharing]
sources: [csce420-lecture-07-deep-learning, csce421-t08-convolution, csce421-t09-cnn]
course: CSCE 420, CSCE 421
updated: 2026-10-20
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

---

# The CSCE 421 Treatment

The section above is the [[CSCE 420]] survey. [[CSCE 421]] builds the layer from the ground up across [[CSCE 421 T08 — Convolution|T08]] (classical filtering) and [[CSCE 421 T09 — Convolutional Neural Networks|T09]] (127 slides, from CS231n).

## The Argument Against Fully Connected

T09 opens with the baseline: a $32\times32\times3$ image **stretched to $3072 \times 1$** and multiplied by a $10 \times 3072$ matrix. Two things are wrong with it — spatial structure is destroyed by the flattening, and the parameter count is enormous.

A convolution layer replaces it by sliding a small filter that spans the **full depth** of the input volume. T09 draws one figure three ways to make the cost concrete: convolution needs **3 parameters** where locally-connected needs **12** and fully-connected needs **24**, the latter two marked *"no weight-sharing."*

## Volumes and Activation Maps

Each filter produces one **activation map**; $K$ filters produce $K$ of them, stacked into the output volume:

$$32\times32\times3 \;\xrightarrow{\;6 \text{ filters of } 5\times5\times3\;}\; 28\times28\times6$$

A ConvNet is then *"a sequence of Convolution Layers, interspersed with activation functions"* — CONV, ReLU, CONV, ReLU, POOL, and so on.

## Spatial Arithmetic

$$\text{output} = \frac{N - F}{\text{stride}} + 1 \qquad\text{and with padding}\qquad \frac{N + 2P - F}{\text{stride}} + 1$$

A non-integer result means the filter **does not fit** and the configuration is invalid. Padding $P = (F-1)/2$ preserves spatial size, which matters because repeated convolution shrinks volumes ($32 \to 28 \to 24 \dots$) and *"shrinking too fast is not good."* Full treatment on [[Convolution]].

**Parameter count for a conv layer**, the exam-shaped calculation:

$$\left(F \times F \times C_{in} + 1\right) \times K$$

T09's worked case — input $32\times32\times3$, ten $5\times5$ filters, stride 1, pad 2 — gives output $32\times32\times10$ and $(5\cdot5\cdot3+1)\times10 = 76 \times 10 = 760$ parameters. Compare the fully connected alternative.

## Pooling

*"Makes the representations smaller and more manageable"* and *"operates over each activation map independently"* — so pooling changes $H$ and $W$ but never the number of channels. The canonical case is **max pool, $2\times2$, stride 2**:

```
1 1 2 4           6 8
5 6 7 8    ->     3 4
3 2 1 0
1 2 3 4
```

## Receptive Field

The region of input that can influence one output. Kernel 3 gives 3; stacking another gives 5; adding stride 2 gives 7. *"Composing many conv layers can create a large receptive field"* — depth buys global context without any single layer being global. This is the quantitative version of the hierarchy described in [[Deep Learning]].

## 1x1 Convolutions

*"(btw, 1x1 convolution layers make perfect sense)"* — a $1\times1\times64$ filter still performs a 64-dimensional dot product at each position, so it mixes and compresses **channels** while leaving spatial extent untouched. This is what makes the Inception bottleneck in [[CNN Architectures]] work.

## Training a CNN

Nothing new. The loop from T02 wraps unchanged:

```
1. Sample a batch of data
2. Forward prop it through the graph (network), get loss
3. Backprop to calculate the gradients
4. Update the parameters using the gradient
```

What T09 adds is the machinery that makes deep versions trainable: [[Activation Functions]] (ReLU over tanh), [[Batch Normalization]], [[Dropout]] and data augmentation, and [[Transfer Learning]] when data is scarce. The architectures that resulted are on [[CNN Architectures]].

## See Also

- [[Convolution]]
- [[CNN Architectures]]
- [[Batch Normalization]]
- [[Transfer Learning]]
- [[Deep Learning]]
- [[Backpropagation]]
- [[Neural Networks]]
- [[Transformers]]
- [[CSCE 420]]
- [[CSCE 421]]
