---
title: "CSCE 421 T09 — Convolutional Neural Networks"
type: source
tags: [lecture, csce421, cnn, convolution, pooling, batch-normalization, dropout, transfer-learning, resnet, activation-functions]
sources: []
course: CSCE 421
updated: 2026-10-20
---

Topic deck 9 of [[CSCE 421]]. **127 slides** — by far the largest deck in the course — credited *"Based on slides by Fei-Fei Li, Justin Johnson, Serena Yeung, Charu Aggarwal, Kaiming He"* and drawn from Stanford CS231n lectures 5–9. It covers the convolution layer, training machinery (activations, normalization, regularization), transfer learning, and a tour of ImageNet architectures.

> **Scope note — slides 46, 47 and 48 are marked "Optional for CSCE 421"** and contain nothing else. They sit between the fully-connected-layer slide and the mini-batch SGD slide. Treat them as excluded.

> **Extraction note:** CS231n slides are image-dominated. Spatial-arithmetic text survives, but the batch-normalization equations, the dropout figures, and all photographs do not. Equations below marked **[figure]** are the standard forms reconstructed from the cited papers; everything in quotes is verbatim.

## Part 1 — The Convolution Layer (slides 2–45)

### From fully connected to convolutional

Slide 2 sets the baseline: a `32x32x3` image **stretched to `3072 x 1`**, multiplied by a `10 x 3072` weight matrix. Each output is *"1 number: the result of taking a dot product between a row of W and the input."* Stretching destroys spatial structure and the parameter count is enormous.

Slide 3 replaces it. A `5x5x3` **filter** is convolved with the `32x32x3` image — *"slide over the image spatially, computing dot products."* The filter spans the **full depth** of the input volume.

- Each filter produces one `28x28x1` **activation map** (slides 5–6).
- *"If we had 6 5x5 filters, we'll get 6 separate activation maps"*, stacked into a `28x28x6` output volume (slide 7).
- Slide 8: *"ConvNet is a sequence of Convolution Layers, interspersed with activation functions"* — CONV, ReLU, CONV, ReLU, POOL, and so on.

### Spatial arithmetic (slides 10–22) — the exam-shaped part

Slides 11–19 walk a `7x7` input with a `3x3` filter at several strides, arriving at the formula on slide 20:

```
Output size:   (N - F) / stride + 1

e.g. N = 7, F = 3:
  stride 1 => (7 - 3)/1 + 1 = 5
  stride 2 => (7 - 3)/2 + 1 = 3
  stride 3 => (7 - 3)/3 + 1 = 2.33    (does not fit)
```

The stride-3 case *"doesn't fit"* — a non-integer result means the configuration is invalid, which slide 19 states outright.

Slides 21–22 add zero padding:

> In general, common to see CONV layers with stride 1, filters of size FxF, and zero-padding with **(F-1)/2** (will preserve size spatially).
>
> `F = 3 => zero pad with 1` · `F = 5 => zero pad with 2` · `F = 7 => zero pad with 3`

Slide 23 gives the motivation: *"32x32 input convolved repeatedly with 5x5 filters shrinks volumes spatially! (32 -> 28 -> 24 ...). Shrinking too fast is not good."*

### Worked examples (slides 38–41)

```
Input volume: 32x32x3,  10 5x5 filters, stride 1, pad 2

Output volume size:   (32 + 2*2 - 5)/1 + 1 = 32 spatially,  so  32x32x10

Number of parameters: each filter has 5*5*3 + 1 = 76 params   (+1 for bias)
                      => 76 * 10 = 760
```

Slide 42 notes *"1x1 convolution layers make perfect sense"* — a `1x1x64` filter still performs a 64-dimensional dot product at each spatial position, so it mixes channels without touching spatial extent.

### Why convolution rather than full connectivity (slides 24–37)

- **Translation equivariance** (24–30): *"process each window in the same way, apply the same weights regardless of the window location."* Slide 30 states the property as the output shift *"does not depend on x."*
- **Parameter count** (31): the same figure drawn three ways — convolution `# params = 3`, locally connected `# params = 12` (*no weight-sharing*), fully connected `# params = 24` (*no weight-sharing*).
- **Convolution as a linear transform** (32–33): `y = Wx` where *"W is sparse"* with *"local connection"* and shared sliding entries `w_-1, w_0, w_1`.
- **Receptive field** (34–37): kernel 3 gives receptive field 3; stacking gives 5; adding stride 2 gives 7. *"Composing many conv layers can create a large receptive field."*

### Pooling and FC (slides 43–45)

Pooling *"makes the representations smaller and more manageable"* and *"operates over each activation map independently."* Slide 44 shows the canonical example — **max pool with 2x2 filters and stride 2**:

```
1 1 2 4           6 8
5 6 7 8    ->     3 4
3 2 1 0
1 2 3 4
```

