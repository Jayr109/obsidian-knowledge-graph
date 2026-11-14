---
title: "CSCE 420"
type: course
tags: [csce420, artificial-intelligence, course]
sources: [csce420-lecture-01-introduction, csce420-midterm-practice, csce420-final-practice, csce420-lecture-02-search-and-game-playing, csce420-lecture-03-logic, csce420-lecture-04-planning, csce420-lecture-05-probabilistic-reasoning, csce420-lecture-06-machine-learning, csce420-lecture-07-deep-learning, csce420-lecture-08-ai-ethics, csce420-som-notebook, csce420-midterm-review, csce420-final-review, csce420-homework-1-search, csce420-homework-2-game-playing-logic, csce420-homework-3-fol-resolution-prover-prolog, csce420-homework-4-probability-learning-deep-learning, csce420-homework-1-solutions, csce420-homework-2-solutions, csce420-fall2025-midterm-review-recording, csce420-fall2025-whiteboard-perceptron-decision-line, csce420-demo-rejection-method, csce420-sp26-0112-syllabus-what-is-intelligence, csce420-sp26-0114-linguistics-neuroscience-history-of-ai, csce420-sp26-0116-modern-ai-limitations-future, csce420-sp26-0121-uninformed-search, csce420-sp26-0123-dfs-dls-ids-informed-intro, csce420-sp26-0128-greedy-astar-heuristics, csce420-sp26-0130-ida-star-iterative-improvement, csce420-sp26-0202-simulated-annealing-csp-game-playing, csce420-sp26-0204-alpha-beta-pruning, csce420-sp26-0206-chance-games-game-ai-history-logic-intro, csce420-sp26-0209-knowledge-bases-propositional-logic, csce420-sp26-0211-normal-forms-logical-consequence-resolution, csce420-sp26-0213-hw2-walkthrough-first-order-logic, csce420-sp26-0216-standard-form-skolemization, csce420-sp26-0218-composition-unification-factors, csce420-sp26-0220-fol-resolution-strategies, csce420-sp26-0223-cheat-sheet-rules-prover-demo-prolog, csce420-sp26-0225-planning, csce420-sp26-0227-exam-rules-practice-walkthrough-frame-problem-uncertainty, csce420-sp26-0302-probability-bayes-rule, csce420-sp26-0304-midterm-review-bayesian-updating-belief-networks, csce420-sp26-0316-belief-network-inference, csce420-sp26-0318-hw3-walkthrough-machine-learning-intro, csce420-sp26-0320-supervised-unsupervised-rl-issues, csce420-sp26-0323-decision-trees-entropy, csce420-sp26-0325-information-gain-neural-networks-intro, csce420-sp26-0330-perceptron-recap-gradient-descent-backprop, csce420-sp26-0331-backprop-ii-recorded-lecture, csce420-sp26-0406-demos-autoencoders-srn-genetic-algorithms, csce420-sp26-0408-hw4-walkthrough-genetic-algorithms-neuroevolution, csce420-sp26-0410-neat-demos-deep-learning-intro, csce420-sp26-0413-final-practice-walkthrough-deep-cnns-alexnet, csce420-sp26-0415-final-review-cnn-representations-deep-rl-dqn, csce420-sp26-0417-dqn-finished-recurrent-networks-lstm, csce420-sp26-0420-lstm-applications-attention-transformers, csce420-sp26-0422-llm-pretraining-chatgpt-rlhf-deep-learning-wrap-up, csce420-sp26-0424-self-organizing-maps-not-on-exam, csce420-sp26-0427-som-evaluation-ai-ethics-not-on-exam, csce420-fall2026-0918-minmax-notebook-walkthrough]
course: CSCE 420
updated: 2026-11-04
---

CSCE 420 (Artificial Intelligence) is Texas A&M's undergraduate survey of AI, taught by [[Yoonsuck Choe]]. The course runs the classical-to-modern arc: it opens with what intelligence is and how AI relates to philosophy, psychology, and neuroscience; moves through search, logic, and probabilistic reasoning; and closes with machine learning and deep learning. The main textbook is Russell & Norvig, *Artificial Intelligence: A Modern Approach* (4th ed.; 3rd is acceptable), with Brighton & Selina's *Introducing Artificial Intelligence: A Graphic Guide* as an optional companion for the philosophical material.

## Logistics

- **Instructor:** [[Yoonsuck Choe]]
- **Communications:** email registered on `email.tamu.edu` plus Canvas announcements
- **Class notes:** posted to Canvas 24 hours before each class
- **Syllabus:** on Canvas and Howdy

## Textbooks

| Role | Text |
|------|------|
| Required | Russell & Norvig (R&N), *Artificial Intelligence: A Modern Approach*, 4th ed. (3rd ed. okay) |
| Optional | Brighton & Selina (B&S), *Introducing Artificial Intelligence: A Graphic Guide* — AI overview including philosophical issues |

## Topic Arc

The two practice exams map the course into two halves.

