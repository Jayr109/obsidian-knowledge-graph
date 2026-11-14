---
title: "CSCE 420 Lecture 7 — Deep Learning"
type: source
tags: [lecture, csce420, deep-learning, cnn, dqn, lstm, transformers]
sources: []
course: CSCE 420
exam: final
updated: 2026-09-01
---

Slide deck 7 of [[CSCE 420]], by [[Yoonsuck Choe]]. 84 slides. Covers deep learning from the neural-network refresher through convolutional networks, deep reinforcement learning, recurrent networks and LSTM, transformers and large language models, and the field's limitations.

## Structure

| Slides | Section |
|---|---|
| 2–11 | What deep learning is; NN refresher; function approximation |
| 12–28 | Representation learning; deep architectures |
| 29–37 | Deep convolutional networks: AlexNet, what is learned |
| 38–51 | Deep reinforcement learning; DQN |
| 52–64 | Deep recurrent networks; LSTM; attention |
| 65–79 | Transformers and large language models |
| 80–84 | Advanced topics; limitations; summary |

## The Definition

> **Learning higher level abstractions/representations from data.** Motivation: how the brain represents and processes sensory information in a **hierarchical** manner.

## The $\sin(x)$ Demonstration

An unusually clear teaching device. Fitting $y = \sin(x)$ with model `[2,tanh:1,linear]` — two hidden units, one linear output — shows **the hidden neurons representing sigmoids and the output being their linear combination**. Scaling to `[20,tanh:3,tanh:1,linear]` composes twenty sigmoids through further layers.

The same example then exposes a limitation: **out-of-range inputs** show the network fitted the training interval rather than learning the function.

## The Strongest Evidence in the Deck

AlexNet's **first-layer kernels resemble mammalian receptive fields** — oriented Gabor patterns and color opponency (red-green, blue-yellow) — with higher layers representing progressively more complex features. Nobody designed those filters; they fell out of backprop on a classification objective. That is the concrete case that learned representations can replace hand-designed ones. See [[Convolutional Neural Networks]].

## The Attention Progression

Worth following as a three-step argument rather than three topics:

1. **[[Recurrent Neural Networks|RNN]]** passes only the *last* encoder hidden vector to the decoder — and **cannot remember far into the past**
2. **[[Long Short-Term Memory|LSTM]]** adds gated memory (input/forget/output) so long-term retention becomes possible
3. **RNN with attention** (Bahdanau, Cho & Bengio 2015) uses a **weighted sum of all** hidden vectors, with weights learned end-to-end
4. **[[Transformers]]** (Vaswani et al. 2017) drop recurrence entirely — **highly parallelizable, reduces serial computation**

The neural machine translation attention map, plotting $\alpha_{ij}$ from source word $j$ to target word $i$, is effectively a **learned word alignment that nobody supervised**.

## The Limitations Section

Six stated limits: massive labeled data; long training and large models; catastrophic forgetting; **model design still mostly manual**; vulnerability to adversarial inputs; and poor explainability. Each is paired with an emerging response — AutoML/NAS for the design problem, DARPA XAI for explainability.

The fundamental open issues read as a list of what the first half of the course had and deep learning lacks: **reasoning, common-sense reasoning, causality**, meaning-level processing, **problem posing**, and AGI.

## Visual-Only Slides

Nearly all figures in this deck are external images — LeCun's tutorial slides, colah's LSTM diagrams, Jalammar's illustrated-transformer figures, and the Bahdanau attention heatmap. Slides 12–28 (representation learning), 45–51 (DQN internals and results), 71–79 (transformer internals and LLM examples) carry substantial figure content that is **not** in the text layer. The architectural claims and numbers have been captured; the visual intuitions have not.

## Pages Created

**New (4)**: [[Convolutional Neural Networks]], [[Transformers]], [[Long Short-Term Memory]], [[Deep Reinforcement Learning]]

**Reconciled (3)**: [[Deep Learning]], [[Deep Q-Network]], [[Neural Networks]]

## See Also

- [[Large Language Models]]

- [[CSCE 420]]
- [[Yoonsuck Choe]]
- [[Deep Learning]]
- [[AI Ethics]]
- [[CSCE 420 Final Exam Practice]]
