---
title: "CSCE 421"
type: course
tags: [csce421, machine-learning, course, linear-models, neural-networks, loss-functions, cnn, transformers, llm, pca, unsupervised]
sources: [csce421-t01-linear-regression, csce421-t02-logistic-regression, csce421-t03-softmax-regression, csce421-t03-softmax-regression-notes, csce421-t04-overfitting, csce421-t05-loss-functions, csce421-t05-loss-functions-notes, csce421-t06-multilayer-perceptron, csce421-t07-backpropagation-examples, csce421-t08-convolution, csce421-t09-cnn, csce421-t10-attention-transformers-llms, csce421-hw1-solution, csce421-hw2-solution, csce421-t11-pca-autoencoders, csce421-t11-pca-notes]
course: CSCE 421
updated: 2026-11-08
---

CSCE 421 (Machine Learning) is Texas A&M's undergraduate machine learning course, taught by [[Shuiwang Ji]]. The lecture material is built on Abu-Mostafa, Magdon-Ismail & Lin's *Learning From Data*. The opening arc is deliberately linear — every model in the first three topics is a linear model, differing only in what the linear signal $s = \mathbf{w}^T\mathbf{x}$ is passed through and what error measure is minimized — and the later topics generalize outward from exactly that point.

Ji has stated the standard for the course explicitly: the goal is **not to understand a little of everything, but to fully understand a few things, leaving nothing as a black box.**

## Logistics

- **Instructor:** [[Shuiwang Ji]] (Department of Computer Science & Engineering)
- **Primary text:** *Learning From Data* (Abu-Mostafa, Magdon-Ismail & Lin)
- Supplementary typed notes are distributed alongside some decks; the softmax notes were compiled by Yaochen Xie from Ji's lecture notes, and the loss-function note is co-authored with Lei Cai (WSU) and Hao Yuan (TAMU)

## Topic Arc

### T01–T03: One model, three output types

| Deck | Model | Output | Error measure | Optimizer |
|---|---|---|---|---|
| **T01** | [[Linear Regression]] | $y \in \mathbb{R}$ | Squared error | Closed form (pseudoinverse) |
| **T02** | [[Logistic Regression]] | $y \in [0,1]$, data $\pm 1$ | [[Cross-Entropy Loss]] | [[Gradient Descent]] / SGD |
| **T03** | [[Softmax Regression]] | Distribution over $K$ classes | Cross-entropy | Gradient descent |

All three share the [[Linear Models|linear signal]] $\mathbf{w}^T\mathbf{x}$. T01 uses it raw, T02 squashes it with the [[Sigmoid Function]], T03 generalizes that to the [[Softmax Function]] over $K$ signals. T03 closes by proving the binary case is exactly the $K=2$ case of the multi-class one.

### T04–T07: Generalization, loss, and depth

| Deck | Subject | What it adds |
|---|---|---|
| **T04** | [[Overfitting]] and [[Regularization]] | The first deck not about a new model — about when fitting *fails to be learning*. Adds [[Model Selection]] and cross-validation. |
| **T05** | [[Loss Functions]] | Six losses on one axis, unified by the margin $y_i s_i$. Establishes [[Convexity]] as the criterion separating usable losses from unusable ones. |
| **T06** | [[Multilayer Perceptron]] | Leaves linear models: XOR motivates hidden layers, and [[Backpropagation]] is derived in sensitivity notation. |
| **T07** | [[Backpropagation]] by examples | The same chain rule executed numerically on a computational graph (CS231n material). |

### T08–T10: Vision and language

| Deck | Subject | What it adds |
|---|---|---|
| **T08** | [[Convolution]] | Classical image filtering with hand-designed kernels — box filter, Sobel — ending on *"CNNs use data to train filter parameters."* |
| **T09** | [[Convolutional Neural Networks]] | 127 slides. The conv layer, then the training machinery: [[Activation Functions]], [[Batch Normalization]], [[Dropout]], [[Transfer Learning]], and [[CNN Architectures]] through ResNet. |
| **T10** | [[Attention Mechanism]] and [[Transformers]] | Data-dependent weights, Q/K/V, multi-head, positional encoding, then GPT/BERT/seq2seq and [[Large Language Models]]. |

| **T11** | [[Principal Component Analysis]] and [[Autoencoders]] | The first **unsupervised** topic. Linear-algebra groundwork ([[Eigendecomposition]], [[Singular Value Decomposition]]), PCA derived twice — maximum variance and minimum reconstruction error — then shown to be a linear autoencoder. |

**Textbook change at T10.** T01–T07 follow *Learning From Data*; T10 is based on Chapter 12 of Bishop & Bishop's *Deep Learning: Foundations and Concepts*. T08 and T09 are adapted from other courses (J. Xiao; Stanford CS231n).

### The three turns

The arc has three distinct pivots worth naming:

1. **T01 → T02.** The wrapper changes, and with it the loss — and a closed form stops existing, which is why [[Gradient Descent]] enters.
2. **T03 → T04.** The question changes from *how do I fit this model* to *which model should I be fitting*, answered empirically rather than analytically.
3. **T05 → T06.** [[Convexity]] is given up. A network's $E_{in}$ has many valleys, so gradient descent finds *a* local minimum rather than *the* minimum — and the guarantee that held since T01 is gone.
4. **T09 → T10.** **Fixed weights** are given up. Every model through T09 multiplies activations by weights frozen after training; [[Attention Mechanism|attention]] computes its mixing coefficients from the input at run time.
5. **T10 → T11.** **Labels** are given up. Ten decks of supervised learning give way to [[Unsupervised Learning|unsupervised]] methods that need no $y$ at all.