**First half (midterm):** philosophy and framing ([[Strong AI and Weak AI]]), then search — [[Heuristic Search]] and [[A* Search]]/[[IDA*]], [[Local Search]] and [[Simulated Annealing]], [[Constraint Satisfaction Problems]], and [[Adversarial Search]] with [[Minimax]], [[Alpha-Beta Pruning]], and [[Expectimax]] — then logic: [[Logical Inference]] by [[Resolution]], [[Unification]], and [[First-Order Logic]] with skolemization.

**Second half (final):** first-order [[Resolution]] again, [[Situation Calculus]], [[Bayesian Networks]], [[Decision Tree Learning]], [[Neural Networks]] and expressiveness, [[Self-Organizing Map]], and [[Deep Learning]] including [[Deep Q-Network]].

## Exam Format

**Scope is the thing to get right.** The two exams are disjoint; the review pages are deliberately kept separate so that a midterm question never draws on final material:

| | Midterm | Final |
|---|---|---|
| Scope | Deck 1 (one question) + Deck 2 + Deck 3 **through unification** (slide 99) | everything after the midterm; **not cumulative** |
| Excluded | — | Self-Organizing Maps; AI Ethics |
| Guaranteed | — | one FOL resolution / theorem-proving question |
| Review page | [[CSCE 420 Midterm Review]] | [[CSCE 420 Final Review]] |
| Rules | 2 pages front/back; one cheat sheet (one sheet, both sides, paper); most problems have ≥ 2 sub-questions for partial credit | same |

