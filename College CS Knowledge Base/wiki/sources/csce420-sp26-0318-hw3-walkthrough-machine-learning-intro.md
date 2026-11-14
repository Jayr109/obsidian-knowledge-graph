---
title: "CSCE 420 Spring 2026 — 03-18 HW3 Walkthrough, Machine Learning Intro"
type: source
tags: [csce420, lecture-recording, spring-2026, hw3, resolution-prover, prolog, royalty, knowledge-engineering, machine-learning, supervised, unsupervised, reinforcement, ml-history]
sources: []
course: CSCE 420
semester: Spring 2026
date: 2026-03-18
deck: slide05, slide06
exam: final
updated: 2026-11-04
---

Spring 2026 lecture, 46 min (recording started late — *"I forgot to record"*). A walkthrough of Spring's HW3 — a propositional resolution prover in Python and a Prolog family-tree — then knowledge engineering and the opening of the machine-learning deck. Slides 05:67–70 and 06:1–14.

> **HW3 here is Spring 2026's.** The user's own sheet is [[CSCE 420 Homework 3 — FOL, Resolution Prover, Prolog]], which adds a written FOL proof and fixes the prover to the two-pointer method with set of support. Use this walkthrough for the design constraints, and the Fall page for what is actually asked.

## HW3 Part 1 — A Propositional Resolution Prover (Python)

**Representation**: a clause is a list of two lists — positive literals, negative literals. P ∨ Q ∨ ¬R → `[['P','Q'], ['R']]`. Clauses are numbered in an outer list.

**`resolve(c1, c2)` returns one of three things**, and telling them apart is the whole assignment:

| Case | Returns | Meaning |
|---|---|---|
| Exactly one complementary pair | the resolvent clause | success |
| Complementary pair, nothing else left | `[[], []]` — the **empty clause** | **logical False** — stop, theorem proved |
| Zero or **two or more** complementary pairs | Python `False` | **failure to resolve** — not a logical value |

*"P ∨ ¬Q and Q ∨ ¬P — can you resolve these? No, there are two complementary literals. Return False. But this False is not the logical false — this is failure."* `null_p` tests for the empty clause; `make_unique` collapses duplicate literals (P ∨ P ∨ Q = P ∨ Q) and had to be applied **before** resolving as well as after, a bug he fixed live. Another fix: **deep-copy** the arguments so resolving does not mutate the clause list.

**The critical requirement**: *"Before you add the resolvent, check if the same clause already exists in the clause list. If so, do not add it. The bad thing that can happen is an infinite loop."* Duplicate clauses may have literals in different order — compare as sets. *"Try disabling this check after your prover works; you'll observe it doesn't terminate."* This is [[Resolution Strategies|the deletion strategy]] made mandatory.

## HW3 Part 2 — Prolog, British Royalty

Facts first (male, female, spouse, parent), then ~12 relation rules. `mother(X,Y) :- female(X), parent(X,Y).` The trap: `brother(X,Y)` via a shared parent Z *"will flag you as the brother of yourself"* — add **`X \= Y`**. Comments start with `%`.

Domain rules stated: **parent = biological only** (Camilla is not a parent of William); **spouse includes divorced** (Diana and Camilla are both spouses of Charles); **grandparent tracks biological ancestry only**; **do not define helper predicates** like `divorced`. See [[Prolog]].

## Knowledge Engineering for Uncertain Reasoning

Decide what to model; choose the random variables and their value ranges; encode dependence as the graph (**qualitative**) and the CPTs (**quantitative**); pose queries; check **sensitivity** of results to CPT perturbations. Node ordering recap: *"if B actually causes A, you may have to point backward — but that's not allowed. So put causes in the node list earlier than what they affect."*

## Machine Learning — Framing

Tom Mitchell's definition: **improve performance in a task through experience.** *"You can memorize things and check if a situation falls in the memory pattern — all the way up to learning very complex strategies."*

| Type | Data | Feedback |
|---|---|---|
| **Supervised** | (input, target) pairs — labeled | **dense** |
| **Unsupervised** | inputs only — unlabeled | **none**; discover structure |
| **Reinforcement** | agent senses, acts, receives reward | **sparse and indirect** — and *"through your action you can also change the environment"* |

RL formalism: the **environment** implements the state-transition function δ(s, a) and the reward function ρ(s, a); *"these are only known to the environment — the agent doesn't have immediate knowledge of them."*

**Why ML**: fault tolerance (*"knock out some parameters, it'll still work — unlike any logic-based system"*), and no need for a complete algorithm — *"you can't write a language model from scratch line by line; you have to make it learn from data."* Dominant in AI since the mid-1990s; a data deluge from every sensor — *"your cell phone is a massive data-acquisition device."* The claim that there is not enough human expertise to analyze it *"has been seriously disrupted lately by generative AI."*

**Math needed**: linear algebra, calculus, probability, statistics; differential geometry for advanced work; and **numerical methods** for engineers — *"the ordering of matrix operations, even though mathematically identical, gives much different convergence behavior."*

## History Slides — His Gloss

IBM Watson beats the Jeopardy champions; Google's YouTube cat detector — *"trivial nowadays, but this was a big deal"*; DeepMind mid-2010s, deep RL on Atari 2600 → **AlphaGo** (*"a major blow to human ego"*) → AlphaStar, AlphaFold — *"some of that work led to a Nobel Prize in medicine"*; ChatGPT *"slightly less than 4 years ago"* fundamentally changed interaction; **2018 Turing Award** (given 2019) to Bengio, Hinton, LeCun; Hinton later a Nobel in Physics. See [[Machine Learning Paradigms]], [[Game AI Milestones]].

## Reading a Dataset Figure

Three coloured Gaussian clouds in (x, y, z): *"whenever you see something like this, think about the table"* — each point is a row (x, y, z, class). The **supervised** version is coloured; the **unsupervised** version is the same points uncoloured — *"but you can actually tell there are three clouds. How many clusters, and what is the prototype of each?"* Continues 03-20.

## See Also

- [[CSCE 420 Spring 2026 — 03-16 Belief Network Inference]]
- [[CSCE 420 Spring 2026 — 03-20 Supervised, Unsupervised, RL Issues]]
- [[CSCE 420 Lecture 6 — Machine Learning]]
- [[Machine Learning Paradigms]]
- [[CSCE 420]]
