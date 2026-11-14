---
title: "CSCE 420 Spring 2026 — 04-20 LSTM Applications, Attention, Transformers"
type: source
tags: [csce420, lecture-recording, spring-2026, lstm, sequence-classification, seq2seq, encoder-decoder, handwriting-generation, attention, bahdanau, alignment, speech-recognition, gnmt, transformers, positional-encoding, multi-head-attention, self-attention, query-key-value, softmax, bert, gpt, elmo, pretraining, fine-tuning]
sources: []
course: CSCE 420
semester: Spring 2026
date: 2026-04-20
deck: slide07
exam: final
updated: 2026-09-17
---

Spring 2026 lecture, 50 min. LSTM recap and applications (classification, seq2seq translation, handwriting generation), the attention mechanism and its alignment matrices, deep learning's impact on speech and Google NMT, then transformers: architecture, scaled dot-product self-attention worked on "je suis étudiant," the training/testing loop, and BERT/GPT/ELMo with pretrain-then-fine-tune. Slides 07:75–100. Course evaluations opened.

## LSTM Recap

Vanilla RNN carries **one** thing across steps — its own output. LSTM carries **two**: the output line and the **memory line C**, and the gates control whether input is written, memory kept or modified, output released. All gate weights and the memory weight are learned by backprop; gates *"open and close based on ongoing activity and what you have observed in the past… known implicitly, just from the error signal."*

## Applications

- **Sequence classification**: feed tokens of any length, then an **end token**; the network emits spam / not-spam. No error → nothing learned; error → backprop through the whole unrolled chain.
- **Sequence translation (seq2seq)**: feed the English sentence token by token; after the end token, generate French tokens — and **each generated token is fed back as input** to condition the next. Compare against the target sentence, backprop.
- **Handwriting generation**: predict the next (x, y) pen coordinate from the previous ones; seeded with a few points it continues the stroke; train on a different scribe for a different style. Side trip into **Russian cursive** (л, и, ш chained into indistinguishable loops). More useful when **conditioned** on the text you want written.

## Attention (Bahdanau, Cho, Bengio — Chorowski et al.)

Kyunghyun Cho is the NYU professor he met on the recent trip.

**Problem**: the encoder squeezes the whole source into the **single last hidden vector**; for long inputs *"it would forget a lot about things that went in the past."*

**Idea**: keep **every** encoder hidden vector and let the decoder use a **weighted sum** of them, with weights from a small feed-forward **attention network** that looks at the encoder states **and the current decoding state** — so attention differs for each output token. *"Where should I look at in the input sequence? You don't need to tell it"* — trained by the same gradient descent.

**Alignment matrices**: English→French, generating *zone* (area) for "the agreement on the European Economic Area": French reverses "European Economic Area," so the position-matched English word would be *European* — wrong — but the learned weights are low/medium/**high** on *Area*. Same for *marine environment* → *environnement marin*. *"The attention is correctly identifying"* the reversed word.

## Impact Plots

**Speech recognition** word-error rate: very high in the early 1990s → **HMM**s brought it to ~14–15% → a decade-long plateau → deep RNNs/LSTM dropped it sharply (~15 years ago; lower now).

**Google Neural Machine Translation (~2016)**: phrase-based vs. GNMT vs. human. English↔Spanish and English↔French: GNMT close to human; English↔Chinese much harder for both, with phrase-based *"seriously lagging."* English→X is slightly easier than X→English for both. Chinese→English attention animation: identical word order, so attention marches diagonally. Production GNMT: stacked LSTM layers across multiple GPUs, encoder embeddings into attention, decoder stack, softmax output.

## Transformers

Recurrence is hard to parallelize — *"information goes back and forth."* Replace it with a **massive feed-forward network** over the entire context at once.

**Architecture**: encoder and decoder stacks, all flowing one way. Input embedding + **positional encoding** (supplies relative position, since nothing is sequential any more). Encoder block = **multi-head attention** → feed-forward. Decoder block = masked multi-head attention → multi-head attention **taking the encoder's output** → feed-forward. Attention takes three lines: **value, key, query** — *"a mixture of the value, where key–query match decides which part of the input is emphasized."* In the encoder→decoder attention, **K and V come from the encoder (source side), Q from the decoding state (target side).**

### Scaled dot-product self-attention, worked ("je suis étudiant")

1. Each input x_i is linearly mapped to **q_i, k_i, v_i** by trainable **W_Q, W_K, W_V** (*"how to generate query, key and value is automatically learned"*).
2. Score q₁ against every key: q₁·k₁ high (e.g. 112), q₁·k₂ lower (96).
3. Scale, **softmax** → weights that behave like probabilities (0.88, 0.12).
4. **z₁ = 0.88·v₁ + 0.12·v₂** — a mixture of the value vectors.
5. Repeat with q₂ for z₂.

So z₁ *"contains information not only about itself but also about different words."* Example: in "I am a student," *I* and *student* refer to the same person, and the transformer *"somehow mysteriously learns"* to make q_I and k_student similar. **Multi-head** = several attention sets in parallel, each *"looking at different aspects."*

### Training and testing loop

Train ("the cute dog" → "le chien mignon"): encode the full source → K, V. Decoder starts with **⟨BOS⟩** → Q; predicts *le*; error → gradient step. Then ⟨BOS⟩ *le* → *chien*, and so on. Test: feed any English sentence and ⟨BOS⟩; the decoder emits a token, **feeds it back into itself**, emits the next… until it emits **⟨EOS⟩**, which terminates. (Microphone died mid-explanation; recovered.)

## BERT, GPT, ELMo — Pretrain Then Fine-Tune

**BERT** (Google): transformer blocks attending **both directions**. **GPT** (OpenAI): attends only to **previous** outputs. **ELMo**: the LSTM-based contender of that era. All feed-forward except ELMo.

*"The real important realization"*: pretrain the internal mechanism on a **huge unlabelled corpus** (Wikipedia, GitHub) so it learns the regularities of language, then **fine-tune** briefly on the task — no retraining the whole model per task. Task heads: sentence-pair classification (same meaning across languages?), single-sentence classification (spam?), **question answering** (given paragraph + question, output the **start and end positions** of the answer span). See [[Transformers]] and [[Large Language Models]].

## See Also

- [[CSCE 420 Spring 2026 — 04-17 DQN Finished, Recurrent Networks and LSTM]]
- [[CSCE 420 Spring 2026 — 04-22 LLMs, Diffusion, Deep Learning Wrap-Up]]
- [[Recurrent Neural Networks]]
- [[Transformers]]
- [[CSCE 420 Lecture 7 — Deep Learning]]
- [[CSCE 420]]
