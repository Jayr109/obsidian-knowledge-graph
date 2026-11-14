---
title: "Large Language Models"
type: concept
tags: [csce420, csce421, llm, lora, prompting, temperature, beam-search, n-gram, pretraining, masked-language-model, next-sentence-prediction, fine-tuning, rlhf, gpt, bert, agentic-ai]
sources: [csce421-t10-attention-transformers-llms, csce420-lecture-07-deep-learning, csce420-sp26-0420-lstm-applications-attention-transformers, csce420-sp26-0422-llm-pretraining-chatgpt-rlhf-deep-learning-wrap-up]
course: CSCE 420, CSCE 421
updated: 2026-10-20
---

A **large language model** is a [[Transformers|transformer]] with hundreds of billions of parameters, **pretrained on unlabelled text** and then adapted to tasks. The course's framing: the translation demo was not the important discovery — *"the real important thing is that you can train the internal mechanism using a very simple dataset that does not require any labelling, and then fine-tune it."*

## Pretraining Without Labels

Two ways to manufacture supervised pairs from raw documents (web, Wikipedia, books, code):

| Task | Input | Target |
|---|---|---|
| **Masked language model** | a sentence with one or more words masked | the original sentence |
| **Next-sentence prediction** | sentence 1, sentence 2 | true if 2 directly follows 1 in the text |

Hundreds of millions of such pairs cost nothing to label. The model learns the regularities of language, so a small task head — sentence-pair classification, spam detection, question-answering span (start, end) — trains quickly on top.

## Model Families

- **BERT** (Google) — encoder blocks attending in **both** directions.
- **GPT** (OpenAI) — attends only to **previous** positions; generates left to right.
- **ELMo** — the LSTM-based contender; ~10 GLUE points below the transformer models.
- **GPT-3** — first to show *"extremely high-quality text generation"*; **PaLM** (Google, 2022) — one model doing cause/effect, emoji puzzles, counterfactuals.

## From GPT-3 to ChatGPT: RLHF

1. **Supervised fine-tuning** on human-written demonstrations.
2. **Reward model**: humans **rank** several candidate outputs (D > C > A > B) — ranking has far lower variance than free-form writing.
3. **Policy optimization** with **PPO**: the reward model scores outputs and trains the policy (state → action) directly. See [[Deep Reinforcement Learning]].

## Generation Loop

At test time the decoder receives the prompt plus ⟨BOS⟩, emits a token, **feeds it back into itself**, and repeats until it emits ⟨EOS⟩.

## Agentic AI

The instructor's addition: chat models answer; **agents** (Claude Code, Codex, Gemini CLI) read a codebase, edit, compile, run, read the error, and iterate, with orchestration harnesses coordinating several agents. Also the source of his 2026 ethics concern — *"people are not sure any longer whether we can control it."* See [[AI Ethics]].

## Known Failure Modes

Training-data extraction (the "repeat *poem* forever" attack), bias, hallucinated reasoning, cost (*"millions of dollars in electricity"*), and explainability — see the limitations table in [[CSCE 420 Spring 2026 — 04-22 LLMs, Diffusion, Deep Learning Wrap-Up]].

---

# The CSCE 421 Treatment

The sections above are the [[CSCE 420]] survey. [[CSCE 421 T10 — Attention, Transformers, and Large Language Models|T10]] approaches the same material from the modelling side.

## What a Language Model Is

A distribution over sequences, factorized by the chain rule:

$$p(x_1,\dots,x_N) = \prod_{n=1}^{N} p(x_n \mid x_1,\dots,x_{n-1})$$

Estimating each factor by frequency counts fails because *"the size of these tables grows exponentially with the length of the sequence."* The classical fix is the **n-gram** approximation — truncate the history to the $L$ most recent tokens ($L=1$ bigram, $L=2$ trigram).

T10's arithmetic makes the failure vivid:

> A **3,001-gram model (like ChatGPT)** learns to predict the next word given the previous 3,000 words. When $|V| = 5k$, need $50{,}000^{3000}$ conditional distributions, with many zeros.
>
> **LLMs compress/approximate this gigantic table with a function.** Although LLMs have billions of parameters, they are **small compared to the size of table**.

That reframing is the useful one: an LLM is a **compressed approximation of an impossibly large probability table**, and its parameter count is small relative to what it approximates — not large.

> LLMs look at everything we say as a **prompt to be completed**.

## Generation and Sampling

The model outputs a distribution; turning it into text is a separate decision.

**Greedy search** takes the argmax at each step. T10 poses the trap as a question: *"simply choosing the highest probability token at each stage is not the same as selecting the highest probability sequence of tokens — why?"* Because the joint probability factorizes over the whole sequence, so a locally optimal token can force low-probability continuations.

**Beam search** keeps $B$ hypotheses, expands each by its $B$ best next tokens to give $B^2$ candidates, then prunes back to the $B$ best by total sequence probability.

**Temperature** addresses the fact that both *"limit the diversity of potential outputs"*:

$$y_i = \frac{\exp(a_i/T)}{\sum_j \exp(a_j/T)}$$

| $T$ | Effect |
|---|---|
| $T \to 0$ | mass concentrated on the most probable state — greedy |
| $T = 1$ | the unmodified softmax distribution |
| $T \to \infty$ | uniform across all states |
| $0 < T < 1$ | concentrated toward the higher values |

**Exposure bias**, stated as a challenge: *"during the learning phase the model is trained on a human-generated input sequence, whereas when it is running generatively the input sequence is itself generated from the model. This means that the model can drift away from the distribution of sequences seen during training."*

## Pretraining and Scale

> The number of compute operations required to train a state-of-the-art machine learning model has grown exponentially since about 2012 with a **doubling time of around 3.4 months**… The impressive increase in performance of the GPT series has come **primarily from an increase in scale**.

Training is **self-supervised** — each token is simultaneously a target for what precedes it and an input for what follows, so *"this self-labelling hugely expands the quantity of training data available."* No human annotation is required, which is what makes web-scale corpora usable.

## Fine-Tuning, Foundation Models, LoRA

> A large model is first **pre-trained using unlabelled data** and then **fine-tuned using supervised learning** on a much smaller set of labelled data. A model with broad capabilities that can subsequently be fine-tuned for specific tasks is called a **foundation model**.

Structurally this is [[Transfer Learning]] from [[CSCE 421 T09 — Convolutional Neural Networks|T09]], in a different domain.

**LoRA** (low-rank adaptation) rests on the observation that *"changes in the model parameters during fine-tuning lie on a manifold whose dimensionality is much smaller than the total number of learnable parameters."* Freeze $W_0$ of shape $D \times D$ and train a parallel low-rank product:

$$\text{layer output} = XW_0 + XAB, \qquad A: D\times R,\; B: R\times D$$

$AB$ has $2RD$ parameters against $D^2$ in $W_0$, so $R \ll D$ is a large saving. Afterwards the update folds back in, $\hat{W} = W_0 + AB$, so **there is no additional inference overhead**.

## Emergent Properties and Prompting

Given `English: the cat sat on the mat. French:` an autoregressive model continues with the translation — *"the model was not trained specifically to do translation but has learned to do so as a result of being trained on a vast corpus of data that includes multiple languages."*

Hence **prompting**: *"by using different prompts, the same trained neural network may be capable of solving a broad range of tasks,"* giving rise to **prompt engineering** and **few-shot learning**, where examples supplied inside the prompt adapt behaviour *"without needing to adapt the parameters of the model."*

T10 points to Minaee et al., *Large Language Models: A Survey* (arXiv:2402.06196) for more.

## See Also

- [[Transformers]]
- [[Attention Mechanism]]
- [[Transfer Learning]]
- [[CSCE 421]]
- [[Autoencoders]]
- [[Deep Learning]]
- [[AI Ethics]]
- [[CSCE 420 Lecture 7 — Deep Learning]]
