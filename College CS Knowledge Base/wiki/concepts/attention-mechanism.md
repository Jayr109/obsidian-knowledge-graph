---
title: "Attention Mechanism"
type: concept
tags: [csce421, attention, self-attention, cross-attention, qkv, multi-head, scaled-dot-product, positional-encoding]
sources: [csce421-t10-attention-transformers-llms]
course: CSCE 421
updated: 2026-10-20
---

Attention computes each output as a weighted average of all inputs, where **the weights are computed from the data itself** rather than learned and frozen. [[CSCE 421 T10 — Attention, Transformers, and Large Language Models|T10]] states the contrast that defines it:

> In a standard neural network, **the weights are fixed once the network is trained**. Attention uses **weights whose values depend on the specific input data**.

Every model from T01 through T09 multiplies activations by fixed weights at inference. Attention does not — and that is the entire novelty.

## The Motivating Example

```
I swam across the river to get to the other bank.
I walked across the road to get cash from the bank.
```

> Appropriate interpretation of 'bank' relies on **other words from the rest of the sequence**. The particular locations that should receive more attention **depend on the input sequence itself**.

No fixed weight matrix can encode "look at *river* when disambiguating *bank*," because which word matters changes from sentence to sentence.

## Attention Coefficients

Map tokens $x_1,\dots,x_N$ to outputs $y_1,\dots,y_N$ where each output is a weighted combination of **all** inputs:

$$y_n = \sum_{m=1}^{N} a_{nm}\,x_m, \qquad a_{nm} \ge 0, \quad \sum_{m=1}^{N} a_{nm} = 1$$

The two constraints make it an **average** rather than an arbitrary linear map. They are enforced the obvious way — by a [[Softmax Function|softmax]]:

$$a_{nm} = \frac{\exp(x_n^T x_m)}{\sum_{i=1}^{N}\exp(x_n^T x_i)}, \qquad \mathbf{a}_n = \mathrm{Softmax}\!\left([x_n^Tx_1,\; \dots,\; x_n^Tx_N]\right)$$

The dot product $x_n^T x_m$ is a **similarity score** — tokens pointing in similar directions attend to each other. Note *"we have a different set of coefficients for each output vector"*, so this is $N$ separate softmaxes, one per row.

## Query, Key, Value

The general form separates three roles:

$$Y = \mathrm{Softmax}\!\left[QK^T\right]V$$

where Softmax normalizes **each row independently**. The intuition: a **query** asks what it is looking for, a **key** advertises what each position offers, the match between them sets the weight, and the **value** is what actually gets mixed into the output.

## Self-Attention

**Without parameters** — use the same matrix for all three roles:

$$Y = \mathrm{Softmax}\!\left[XX^T\right]X$$

> This process is called **self-attention** because we are using the same sequence to determine the queries, keys, and values. **The transformation is fixed and has no capacity to learn.**

**With parameters** — project $X$ three ways first:

$$Q = XW^{(q)}, \qquad K = XW^{(k)}, \qquad V = XW^{(v)}$$

In single-head self-attention those three matrices are the entire set of learnable parameters; multi-head adds the output projection $W^{(o)}$ below. T10 notes that setting $D_v = D$ *"will facilitate the inclusion of residual connections"* — the output must match the input shape to be added back.

**Cross-attention** is the same machinery with the queries coming from one sequence and the keys and values from another. In translation, *"the query vectors come from the sequence being generated… the key and value vectors come from the sequence represented by $Z$."*

## Scaled Dot-Product

$$Y = \mathrm{Attention}(Q,K,V) = \mathrm{Softmax}\!\left[\frac{QK^T}{\sqrt{D_k}}\right]V$$

T10 justifies the $\sqrt{D_k}$ rather than asserting it:

> $\dfrac{\partial p_i}{\partial a_j} = p_i(\delta_{ij}-p_j)$: **small for inputs of high magnitude**.
>
> If the elements of the query and key vectors were all independent random numbers with **zero mean and unit variance**, then the **variance of the dot product would be $D_k$**. Normalize using the standard deviation.

That derivative is the **softmax Jacobian** derived in the [[CSCE 421 T03 Notes — Softmax Regression Derivations|T03 notes]]. Large dot products saturate the softmax, flattening its gradient — the same saturation problem as in [[Activation Functions]], arriving by a different route. Since the dot product of two $D_k$-dimensional unit-variance vectors has variance $D_k$, dividing by $\sqrt{D_k}$ restores unit variance and keeps the softmax in its responsive region.

## Multi-Head Attention

One set of $Q,K,V$ projections can only express one notion of relevance. Multi-head runs $H$ of them in parallel:

$$H_h = \mathrm{Attention}(Q_h,K_h,V_h), \qquad Q_h = XW_h^{(q)},\; K_h = XW_h^{(k)},\; V_h = XW_h^{(v)}$$

$$Y(X) = \mathrm{Concat}[H_1,\dots,H_H]\,W^{(o)}$$

> Typically $D_v$ is chosen to be equal to $D/H$ so that the resulting concatenated matrix has dimension $N \times D$.

So the cost is roughly constant in $H$ — the heads split the dimensionality rather than multiplying it. Concat gives $N \times HD_v$, and $W^{(o)}$ of shape $HD_v \times D$ brings it back.

## Two Structural Limitations

Attention alone is not enough, and T10 is explicit about why.

**It cannot leave the span of its inputs.** *"The output vectors are constrained to lie in the subspace spanned by the input vectors and this limits the expressive capabilities of the attention layer."* Since $y_n$ is a weighted average of the $x_m$, no combination escapes their span. The fix is an **MLP** applied identically to each position — which is why a [[Transformers|transformer]] layer is attention *plus* a feed-forward network.

**It is permutation equivariant.** Permuting the input rows permutes the output rows and changes nothing else — attention has no notion of order. For language this is fatal:

```
'The food was bad, not good at all.'
'The food was good, not bad at all.'
```

The fix is **positional encoding**: a vector $r_n$ attached to each position. T10's four requirements — unique per position, bounded, generalizes to longer sequences, and *"a consistent way to express the number of steps between any two input vectors irrespective of their absolute position, because the relative position of tokens is often more important than the absolute position."*

## See Also

- [[Transformers]]
- [[Large Language Models]]
- [[Softmax Function]]
- [[Batch Normalization]]
- [[Deep Learning]]
- [[CSCE 421]]
