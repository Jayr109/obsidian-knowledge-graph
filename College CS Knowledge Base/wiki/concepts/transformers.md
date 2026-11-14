---
title: "Transformers"
type: concept
tags: [csce420, csce421, transformers, self-attention, llm, qkv, attention, layer-normalization, positional-encoding, gpt, bert]
sources: [csce420-lecture-07-deep-learning, csce421-t10-attention-transformers-llms]
course: CSCE 420, CSCE 421
updated: 2026-10-20
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

---

# The CSCE 421 Treatment

The section above is the [[CSCE 420]] survey. [[CSCE 421 T10 — Attention, Transformers, and Large Language Models|T10]] derives the layer, following Chapter 12 of Bishop & Bishop's *Deep Learning: Foundations and Concepts* — note the textbook change from *Learning From Data*, which carried T01 through T07.

## The Layer

A transformer takes an $N \times D$ matrix and returns one of the same shape, so layers stack:

$$\tilde{X} = \mathrm{TransformerLayer}[X]$$

Two sub-blocks, each wrapped in a residual connection and a normalization:

$$Z = \mathrm{LayerNorm}\!\left[Y(X) + X\right] \qquad \tilde{X} = \mathrm{LayerNorm}\!\left[\mathrm{MLP}[Z] + Z\right]$$

where $Y(X)$ is multi-head self-attention. T10 also gives the **pre-norm** variants, which is what modern models use:

$$Z = Y\!\left(\mathrm{LayerNorm}[X]\right) + X \qquad \tilde{X} = \mathrm{MLP}\!\left[\mathrm{LayerNorm}[Z]\right] + Z$$

This is the same choice [[CNN Architectures]] reaches from the vision side — the ResNet identity-mappings study found pre-activation keeps the residual path clean, and [[CSCE 421 T09 — Convolutional Neural Networks|T09]] closes by pointing directly at *"Attention is all you need"* and GPT-2 for the same reason.

**Why LayerNorm and not BatchNorm:** layer normalization takes statistics per sample across features, so it has *"same behavior at train and test"* and no dependence on batch composition or sequence length. See [[Batch Normalization]].

## Why the MLP Is Not Optional

> The output vectors are **constrained to lie in the subspace spanned by the input vectors** and this limits the expressive capabilities of the attention layer.

Attention produces weighted *averages* of its inputs, so it can never leave their span no matter how many heads or layers. The MLP — *"a two-layer fully connected network with ReLU hidden units"* — breaks out of it. It is applied **separately and identically to every position** (*"the same shared network is applied to each of the output vectors"*), which is what preserves variable-length handling.

So a transformer layer is: **mix across positions** (attention), then **transform each position** (MLP). Neither alone suffices.

## Positional Encoding

Attention is permutation **equivariant** — permute the rows of $X$ and the rows of $\tilde{X}$ permute identically. T10's example of why that is fatal:

```
'The food was bad, not good at all.'
'The food was good, not bad at all.'
```

A position vector $r_n$ is combined with each token embedding. The four requirements: unique per position, bounded, generalizes to longer sequences, and a consistent encoding of the **distance** between positions, *"because the relative position of tokens is often more important than the absolute position."*

Mechanics of attention itself — Q/K/V, the $\sqrt{D_k}$ scaling, multi-head — are on [[Attention Mechanism]].

## Three Shapes

| Shape | Mapping | Example | Model |
|---|---|---|---|
| **Encoder only** | sequence to single value | sentiment analysis | BERT |
| **Decoder only** | vector to sequence | generation, captioning | GPT |
| **Encoder-Decoder** | sequence to sequence | translation | seq2seq |

**Decoder (GPT).** Autoregressive: $p(x_n \mid x_1,\dots,x_{n-1})$ expressed by a transformer, with output projected to the vocabulary by $Y = \mathrm{Softmax}[\tilde{X}W^{(p)}]$ and trained with [[Cross-Entropy Loss]] at every position. Two mechanisms stop it from cheating — the input is **shifted right by one**, and **causal (masked) attention** zeroes every weight pointing at a later token before renormalizing.

**Encoder (BERT).** *"Bidirectional encoder representations from transformers."* Roughly **15%** of tokens are replaced by `<mask>` and predicted; only the masked positions contribute to the loss. Being bidirectional, it needs no shifting or masking — and consequently **cannot generate sequences**.

**Encoder-decoder.** The decoder is conditioned on the encoded input through **cross attention**: queries from the sequence being generated, keys and values from the encoded source.

Where this goes next — pretraining, fine-tuning, LoRA, prompting — is on [[Large Language Models]].

## See Also

- [[Attention Mechanism]]
- [[Large Language Models]]
- [[Batch Normalization]]
- [[Deep Learning]]
- [[Recurrent Neural Networks]]
- [[Convolutional Neural Networks]]
- [[Neural Networks]]
- [[CSCE 420]]
- [[CSCE 421]]
