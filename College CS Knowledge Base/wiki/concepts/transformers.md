---
title: "Transformers"
type: concept
tags: [csce420, transformers, self-attention, llm, qkv, attention]
sources: [csce420-lecture-07-deep-learning]
course: CSCE 420
updated: 2026-09-01
---

The Transformer (Vaswani et al., 2017 — *Attention is all you need*) replaced recurrence with **self-attention**. The deck's summary: transformers **surpass RNNs, and even infringe on CNN territory**, and Large Language Models such as ChatGPT are built on them.

## Why It Won

- **Highly parallelizable** — reduces serial computation

This is the decisive property. An [[Recurrent Neural Networks|RNN]] must process a sequence step by step, so training time scales with sequence length and cannot be parallelized across positions. Self-attention compares all positions simultaneously.

## The Architecture

- **Multi-head self-attention**
- **Position encoding** and **position-wise feed-forward** layers
- Organized over **Query, Key, Value (Q, K, V)**

Position encoding is required precisely *because* attention is order-agnostic: having discarded sequential processing, position must be reintroduced explicitly.

## Self-Attention

> **Goal: turn a raw token $x_i$ into a "mixture" token $z_i$ that contains some aspect of $\{x_1, x_2, x_3\}$.**

The mechanism:

1. Generate **Q, K, V** from each input token $x_i$
2. **Q comes from the current word; (K, V) come from the compared word**
3. **QK computes the weight** $w$ — how much the compared word should contribute
4. The output is the weighted combination of values

Each token's new representation is therefore a blend of the whole sequence, weighted by learned relevance.

## The Path From Attention

The deck builds up to this rather than starting there:

1. **[[Recurrent Neural Networks|RNN]]** — uses only the *last* hidden vector from the encoder as decoder input
2. **RNN with attention** (Bahdanau, Cho & Bengio, ICLR 2015) — uses a **weighted sum of all hidden vectors**, with weights computed by a small feed-forward net from the encoder states, **trained end-to-end** and changing dynamically per input
3. **Transformer** — drop the recurrence entirely and keep only attention

The neural machine translation visualization makes attention legible: source language on one axis, target on the other, pixel intensity showing $\alpha_{ij}$, the attention from source word $j$ to target word $i$ — effectively a learned word alignment nobody supervised.

## See Also

- [[Deep Learning]]
- [[Recurrent Neural Networks]]
- [[Convolutional Neural Networks]]
- [[Neural Networks]]
- [[CSCE 420]]
