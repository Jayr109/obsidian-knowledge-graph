---
title: "CSCE 421 T10 — Attention, Transformers, and Large Language Models"
type: source
tags: [lecture, csce421, attention, self-attention, transformers, llm, gpt, bert, lora, positional-encoding]
sources: []
course: CSCE 421
updated: 2026-10-20
---

Topic deck 10 of [[CSCE 421]], by [[Shuiwang Ji]], *"based on Chapter 12 of Deep Learning: Foundations and Concepts"* (Bishop & Bishop). 41 slides. Note the textbook change — T01 through T07 came from *Learning From Data*; this deck switches sources. It builds [[Attention Mechanism|attention]] from scratch, assembles the [[Transformers|transformer layer]], then covers decoder/encoder/seq2seq variants and [[Large Language Models]].

## Why Attention (slide 3)

The motivating pair:

```
I swam across the river to get to the other bank.
I walked across the road to get cash from the bank.
```

> Appropriate interpretation of 'bank' relies on **other words from the rest of the sequence**. The particular locations that should receive more attention **depend on the input sequence itself**.
>
> In a standard neural network, **the weights are fixed once the network is trained**. Attention uses **weights whose values depend on the specific input data**.

That contrast is the thesis of the deck. Every model from T01 to T09 has fixed weights at inference; attention computes its mixing coefficients from the input at run time.

## Word Embedding (slide 4)

One-hot vectors of dictionary size `K` are mapped into a `D`-dimensional embedding space by a matrix `E` of size `D x K`:

```
v_n = E x_n
```

> Word embeddings can be viewed as the **first layer in a deep neural network**. They can be fixed using some standard pre-trained embedding matrix, or they can be trained.

## Transformer Processing (slide 5)

Input is a **set** of `N` vectors of dimensionality `D`, stacked into a matrix `X` of shape `N x D` where row `n` is the token vector `x_n^T`. A transformer maps it to a matrix of the same shape:

```
X_tilde = TransformerLayer[X]
```

Same shape in and out — which is what lets layers stack and residual connections work.

## Attention Coefficients (slide 6)

Each output is a **weighted average of all inputs**:

```
y_n = sum_{m=1}^{N} a_nm x_m        with   a_nm >= 0  and  sum_m a_nm = 1
```

The constraints are what make it an average rather than an arbitrary linear map. The commonly used coefficients come from a softmax over dot products:

```
a_nm = exp(x_n^T x_m) / sum_{i=1}^{N} exp(x_n^T x_i)

a_n = Softmax( [x_n^T x_1, x_n^T x_2, ..., x_n^T x_N] )
```

> We have a **different set of coefficients for each output vector** `y_n`.

The dot product `x_n^T x_m` is a similarity score — tokens that point in similar directions attend to each other.

## General Attention, Q/K/V (slides 7–8)

Query, key and value vectors as rows of matrices `Q`, `K`, `V`:

```
Y = Softmax[ Q K^T ] V
```

> where `Softmax[L]` takes the exponential of every element of `L` and then **normalizes each row independently** to sum to one.
>
> Whereas standard networks multiply activations by **fixed weights**, here the activations are multiplied by **data-dependent attention coefficients**.

## Self-Attention (slides 9–10)

**Without parameters** — use `X` for all three roles:

```
Y = Softmax[ X X^T ] X
```

> This process is called **self-attention** because we are using the same sequence to determine the queries, keys, and values. **The transformation is fixed and has no capacity to learn.**

**With parameters** — project `X` three ways first:

```
Q = X W_q   in R^(N x Dk)
K = X W_k   in R^(N x Dk)
V = X W_v   in R^(N x Dv)
```

> `Dv` governs the dimensionality of the output vectors. Setting `Dv = D` will facilitate the inclusion of **residual connections**.

Those three weight matrices are the only learnable parameters in an attention layer.

## Scaled Dot-Product Attention (slide 12)

The justification for the `sqrt(Dk)` is given rather than asserted:

```
d p_i / d a_j = p_i (delta_ij - p_j)      "small for inputs of high magnitude"
```

> If the elements of the query and key vectors were all **independent random numbers with zero mean and unit variance**, then the **variance of the dot product would be `Dk`**. Normalize using the standard deviation.

```
Y = Attention(Q, K, V) = Softmax[ Q K^T / sqrt(Dk) ] V
```

Note that the derivative shown is the **softmax Jacobian** `p_i(delta_ij - p_j)` — the same object derived in the [[CSCE 421 T03 Notes — Softmax Regression Derivations|T03 notes]]. Large-magnitude inputs saturate the softmax and flatten its gradient, which is the problem the scaling prevents.

