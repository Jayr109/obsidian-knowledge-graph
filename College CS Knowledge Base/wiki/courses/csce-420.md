---
title: "CSCE 420"
type: course
tags: [csce420, artificial-intelligence, course]
sources: [csce420-lecture-01-introduction, csce420-midterm-practice, csce420-final-practice]
course: CSCE 420
updated: 2026-09-03
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

The full lecture sequence is now ingested. Note that several concept pages predate the lecture ingests — they were reconstructed from the practice exams plus standard R&N material before the slides arrived, so where a page's framing differs from the instructor's, the lecture source page is authoritative.

## See Also

- [[Artificial Intelligence]]
- [[History of AI]]
- [[Foundations of AI]]
- [[Yoonsuck Choe]]
- [[CSCE 420 Lecture 1 — Introduction to AI]]
