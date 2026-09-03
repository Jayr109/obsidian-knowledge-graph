---
title: "Deep Learning"
type: concept
tags: [csce420, deep-learning, cnn, rnn, transformers, limitations]
sources: [csce420-lecture-01-introduction, csce420-final-practice, csce420-lecture-07-deep-learning]
course: CSCE 420
updated: 2026-09-01
---

Deep learning is machine learning with many-layered [[Neural Networks|neural networks]] that learn a hierarchy of features directly from raw data, replacing hand-engineered features. Lecture 1 dates the era from the mid-2010s to the present and identifies three ingredients that made it possible.

## Fuel for the Deep Learning Revolution

1. **Algorithm** — very deep neural networks
2. **Big data**
3. **Computing power** — GPU-based

All three were necessary; none alone was sufficient, which is why the ideas of the 1980s (backpropagation, convolutional nets, the Neocognitron — all in the [[History of AI]] timeline) had to wait thirty years to work.

## Architecture Families and Their Domains

| Architecture | Primary domain | Course answer (Final Practice, Problem 9) |
|---|---|---|
| **CNN** — convolutional neural networks | Vision: hierarchical feature extraction over images | **(C) computer vision** |
| **Deep RL** — deep reinforcement learning | Control of behavior from perception | **(B) robotics / autonomous driving** |
| **RNN / Transformer** | Sequence modeling, attention, language | **(A) natural language processing** |

The mapping follows the structure each architecture assumes: convolution assumes spatial locality (images), recurrence and attention assume sequence (language), and reinforcement learning assumes an agent taking actions and receiving reward (control). See [[Reinforcement Learning]] and [[Deep Q-Network]].

The CNN slide illustrates the hierarchy explicitly: learned features progress from **pixels → 1st-stage edges → 2nd-stage object parts → 3rd-stage objects.** That progression — from raw signal to composed structure with no human specifying the intermediate levels — is what "deep" buys.

## Advances (Lecture 1)

- **Vision, speech, NLP** — superhuman in some cases. Beyond classification: detection, semantic and instance segmentation, enhanced speech.
- **Vision + language** — visual question answering, question answering grounded in images.
- **Beyond perception and language** — control of complex behavior based on perception. Deep RL (AlphaGo, AlphaStar) learns to behave from perception plus reward; the slide shows Atari games, VizDoom, Montezuma's Revenge, Minecraft, and simulated robot locomotion.

## Limitations (Lecture 1)

The lecture is explicit that the results come with structural problems:

- **Needs large data;** cannot do complex reasoning
- **Lack of common sense**
- **Lack of interpretability;** susceptible to noise
- **Learns spurious features**

Each is illustrated. *Sensitivity to small perturbations:* an imperceptible perturbation flips a confident "panda" prediction to "gibbon," and physically altered stop signs are misread. *Lack of common sense:* an object detector labels a scene's contents correctly but has no basis for a question like "what to rescue first in case of fire." *Spurious features:* a husky-vs-wolf classifier turns out to have learned **snow in the background**, not any property of the animal.

These four limitations are the exact motivation for [[Neurosymbolic AI]] on the following slide — reasoning, common sense, and interpretability are what [[Symbolic AI]] had and deep learning lacks.

## Where Deep Learning Starts (CSCE 421)

The closing slide of [[CSCE 421]]'s softmax deck frames deep learning as one substitution. Keep the [[Softmax Function|softmax]] head and [[Cross-Entropy Loss]] exactly as they are, and replace the hand-designed input vector $\mathbf{x}$ with the output of a CNN or Transformer over images, text, or speech.

The question it poses — **how do we learn $X$ automatically?** — is the dividing line. [[Linear Models]] require someone to decide that a digit should be described by intensity and symmetry; deep learning learns that representation from data. The classifier on top is unchanged.

## From the Lecture (Deck 7)

### Definition

> **Learning higher level abstractions/representations from data.**
> Motivation: how the brain represents and processes sensory information in a **hierarchical** manner.

### The Four Architectures

The deck's own closing summary:

| Architecture | Verdict |
|---|---|
| **[[Convolutional Neural Networks\|Deep convolutional networks]]** | High computational demand; across-the-board great performance in vision |
| **[[Deep Q-Network]]** | Unique approach to RL; **end-to-end** machine learning; super-human performance |
| **[[Recurrent Neural Networks\|Deep recurrent networks]]** | Sequence learning; **[[Long Short-Term Memory\|LSTM]] is a powerful mechanism** |
| **[[Transformers]]** | Based on self-attention; **surpasses RNNs and even infringes on CNN territory**; LLMs such as ChatGPT are built on it |

### The Evidence That Representations Are Learned

AlexNet's first-layer kernels come out resembling **mammalian receptive fields** — oriented Gabor patterns and color opponency — with **higher layers representing progressively more complex features**. Nobody designed those filters. This is the concrete support for the claim that learned representations replace hand-designed ones.

### Six Limitations

- Requires **massive amounts of (labeled) data**
- **Long training time**, large trained models
- **Catastrophic forgetting**
- **Designing a good model is done mostly manually**
- **Vulnerable to adversarial inputs**
- **Hard to explain** how it works or what it learned

The fourth is quietly ironic: deep learning automated feature design but left architecture design to humans.

### Emerging Responses

| Limitation | Response |
|---|---|
| Data | Active learning, core sets, data augmentation |
| Computing time | Train with reduced data; compact models |
| Large models | Compression, distillation |
| Catastrophic forgetting | Various approaches, **not perfect yet** |
| Manual design | **AutoML, NAS, ENAS, evolution** |
| Adversarial inputs | Adversarial training, defensive distillation |
| Explainability | **DARPA XAI**, explanation generation, Bayesian program induction, semantic associations |

The manual-design row closes a loop with [[Genetic Algorithms]] — evolution returns as a way to search architectures.

### Advanced Topics Named

DALL·E 2; **Generative Adversarial Networks** (style transfer, data augmentation, deep fakes); **Graph Neural Networks** (molecular fingerprinting, combinatorial optimization, vision); meta/transfer/multi-task/imitation learning; optimizers (**Adam, RMSprop**); continuous, semi-supervised, active, and federated learning; model compression and distillation.

### The Fundamental Open Issues

The deck's final list is a research agenda, and it reads as a list of everything the first half of the course had and deep learning lacks:

- **Reasoning, common-sense reasoning, causality**
- Self-supervised learning; combining unsupervised with supervised/reinforcement learning
- Human-like learning; **meaning/semantic-level processing**
- **Problem posing**; coping with new tasks
- Tool construction and tool use
- **Open-endedness, Artificial General Intelligence**

*Problem posing* echoes the caution in [[Machine Learning]] — ML solves problems but does not pose them (Choe and Mann, 2012) — and *reasoning and causality* are precisely what [[Neurosymbolic AI]] proposes to recover.

## See Also

- [[Softmax Regression]]
- [[Linear Models]]
- [[Neural Networks]]
- [[Reinforcement Learning]]
- [[Deep Q-Network]]
- [[Neurosymbolic AI]]
- [[History of AI]]
- [[Machine Learning Paradigms]]
- [[CSCE 421]]