What survives the first four turns is the linear signal itself: [[Multilayer Perceptron|T06]] computes $s^{(\ell)} = \left(W^{(\ell)}\right)^T x^{(\ell-1)}$ at every layer, with the slide noting *"recall the linear signal $s = \mathbf{w}^T\mathbf{x}$."*

## Framing

The course opens by separating tasks that need arithmetic from tasks that need learning: a large multiplication is not intelligence, but answering *"is there a tree in this photo?"* cannot be written down as a rule. Learning from data means writing a program with free parameters and tuning them from labeled examples.

See [[Machine Learning Paradigms]] for the supervised/unsupervised/reinforcement split as this course frames it, and [[In-Sample and Out-of-Sample Error]] for the distinction that makes T04 necessary.

## Ingested Sources

| Source | Size |
|---|---|
| [[CSCE 421 T01 — Introduction and Linear Regression]] | 20 slides |
| [[CSCE 421 T02 — Logistic Regression for Binary Classification]] | 30 slides |
| [[CSCE 421 T03 — Logistic Regression: From Binary to Multi-Class]] | 20 slides |
| [[CSCE 421 T03 Notes — Softmax Regression Derivations]] | 6-page typed notes |
| [[CSCE 421 T04 — Overfitting and Regularization]] | 14 slides |
| [[CSCE 421 T05 — A Unified View of Loss Functions in Supervised Learning]] | 12 slides |
| [[CSCE 421 T05 Notes — A Unified View of Loss Functions]] | 4-page typed note |
| [[CSCE 421 T06 — Multi-Layer Perceptron/Networks]] | 24 slides |
| [[CSCE 421 T07 — Backpropagation by Examples]] | 9 slides |
| [[CSCE 421 T08 — Convolution]] | 13 slides (image-heavy) |
| [[CSCE 421 T09 — Convolutional Neural Networks]] | 127 slides; **46–48 marked "Optional for CSCE 421"** |
| [[CSCE 421 T10 — Attention, Transformers, and Large Language Models]] | 41 slides |
| [[CSCE 421 HW1 Solutions — Linear Models for Handwritten Digits]] | 4 pages, released answer key |
| [[CSCE 421 HW2 Solutions — Loss Functions, Backpropagation, MLP]] | 3 pages, released answer key |
| [[CSCE 421 T11 — Principal Component Analysis and Autoencoders]] | 32 slides |
| [[CSCE 421 T11 Notes — Principal Component Analysis and Autoencoders]] | 8-page typed note; carries two **exercises** and material the slides omit |

Decks are numbered by topic (T01, T02, ...), not by lecture date. Some ship a companion notes PDF; ingest both when present.

**Slide-numbering note:** footer numbers match PDF page numbers in T01 and T02, but **T03 runs one behind** (21 PDF pages, footer counts to 20). Confirm against the footer before citing a slide number.

## Exams

The course has **both a midterm and a final**, and Ji scopes topics to one or the other in lecture. Recorded so far:

| Item | Exam | Source |
|---|---|---|
| **[[Batch Normalization]]** — a question is promised | **Final only**, explicitly not the midterm | stated in class 2026-10-07 |
| T02 slide 9/30 "Predict Probabilities" | flagged as exam material; which exam **unconfirmed** | stated in class 2026-09-02 |
| T03 slide 9/20 "A Neural Network View" | flagged as exam material; which exam **unconfirmed** | stated in class 2026-09-09 |

**Answer-format warning.** Ji said a question will ask you to *calculate* the cross-entropy loss and that **writing the formula alone earns zero credit** — the arithmetic must be carried through to a number.

**Scope exclusion.** [[CSCE 421 T09 — Convolutional Neural Networks|T09]] slides 46, 47 and 48 are marked *"Optional for CSCE 421."*

## Relation to CSCE 420

This course overlaps [[CSCE 420]]'s [[Neural Networks]] and [[Deep Learning]] material from the opposite direction — bottom-up derivation rather than top-down survey. [[Backpropagation]], [[Machine Learning Paradigms]], [[Convolutional Neural Networks]], [[Transformers]] and [[Large Language Models]] carry both treatments on one page, the 420 survey above a `# The CSCE 421 Treatment` section; [[Perceptron]] and [[Linear Separability]] remain the 420-side pages and are cross-linked rather than duplicated.

## See Also

- [[Linear Models]]
- [[Linear Regression]]
- [[Logistic Regression]]
- [[Softmax Regression]]
- [[Loss Functions]]
- [[Overfitting]]
- [[Multilayer Perceptron]]
- [[Backpropagation]]
- [[Convolution]]
- [[Convolutional Neural Networks]]
- [[Batch Normalization]]
- [[Attention Mechanism]]
- [[Transformers]]
- [[Principal Component Analysis]]
- [[Singular Value Decomposition]]
- [[Autoencoders]]
- [[Gradient Descent]]
- [[Machine Learning Paradigms]]
- [[Shuiwang Ji]]