The pipeline on the slide: `X -> {W_q, W_k, W_v} -> {Q, K, V} -> mat mul -> scale -> softmax -> mat mul -> Y`.

## Multi-Head Attention (slides 13–14)

```
H_h = Attention(Q_h, K_h, V_h)     for h = 1..H
Q_h = X W_q_h,   K_h = X W_k_h,   V_h = X W_v_h

Y(X) = Concat[H_1, ..., H_H] W_o
```

> Typically `Dv` is chosen to be equal to `D/H` so that the resulting concatenated matrix has dimension `N x D`.

Shapes: concat gives `N x H*Dv`, then `W_o` of shape `H*Dv x D` brings it back to `N x D`.

## Transformer Layers (slides 15–17)

> Stack multiple self-attention layers on top of each other. Introduce **residual connections** and require the output dimensionality to be the same as the input dimensionality, namely `N x D`. Followed by **layer normalization** to improve training efficiency.

```
Z = LayerNorm[ Y(X) + X ]                    (post-norm)

Z = Y( LayerNorm[X] ) + X                    (pre-norm)
```

Both forms are given — the pre-norm variant is exactly what [[CSCE 421 T09 — Convolutional Neural Networks|T09]] slide 127 flagged as carrying over from the ResNet identity-mappings study.

**Why an MLP is needed** (slide 16):

> The output vectors are **constrained to lie in the subspace spanned by the input vectors** and this limits the expressive capabilities of the attention layer.

Because `y_n` is a weighted *average* of the inputs, attention alone can never leave their span. The fix: *"a standard nonlinear neural network with D inputs and D outputs… a two-layer fully connected network with ReLU hidden units,"* applied **separately and identically to each row** — *"the same shared network is applied to each of the output vectors"* — which is what preserves variable-length sequence handling.

```
X_tilde = LayerNorm[ MLP[Z] + Z ]            (post-norm)
X_tilde = MLP[ LayerNorm[Z] ] + Z            (pre-norm)
```

## Positional Encoding (slide 18)

> The transformer has the property that **permuting the order of the input tokens results in the same permutation of the rows of the output** — equivariance.

Which is fatal for language:

```
'The food was bad, not good at all.'
'The food was good, not bad at all.'
```

Same multiset of tokens, opposite meaning. The fix is a position vector `r_n` combined with each token embedding `x_n`. The four stated requirements for a good encoding:

> unique representation for each position · bounded · generalizes to longer sequences · a **consistent way to express the number of steps between any two input vectors** irrespective of absolute position, because **relative position is often more important than absolute position**

## Language Models, Narrow Sense (slides 19–20)

```
p(x_1, ..., x_N) = prod_{n=1}^{N} p(x_n | x_1, ..., x_{n-1})
```

Estimating each term by frequency counts fails because *"the size of these tables grows exponentially with the length of the sequence."* The n-gram approximation truncates the history to the `L` most recent words (`L=1` bi-gram, `L=2` tri-gram).

The slide's arithmetic, credited to R. Kambhampati:

> A **3,001-gram model (like ChatGPT)** learns to predict the next word given the previous 3,000 words. When `|V| = 5k`, need `50,000^3000` conditional distributions, with many zeros.
>
> **LLMs compress/approximate this gigantic table with a function.** Although LLMs have billions of parameters, they are **small compared to the size of table**.
>
> LLMs look at everything we say as a **prompt to be completed**.

## Three Model Shapes (slide 21)

| Shape | Input to output | Example |
|---|---|---|
| **Encoder only** | sequence to single value | sentiment analysis |
| **Decoder only** | single vector to sequence | image captioning, generation |
| **Encoder-Decoder** | sequence to sequence | translation |

## Decoder Transformers / GPT (slides 22–29)

> **GPT** stands for **generative pretrained transformer**… an **autoregressive** model in which the conditional distributions `p(x_n | x_1,...,x_{n-1})` are expressed using a transformer.

Output projection to vocabulary (slide 23):

```
Y = Softmax[ X_tilde W_p ]          W_p of shape D x K
```

> Each softmax output unit has an associated **cross-entropy error function**.

That is the same loss from [[CSCE 421 T03 — Logistic Regression: From Binary to Multi-Class|T03]], applied once per position.