Both practice exams are 10 problems of roughly equal weight (the final's Problem 1 is 15 pts and Problem 4 is 5 pts), a mix of mark-one selections with required explanations and full worked derivations. Every page carries an honor-code line the student must sign. Several problems explicitly say *don't reduce to a single value — just show the formula*, so setup is graded over arithmetic.

## Ingested Sources

**Lectures (all 8):**

- [[CSCE 420 Lecture 1 — Introduction to AI]] — framing lecture; definitions, six foundational disciplines, history; 42 slides
- [[CSCE 420 Lecture 2 — Search and Game Playing]] — uninformed + informed search, CSP, minimax, alpha-beta, game AI history; 138 slides
- [[CSCE 420 Lecture 3 — Logic and Automated Theorem Proving]] — propositional + first-order logic, resolution, Prolog; 145 slides
- [[CSCE 420 Lecture 4 — Planning]] — Wumpus World, situation calculus, the frame problem; 27 slides
- [[CSCE 420 Lecture 5 — Uncertainty and Probabilistic Reasoning]] — Bayes, belief networks, decision theory; 67 slides
- [[CSCE 420 Lecture 6 — Machine Learning]] — decision trees, perceptrons, backprop, SOM, genetic algorithms; 124 slides
- [[CSCE 420 Lecture 7 — Deep Learning]] — CNNs, DQN, LSTM, transformers, limitations; 84 slides
- [[CSCE 420 Lecture 8 — AI Ethics]] — fairness, accountability, future of work, regulation; 20 slides

**Practice and code:**

- [[CSCE 420 Midterm Practice]] — no answer key; solutions in this KB were derived during ingest
- [[CSCE 420 Final Exam Practice]] — no answer key; solutions in this KB were derived during ingest
- [[SOM Notebook — Self-Organizing Maps (2D Grid)]] — NumPy implementation on an n×n grid

**Course export (ingested 2026-09-17).** The instructor's course-files export contained three semesters of material:

- **Fall 2026 (the user's section)** — [[CSCE 420 Homework 1 — Search]], [[CSCE 420 Homework 2 — Game Playing, Logic]], [[CSCE 420 Homework 3 — FOL, Resolution Prover, Prolog]] and [[CSCE 420 Homework 4 — Probability, Learning, Deep Learning]], with their notebooks in `raw/`. Assignment pages carry asks and conventions only. HW1 and HW2 are past due and the instructor has released official keys — [[CSCE 420 Homework 1 Solutions — Fall 2026]] and [[CSCE 420 Homework 2 Solutions — Fall 2026]]; HW3 and HW4 have no released key yet, so neither has a key page.
- **Spring 2026** — 38 lecture recordings, one source page each (`csce420-sp26-MMDD-*`), indexed under *Sources — CSCE 420 Spring 2026 Lecture Recordings*. Each carries `exam: midterm | final | excluded` in its frontmatter; four straddling pages are marked `midterm / final` with a boundary note in the body. Spring's HW3 (resolution prover + Prolog royalty) and HW4 (belief nets, DTL, perceptron, gradient descent, Colab CNN) are described in the 03-18 and 04-08 walkthrough pages as previews only.
- **Fall 2025** — [[CSCE 420 Fall 2025 — Midterm Review Recording]] (source of the Canvas objectives transcribed into [[CSCE 420 Midterm Review]]), [[CSCE 420 Fall 2025 — Whiteboard: Perceptron Decision Line]], and [[CSCE 420 Demo — Rejection Method Animation]].

Scheduling facts recovered from the recordings: the Spring 03-27 lecture was never recorded; 04-01 was replaced by a pre-recorded lecture (filed as 03-31); the 04-28 "Redefined Friday" class was a research talk and is not in the export.

The full lecture sequence is now ingested. Note that several concept pages predate the lecture ingests — they were reconstructed from the practice exams plus standard R&N material before the slides arrived, so where a page's framing differs from the instructor's, the lecture source page is authoritative.

## Session Recordings

Class-session notes transcribed from recordings — a separate stream from the lecture decks above, following the course day by day.


**Spring 2026 — January**

- [[CSCE 420 Spring 2026 — 01-12 Syllabus, What Is Intelligence]]
- [[CSCE 420 Spring 2026 — 01-14 Linguistics, Neuroscience, History of AI]]
- [[CSCE 420 Spring 2026 — 01-16 Modern AI, Limitations, Future]]
- [[CSCE 420 Spring 2026 — 01-21 Uninformed Search]]
- [[CSCE 420 Spring 2026 — 01-23 DFS, DLS, IDS, Informed Search Intro]]
- [[CSCE 420 Spring 2026 — 01-28 Greedy, A*, Heuristics]]
- [[CSCE 420 Spring 2026 — 01-30 IDA*, Iterative Improvement]]

**Spring 2026 — February**

- [[CSCE 420 Spring 2026 — 02-02 Simulated Annealing, CSP, Game Playing]]
- [[CSCE 420 Spring 2026 — 02-04 Alpha-Beta Pruning]]
- [[CSCE 420 Spring 2026 — 02-06 Chance Games, Game AI History, Logic Intro]]
- [[CSCE 420 Spring 2026 — 02-09 Knowledge Bases, Propositional Logic]]
- [[CSCE 420 Spring 2026 — 02-11 Normal Forms, Logical Consequence, Resolution]]
- [[CSCE 420 Spring 2026 — 02-13 HW2 Walkthrough, First-Order Logic]]
- [[CSCE 420 Spring 2026 — 02-16 Standard Form, Skolemization]]
- [[CSCE 420 Spring 2026 — 02-18 Composition, Unification, Factors]]
- [[CSCE 420 Spring 2026 — 02-20 FOL Resolution, Strategies]]
- [[CSCE 420 Spring 2026 — 02-23 Cheat Sheet Rules, Prover Demo, Prolog]]
- [[CSCE 420 Spring 2026 — 02-25 Planning]]
- [[CSCE 420 Spring 2026 — 02-27 Exam Rules, Practice Exam Walkthrough, Frame Problem, Uncertainty]]

**Spring 2026 — March**

- [[CSCE 420 Spring 2026 — 03-02 Probability, Bayes Rule]]
- [[CSCE 420 Spring 2026 — 03-04 Midterm Review, Bayesian Updating, Belief Networks]]
- [[CSCE 420 Spring 2026 — 03-16 Belief Network Inference]]
- [[CSCE 420 Spring 2026 — 03-18 HW3 Walkthrough, Machine Learning Intro]]
- [[CSCE 420 Spring 2026 — 03-20 Supervised, Unsupervised, RL Issues]]
- [[CSCE 420 Spring 2026 — 03-23 Decision Trees, Entropy]]
- [[CSCE 420 Spring 2026 — 03-25 Information Gain, Neural Networks Intro]]
- [[CSCE 420 Spring 2026 — 03-30 Perceptron Recap, Gradient Descent, Backprop I]]
- [[CSCE 420 Spring 2026 — 03-31 Backprop II, Recorded Lecture]]

**Spring 2026 — April**

- [[CSCE 420 Spring 2026 — 04-06 Demos, Autoencoders, SRN, Genetic Algorithms]]
- [[CSCE 420 Spring 2026 — 04-08 HW4 Walkthrough, Genetic Algorithms, Neuroevolution]]
- [[CSCE 420 Spring 2026 — 04-10 NEAT Demos, Deep Learning Intro]]
- [[CSCE 420 Spring 2026 — 04-13 Final Practice Walkthrough, Deep CNNs, AlexNet]]
- [[CSCE 420 Spring 2026 — 04-15 Final Review Posted, CNN Representations, Deep RL, DQN]]
- [[CSCE 420 Spring 2026 — 04-17 DQN Finished, Recurrent Networks and LSTM]]
- [[CSCE 420 Spring 2026 — 04-20 LSTM Applications, Attention, Transformers]]
- [[CSCE 420 Spring 2026 — 04-22 LLMs, Diffusion, Deep Learning Wrap-Up]]
- [[CSCE 420 Spring 2026 — 04-24 Self-Organizing Maps (Not on Exam)]]
- [[CSCE 420 Spring 2026 — 04-27 SOM Evaluation, AI Ethics (Not on Exam)]]

**Fall 2026**

- [[CSCE 420 Fall 2026 — 09-18 minmax.ipynb Walkthrough]]

## See Also

- [[Artificial Intelligence]]
- [[History of AI]]
- [[Foundations of AI]]
- [[Yoonsuck Choe]]
- [[CSCE 420 Lecture 1 — Introduction to AI]]
