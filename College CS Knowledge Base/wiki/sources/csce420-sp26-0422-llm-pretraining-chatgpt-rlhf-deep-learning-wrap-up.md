---
title: "CSCE 420 Spring 2026 — 04-22 LLMs, Diffusion, Deep Learning Wrap-Up"
type: source
tags: [csce420, lecture-recording, spring-2026, pretraining, masked-language-model, next-sentence-prediction, glue, gpt-3, palm, chatgpt, rlhf, ppo, agentic-ai, gan, graph-neural-networks, transfer-learning, imitation-learning, optimizers, continual-learning, catastrophic-forgetting, adversarial, explainability, self-supervised, agi]
sources: []
course: CSCE 420
semester: Spring 2026
date: 2026-04-22
deck: slide07
exam: final
updated: 2026-09-17
---

Spring 2026 lecture, 47 min. How LLMs are pretrained on unlabelled text, the GLUE jump, GPT-3 (philosopherai), PaLM, ChatGPT's three-step RLHF, agentic AI, a survey of advanced deep-learning topics, limitations and their countermeasures, self-supervised vision, and open questions up to AGI. Slides 07:100–end. **Redefined Friday**: Tuesday 04-28 meets as a Friday class.

> **Exam-scope note.** He confirmed the remaining lectures would revisit **Self-Organizing Maps** — *"I won't put that on the exam, because I wasn't expecting to cover it"* — and then **AI Ethics**, also excluded. See [[CSCE 420 Final Review]].

## Pretraining on Unlabelled Text

Millions of documents (web, Wikipedia, scanned books) with **no labels**. Two ways to manufacture supervised pairs automatically:

| Task | Input | Target |
|---|---|---|
| **Masked language model** | a sentence with one or several words **masked out** | the original sentence |
| **Next-sentence prediction** | sentence 1 + sentence 2 | **true** if sentence 2 directly follows sentence 1 in the text, **false** if taken from elsewhere |

*"You can create hundreds of millions of such pairs just by looking at unlabelled documents."* The transformer *"learns some property about language,"* so a task-specific layer on top *"easily learns the task without having to learn the structure of the language."* Task heads recap: sentence-pair classification, single-sentence classification, QA span (start, end).

**GLUE benchmark**: average human ≈ 87; LSTM/RNN models ≈ 70; every transformer model (*"everything with a T"*) about **10 points above** the LSTM ones. ELMo is the lone LSTM entry.

## GPT-3, PaLM, ChatGPT

**GPT-3** — hundreds of billions of parameters; *"one of the first to show extremely high-quality text generation."* His first exposure was **philosopherai.com** (free during the GPT-3 API trial, later paid, now moot). He read its answer to *"Can consciousness survive after death?"* — it invoked Brazilian neuroscientist **Miguel Nicolelis** (real: the EEG-controlled exoskeleton kick at the 2014 World Cup opening) and a theory of consciousness as neurons projecting sensation onto the body. Second question: *"Is the universe fundamentally computational?"*

**PaLM** (Google, 2022): one model doing many things — cause/effect (*"I got an A because I studied hard"*), emoji → movie (🤖🪲🌱🌍 = WALL-E), synonym games, counterfactuals, concept definitions.

**ChatGPT — three steps (RLHF)**:
1. **Supervised fine-tuning**: humans write demonstrations of desired output for prompts → train GPT-3.5.
2. **Reward model**: for a prompt ("explain RL to a 6-year-old") the model generates candidates A–D; a human **ranks** them (D > C > A > B). *"Every human would write it differently — the feedback is too high-variance; ranking narrows it."* OpenAI hired hundreds of rankers.
3. **Policy optimization** with **PPO** (policy = state → action): the reward model scores outputs and trains the policy directly.

## Agentic AI (his addition to the slides)

Chat: you copy code out, run it, paste errors back. **Agents** (Claude Code, Codex, Gemini CLI): sit in VS Code or the terminal, read the codebase, fix, compile, run, read the error, fix again — *"you just say A or B and wait."* Orchestration harnesses coordinate multiple agents *"even while you sleep."* See [[Large Language Models]].

## Advanced Topics Survey

- **Generative**: DALL·E; **GANs** predate diffusion — style transfer, data augmentation, deepfakes.
- **Graph neural networks**: molecular fingerprinting, combinatorial optimization, social networks.
- **Deep RL**: meta-learning, **transfer learning** incl. **sim-to-real** (*"you can almost never use a simulator-trained model directly on a physical robot"*), multitask, **imitation learning** — guide the robot's hand instead of letting it explore unsafe behaviours.
- **Theory**: optimizers — online GD = SGD; **Adam**, RMSprop are flavours of gradient descent.
- **Engineering**: **continual learning** on streaming data vs. **catastrophic forgetting**; semi-supervised; **active learning** (the learner chooses what to sample); **federated learning**; **model compression and distillation** for phones.

## Limitations → Countermeasures

| Limitation | Countermeasure |
|---|---|
| massive labelled data | active learning, core sets, data augmentation, self-supervision |
| long/expensive training (*"millions of dollars in electricity"*) | core sets, compact models, compression, **distillation** |
| catastrophic forgetting | many partial fixes, *"no single solution"* |
| manual architecture design | AutoML, neural architecture search, evolutionary search |
| adversarial inputs | **adversarial training**, defensive distillation |
| explainability | DARPA **XAI** (~5 yrs ago), Bayesian program induction; **Anthropic's** emotion-vector work — scale an "anger" vector and the responses change |

Deeper issues: reasoning, common sense, causality (*"Can you put an elephant into a refrigerator?"*); the Wittgenstein **duck–rabbit** — a CNN answers deterministically, ChatGPT *"knows too much"* and cites Wittgenstein.

## Self-Supervised Learning, and Open Questions

Vision analogue of MLM: **3 previous video frames → predict the next frame**, pixel by pixel — infinite samples from unlabelled video; the model *"learns some property of the visual world."*

Open questions he listed: human-like learning (Harari: AI as **alien** intelligence — octopus analogy); meaning vs. embeddings (strong/weak AI, Chinese room); **problem posing** (agents inventing subgoals — "OpenClaw"-style harnesses); tool construction and use; **open-endedness**; **AGI** — once a fringe conference topic, now the stated goal of DeepMind and OpenAI.

## See Also

- [[CSCE 420 Spring 2026 — 04-20 LSTM Applications, Attention, Transformers]]
- [[CSCE 420 Spring 2026 — 04-24 Self-Organizing Maps (Not on Exam)]]
- [[Transformers]]
- [[Large Language Models]]
- [[CSCE 420 Lecture 7 — Deep Learning]]
- [[CSCE 420]]