**Concurrent processing** (slide 24): training is self-supervised on unlabeled text, and an entire sequence is processed at once so *"each token acts both as a target value for the sequence of previous tokens and as an input value for subsequent tokens."* The constraint: *"ensure that the network is not able to 'cheat' by looking ahead in the sequence."*

**Causal masking** (slide 25), two mechanisms:

> First, **shift the input sequence to the right by one step**, so that input `x_n` corresponds to output `y_{n+1}`, with target `x_{n+1}`.
>
> Second, use **causal (masked) attention**, in which we set to zero all of the attention weights that correspond to a token attending to any **later** token, and then normalize the remaining elements.

**Training vs generation** (slide 27):

> Training: the next token is **given**, so it is a multi-class prediction problem using cross-entropy loss.
> Generation: **sample** a token based on the computed probability, and use it as input to compute the next.
>
> Challenge: during learning the model is trained on a **human-generated** input sequence, whereas when running generatively the input sequence is **itself generated from the model** — the model can **drift away from the distribution** seen during training.

**Sampling strategies** (slides 28–29):

- **Greedy search** — highest-probability token at each step, deterministic. The slide poses the trap: *"simply choosing the highest probability token at each stage is not the same as selecting the highest probability sequence of tokens — why?"* Because the joint probability factorizes over the whole sequence, a locally best token can force low-probability continuations.
- **Beam search** — keep `B` hypotheses, expand each to its `B` best next tokens giving `B^2` candidates, prune back to the `B` most probable overall.
- **Temperature** — both greedy and beam *"limit the diversity of potential outputs"*:

```
y_i = exp(a_i / T) / sum_j exp(a_j / T)

T -> 0    probability mass concentrated on the most probable state (greedy)
T  = 1    the unmodified softmax distribution
T -> inf  uniform across all states
0 < T < 1 probability concentrated towards the higher values
```

## Encoder Transformers / BERT (slides 30–31)

> **BERT** stands for **bidirectional encoder representations from transformers**. A randomly chosen subset of the tokens, **say 15%**, are replaced with a special `<mask>` token. The model is trained to predict the missing tokens.

```
I <mask> across the river to get to the <mask> bank.
```

> The network should predict 'swam' at output node 2 and 'other' at output node 10. **Only two of the outputs contribute to the error function** and the other outputs are ignored.
>
> BERT is bidirectional, so **no need to shift inputs and mask outputs**. An encoder model is **unable to generate sequences**.

## Sequence-to-Sequence (slides 32–34)

Translation conditions a decoder on an encoded input `Z`, joined by **cross attention**:

> The **query vectors come from the sequence being generated** (the Dutch output), the **key and value vectors come from the sequence represented by Z** (the English input).

That asymmetry is the one-line definition of cross attention versus self attention.

## Large Language Models (slides 35–39)

**Pretraining** (35):

> The number of compute operations required to train a state-of-the-art machine learning model has grown exponentially since about 2012 with a **doubling time of around 3.4 months**… The impressive increase in performance of the GPT series has come **primarily from an increase in scale**.

**Fine-tuning and foundation models** (36):

> A large model is first **pre-trained using unlabelled data** and then **fine-tuned using supervised learning** on a much smaller set of labelled data. A model with broad capabilities that can subsequently be fine-tuned for specific tasks is called a **foundation model**.

**LoRA** (36–37) — low-rank adaptation:

> Changes in the model parameters during fine-tuning lie on a manifold whose **dimensionality is much smaller** than the total number of learnable parameters.

```
layer output:  X W_0 + X A B          W_0: D x D,  A: D x R,  B: R x D

parameters in AB = 2RD    versus    D^2 in W_0        so R << D is a large saving

after fine-tuning:   W_hat = W_0 + A B     ->  no additional inference overhead
```

**Emergent properties** (38): given `English: the cat sat on the mat. French:` an autoregressive model continues with the translation. *"The model was not trained specifically to do translation but has learned to do so as a result of being trained on a vast corpus."*

**Prompting** (39): *"the sequence of input tokens given by the user is called a prompt… leading to a new field called prompt engineering,"* allowing new tasks *"without needing to adapt the parameters of the model. This is an example of few-shot learning."*

Slide 40 points to Minaee et al., *Large Language Models: A Survey*, arXiv:2402.06196.

## See Also

- [[Attention Mechanism]]
- [[Transformers]]
- [[Large Language Models]]
- [[Batch Normalization]]
- [[Softmax Function]]
- [[Cross-Entropy Loss]]
- [[Deep Learning]]
- [[CSCE 421]]
- [[Shuiwang Ji]]
