---
title: "Artificial Intelligence"
type: concept
tags: [csce420, artificial-intelligence, agents, definitions]
sources: [csce420-lecture-01-introduction]
course: CSCE 420
updated: 2026-08-25
---

Artificial Intelligence is the study of building machines that behave intelligently — but the field has never settled on one definition, because *intelligence* itself resists definition. Russell & Norvig organize the competing definitions along two axes (thought vs. behavior, human standard vs. rational standard), then commit to one: **"We define AI as the study of agents that receive percepts from the environment and perform actions."**

## The Four Textbook Definitions

|  | **Human standard** | **Rational standard** |
|---|---|---|
| **Thought** | Thinking like humans | Thinking rationally |
| **Behavior** | Acting like humans | Acting rationally |

R&N's agent-based definition sits in the *acting rationally* cell. The choice matters: it makes AI an engineering discipline with a measurable objective (does the agent act well given its percepts?) rather than a philosophical one about inner experience — which is exactly the divide between [[Strong AI and Weak AI]].

## Why Intelligence Is Hard to Define

Lecture 1 poses the question with a comparison: a math professor, a child, and Mathematica.

- The professor is better than the child at math, so we call the professor more intelligent.
- Mathematica is also better than the child at math — but almost nobody wants to say Mathematica is more intelligent than a child.

Competence at a task is therefore not the same as intelligence, and any single-task benchmark can be gamed by a system that has none of the general capacity we mean by the word.

## Why Not Just Engineer It?

An engineering analogy that Lecture 1 raises and then rejects: why not build AI the way people built airplanes?

| | Flight | Intelligence |
|---|---|---|
| Goal | Simple | Complex, hard to define clearly |
| Verification | You know when a thing is flying | Intelligence is a collection of many abilities |

There are many ways to meet a single clear goal, but only a small number of ways to simultaneously meet a huge number of unclearly defined goals. This is the argument for studying existing solutions — brains — rather than engineering from first principles. See [[Yoonsuck Choe]] for the insect-flight illustration of the same point.

## Subfields

The scope of AI as represented by AAAI (`aaai.org`): problem solving, reasoning, theorem proving, learning, planning, knowledge representation, perception and robotics, agents, and more recently deep learning and AI ethics.

## See Also

- [[Strong AI and Weak AI]]
- [[Turing Test]]
- [[History of AI]]
- [[Foundations of AI]]
- [[CSCE 420]]