Slide 45 covers the FC layer and asks *"How to perform BP in CNN?"*

## Part 2 — Training Machinery (slides 49–86)

### Mini-batch SGD (slide 49)

```
Loop:
  1. Sample a batch of data
  2. Forward prop it through the graph (network), get loss
  3. Backprop to calculate the gradients
  4. Update the parameters using the gradient
```

Exactly the loop from [[CSCE 421 T02 — Logistic Regression for Binary Classification|T02]], now wrapping a CNN.

### Activation functions (slides 50–53)

| Function | Slide notes |
|---|---|
| `tanh(x)` | *"Squashes numbers to range [-1,1]"*, *"zero centered (nice)"*, *"still kills gradients when saturated"* |
| **ReLU** `f(x) = max(0,x)` | *"Does not saturate (in +region)"*, *"Very computationally efficient"*, *"Converges much faster than sigmoid/tanh in practice (e.g. 6x)"*, *"Actually more biologically plausible than sigmoid"*, *"Not zero-centered output"* |

Slide 52 ends on a question: *"An annoyance: hint, what is the gradient when x < 0?"* — the dead-ReLU problem. See [[Activation Functions]].

### Why normalize (slides 55–61)

Slide 55 restates the update `W := W - eta * dE/dW` and shows learning-rate regimes: *"gradually converging / ideal / oscillating"*, citing LeCun et al. 1998 *"Efficient Backprop"*.

Slide 56 gives the argument:

> - Same learning rate applied to all weights
> - **Large weights dominate updates**
> - **Small weights oscillate (or diverge)**
> - Similar pace for all weights [when normalized]

Slide 57 asks the question that matters at test time — training data has a mean and standard deviation, and the test data's are marked **"?"**. Slide 58: *"In practice for Images: center only."*

Slides 59–61 extend it inward: *"We want to maintain variance for all layers — normalize features in the network,"* with the key reframing *"what if we think of this as a new input?"*

### Batch Normalization (slides 62–71)

> **"you want zero-mean unit-variance activations? just make them so."**

Slide 64, for a batch `X` of shape `N x D`:

> 1. compute the empirical **mean and variance independently for each dimension**
> 2. **Normalize**

```
[figure]   mu_j    = (1/N) sum_i x_ij
           var_j   = (1/N) sum_i (x_ij - mu_j)^2
           x_hat   = (x - mu) / sqrt(var + eps)
```

Slide 63 notes this is *"a vanilla differentiable function"* — so it backpropagates like any other layer.

Slide 65: *"Usually inserted after Fully Connected or Convolutional layers, and before nonlinearity"* — `FC -> BN -> tanh -> FC -> BN -> tanh -> ...`

Slide 66 adds the learnable scale and shift:

> And then allow the network to **squash the range if it wants to** … Note, the network can learn **to recover the identity mapping**.

```
[figure]   y = gamma * x_hat + beta

           gamma = sqrt(var), beta = mu   ->   recovers the identity
```

Slide 67, the benefits:

> - Improves gradient flow through the network
> - Allows higher learning rates
> - Reduces the strong dependence on initialization
> - Acts as a form of regularization in a funny way, and slightly reduces the need for dropout, maybe

Slide 68, the detail that makes it exam material:

> Note: **at test time BatchNorm layer functions differently.** The mean/std are **not** computed based on the batch. Instead, a single fixed empirical mean of activations during training is used (e.g. can be estimated during training with **running averages**).

Slides 69–70 lay this out as Input / Learnable params / Intermediates / Output, contrasting *"Estimate mean and variance from minibatch; **can't do this at test-time**"* against *"**(Running) average** of values seen during training."*

Slide 71 gives the shapes:

```
fully-connected:   x: N x D           mu,sigma: 1 x D           gamma,beta: 1 x D
convolutional:     x: N x C x H x W   mu,sigma: 1 x C x 1 x 1   gamma,beta: 1 x C x 1 x 1
                   (Spatial Batchnorm, BatchNorm2D)
```

Full treatment on [[Batch Normalization]].

### Layer Normalization (slide 72)

Same formula `y = gamma*(x-mu)/sigma + beta`, but the statistics are taken **per sample across features** (`mu,sigma: N x 1`) instead of per feature across the batch (`1 x D`). Two consequences stated on the slide:

> **Same behavior at train and test!** Can be used in recurrent networks.

This is why transformers use LayerNorm — see [[CSCE 421 T10 — Attention, Transformers, and Large Language Models|T10]].

### Regularization (slides 73–86)

**Early stopping** (73): train/val curves with *"Stop training here"* marked at the point validation accuracy turns.

**Dropout** (74–79): *"In each forward pass, randomly set some neurons to zero. Probability of dropping is a hyperparameter; 0.5 is common"* (Srivastava et al., JMLR 2014). Two justifications given:

> Forces the network to have a **redundant representation**; prevents co-adaptation of features.
>
> Another interpretation: dropout is **training a large ensemble of models** that share parameters.

At test time (77–79) the randomness must be averaged out — *"want to approximate the integral."*

**Data augmentation** (81–85): horizontal flips, random crops and scales. The ResNet recipe is given: *"Pick random L in range [256, 480]; resize training image, short side = L; sample random 224 x 224 patch."*

**The unifying pattern** (80, 86) — stated twice, which signals its importance:

> **Training: add some kind of randomness. Testing: average out randomness (sometimes approximate).**
>
> Examples: Dropout, **Batch Normalization**, Data Augmentation, DropConnect

Batch norm is named as a member of this family — its training/test asymmetry is not an implementation wart but the same mechanism dropout uses.

## Part 3 — Transfer Learning (slides 87–89)

Train on ImageNet, then reuse. Slide 88 gives three regimes on a VGG stack: train on ImageNet; for a **small dataset** *"freeze these"* (all conv layers) and *"reinitialize this and train"* (the final FC); for a **bigger dataset** freeze fewer layers and finetune more, with *"lower learning rate when finetuning; 1/10 of original LR."*

Slide 89 is the decision table, organized by how similar the new dataset is and how much of it there is:

| | very similar dataset | very different dataset |
|---|---|---|
| **very little data** | Use linear classifier on top layer | *"You're in trouble…"* try linear classifier from different stages |
| **quite a lot of data** | Finetune a few layers | Finetune a larger number of layers |

The axis label on the stack — *"More generic"* at the bottom, *"More specific"* at the top — is the reason this works.

## Part 4 — Architecture Case Studies (slides 91–127)

| Architecture | Slides | Key points |
|---|---|---|
| **LeNet-5** (LeCun 1998) | 91 | *"Conv filters were 5x5, applied at stride 1; subsampling (pooling) layers were 2x2 applied at stride 2"* |
| **AlexNet** (Krizhevsky 2012) | 92 | `[227x227x3] INPUT`, `CONV1: 96 11x11 filters at stride 4` |
| **VGGNet** (Simonyan & Zisserman 2014) | 94–97 | *"Small filters, deeper networks"*, 8 to 16–19 layers, **only 3x3 CONV**; slide 97 tabulates memory and params layer by layer |
| **GoogLeNet** (Szegedy 2014) | 99–101 | Naive Inception module, then *"Inception module with dimension reduction"* (1x1 bottlenecks), stacked |
| **ResNet** (He 2015) | 103–112 | The deeper-is-worse observation, then residual blocks |

Slides 93, 98, 102 and 112 repeat the **ILSVRC winners** chart: *"shallow, 8 layers, 8 layers, 19 layers, 22 layers, 152 layers."*

### ResNet (103–112)

Slide 103 poses the problem: *"What happens when we continue stacking deeper layers on a 'plain' convolutional neural network?"* — the 56-layer net does **worse** than the 20-layer one, on training error as well as test, so it is not overfitting.

Slide 105: *"Solution: use network layers to fit a **residual mapping** instead of directly trying to fit a desired underlying mapping."* The block computes `F(x) + x` with an `identity` shortcut. Depths of **34, 50, 101, or 152** layers for ImageNet; ResNet-50+ uses a *"bottleneck layer to improve efficiency (similar to GoogLeNet)."*

### Identity Mappings (113–127)

A follow-up study (He et al., ECCV 2016) asking two questions empirically on ResNet-110 / CIFAR-10:

**Question 1: "What if shortcut mapping h is not identity?"**

```
h(x) = x            error:  6.6%     <- identity wins
h(x) = 0.5x         error: 12.4%
h(x) = gate * x     error:  8.7%
```

Slide 123's conclusion: *"h = identity: don't block signal."* Conv shortcuts and dropout shortcuts are also tested and are worse.

**Question 2: "What if post activation is identity?"** — slides 125–126 compare post-activation against **pre-activation** (`BN -> ReLU -> weight -> BN -> ReLU -> weight -> addition`), which enables **1001-layer ResNets**.

Slide 127 closes by linking this to **pre-activation / pre-normalization** in *"Attention is all you need"* (Vaswani et al., 2017) and GPT-2 — the direct bridge into [[CSCE 421 T10 — Attention, Transformers, and Large Language Models|T10]], where the same pre-norm choice reappears as `Z = Y(LayerNorm[X]) + X`.

## See Also

- [[Convolutional Neural Networks]]
- [[Batch Normalization]]
- [[Activation Functions]]
- [[Dropout]]
- [[Transfer Learning]]
- [[CNN Architectures]]
- [[Convolution]]
- [[Regularization]]
- [[CSCE 421]]
