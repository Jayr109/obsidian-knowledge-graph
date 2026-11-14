---
title: "CSCE 420 Midterm Review"
type: source
tags: [csce420, exam, midterm, review, scope, study-guide]
sources: []
course: CSCE 420
exam: midterm
semesters: [Fall 2025, Spring 2026]
updated: 2026-09-17
---

The instructor's own **midterm scope**, assembled from the Canvas "Midterm Review" page (captured frame-by-frame from the Fall 2025 walkthrough recording) plus his spoken hints in two offerings — Fall 2025 and Spring 2026. The page and the scope were identical across both semesters, so this is stable.

> **This page is for the MIDTERM only.** Final-exam scope lives on [[CSCE 420 Final Review]] and is deliberately kept separate — the final is *not cumulative*, and nothing from the midterm reappears on it.

## Exam Logistics (as stated, both offerings)

- **In class, 50 minutes**, on the last class day before spring break (Spring 2026: Fri Mar 6; Fall 2025: the Friday after the review).
- **Cheat sheet allowed**: one sheet of handwritten notes. In Spring he handed out the paper himself.
- **Weight**: 25% of the grade (final is 30%; together 55%).
- **Practice exam** under Canvas Quick Links → Practice Exam → *midterm exam sample*. Already ingested: [[CSCE 420 Midterm Practice]].

## Scope at a Glance

| Deck | On the midterm? | Depth |
|---|---|---|
| slide01 Introduction | Yes — **exactly one question** | Read, don't memorize; mirrors the practice exam |
| slide02 Search & Game Playing | Yes — the bulk | Uninformed, informed, iterative improvement, CSP, minimax, alpha-beta, chance games |
| slide03 Logic | Yes — **through unification** | Propositional logic + theorem proving in full; FOL only up to standard form / substitution / unification |
| slide03 FOL resolution, answer extraction, Prolog | **No** | Explicitly excluded |
| slide04 Planning and everything after | **No** | Post-midterm; see [[CSCE 420 Final Review]] |

## Spoken Hints — Worth More Than the Page

These are things he *said* that are not written on the Canvas page. He told the Fall 2025 class outright: *"I've given you some very suggestive hints while talking about this — watch the recording."*

1. **Slide 1**: *"No need to memorize anything. There will be only one question. See the midterm exam practice."*
2. **Alpha-beta and minimax**: *"Always use the algorithm. If you start to reason about it in your head, you'll make errors — and the same with me. Probably you should write down the algorithm on your cheat sheet."* See [[Alpha-Beta Pruning]] — the Max-Value / Min-Value pseudocode is the thing to copy.
3. **Simulated annealing**: *"It's about minimizing energy, and how it accepts or rejects moves based on the probability and delta E. This is very similar to the practice exam."* See [[Simulated Annealing]].
4. **Games with chance**: *"Doesn't appear in the practice exam, but it might actually appear in our exam."* See [[Expectimax]].
5. **History of game AI**: *"Pretty high-level topics — may not be on the exam."*
6. **Logic is the main part**: *"Propositional logic and theorem proving — that would be the main part. You need to know how to convert into standard form and how to apply the resolution proof. Also the basic laws, the inference rules — modus ponens, resolution — and how they might be related, and the limitations of propositional logic."*
7. **Where FOL stops**: *"Mostly canonical forms — prenex normal form, skolemization — and up to substitution and unification. That's the end of it. No full-blown first-order theorem proving. Question answering won't be on the exam."*
8. **Spring 2026 addition**: *"Review your homework questions."* He walked through the HW2 solutions on 02-27 — *"I actually almost gave out the answers."*

## The Canvas Page — Learning Objectives, Complete

Transcribed from the page as displayed on screen. Bold verbs are the page's own emphasis. Order preserved.

### Introduction (slide01)

> *No need to memorize anything from slide01. Just read through the slides. There will be only 1 question from this slide deck. See the midterm exam practice.*

- **Identify** the required and optional textbooks for the course and the notable figures included in their covers.
- **Explain** the different definitions of intelligence and the broad scope of AI, including problem-solving, reasoning, learning, and robotics.
- **Differentiate** between the concepts of strong AI and weak AI and describe their respective challenges.
- **Discuss** the role of philosophy, particularly the philosophy of mind, in AI, and articulate the concepts of dualism, monism, idealism, materialism, and epiphenomenalism.
- **Recognize** the importance of AI ethics and the issues it focuses on, such as safety, fairness, privacy, transparency, and more.
- **Explain** the contribution of different academic disciplines, such as mathematics, psychology, linguistics, cognitive science, and neuroscience, to AI.
- **Trace** the history of AI from its early stages in the 1940s to the present day, highlighting key developments and milestones.
- **Evaluate** the successes and breakthroughs of AI in various domains, including computer games, language models, and scientific applications like AlphaFold.
- **Analyze** the evolution of AI approaches from symbolic logic-based to machine learning and deep learning.
- **Predict** the potential future developments in AI, focusing on the pursuit of Artificial General Intelligence (AGI) and neuro-symbolic AI.

KB pages: [[CSCE 420 Lecture 1 — Introduction to AI]], [[Strong AI and Weak AI]], [[Philosophy of Mind]], [[Foundations of AI]], [[History of AI]], [[Neurosymbolic AI]].

### Search and Game Playing (slide02)

**Intro**

- **Explain** the significance of search in AI and its prevalence in everyday scenarios, such as Google search, by exploring the role of search in problem-solving and game-playing.
- **Identify** the key components of a typical search problem, including initial states, operators, and goal states, and recognize how they contribute to the search process.
- **Explore** various search types, such as uninformed and informed search, and understand how they are influenced by task requirements and available information.
- **Consider** the application of search algorithms in game-playing, using chess as an example, and recognize the similarities between game-playing and search problems.
- **Evaluate** different search strategies based on criteria such as time complexity, space complexity, completeness, and optimality, to determine their effectiveness in solving search problems.

**Uninformed search**

- **Explain** the concept and implementation of breadth-first search (BFS) as a method for exploring a search tree, including its key characteristics, such as visiting nodes in a breadth-first order and the role of the node list.
- **Evaluate** the performance of BFS based on the branching factor and depth of the solution, recognizing its completeness and exponential time and space complexity.
- **Explore** depth-first search (DFS) and its variations, including the process of node expansion and the stack-based data structure used in DFS.
- **Analyze** the limitations of DFS, such as incompleteness, suboptimality, and exponential space complexity, and learn about depth-limited search and iterative deepening search as modifications to address these issues.
- **Discuss** Depth Limited Search (DLS) and Iterative Deepening Search (IDS).
- **Explain** the concept and benefits of bidirectional search, including its reduction of search space and the requirements for its application, such as backtracking possibilities and explicit knowledge of the goal's location.
- **Recognize** the challenges of repeated states in search algorithms and the impact on search efficiency, and explore techniques to avoid repeated states, such as not returning to the parent node and avoiding the generation of previously visited states, considering factors like cycle detection and storage optimization through hash tables and checksums.

**Informed search**

- **Explain** the concept of informed search algorithms and their use of domain knowledge to enhance search efficiency.
- **Discuss** the best-first search algorithm, its queueing function, and the role of the evaluation function in this algorithm.
- **Apply** the greedy best-first search and A* algorithms to problem-solving scenarios, demonstrating the use of distinct evaluation functions.
- **Analyze** the strengths and weaknesses of the greedy best-first search and A* algorithms, including their completeness, optimality, and space complexity.
- **Evaluate** the impact of heuristic functions on the performance of search algorithms using examples such as the 8-puzzle problem.
- **Synthesize** knowledge of informed search algorithms to understand and explain the implementation of Iterative Deepening A* (IDA*) and Beam Search algorithms.

**Iterative improvement algorithms and CSP**

- **Explain** the concept of iterative improvement algorithms, including Hill Climbing and Simulated Annealing, and how they differ from informed and uninformed search algorithms.
- **Explain** the process of Hill Climbing, its strengths and weaknesses, and strategies to overcome its limitations.
- **Describe** the concept of Simulated Annealing, its inspiration from the metallurgical process, and how it introduces randomness into the hill climbing process.
- **Analyze** the goal of Simulated Annealing in minimizing energy and how it accepts or rejects moves based on a probability function controlled by delta E and the temperature.
- **Explain** the concept of constraint satisfaction search, including the definition of state, goal, and operators, and the different types of constraints.
- **Apply** the strategies for constraint satisfaction problems, including backtracking and forward checking, and the heuristics for variable selection and value assignment to solve a simple CSP problem like map coloring.

**Game playing and pruning, probabilistic games**

- **Explain** the concept of game playing in artificial intelligence, including its challenges and the categorization of games along the axes of deterministic vs. chance and perfect vs. imperfect information.
- **Apply** the Minimax algorithm to solve two-person perfect information games, demonstrating an understanding of how the algorithm generates a game tree, applies a utility function to the leaves, and assigns minimum or maximum values to nodes.
- **Analyze** the limitations of the Minimax algorithm, particularly its time complexity, and **propose** solutions such as evaluation functions and cutoff tests to limit exploration depth.
- **Understand and implement** α-β pruning to optimize the Minimax algorithm, demonstrating an understanding of the conditions for α and β cuts, how α and β values are updated and passed down the tree, and how pruning can reduce computational complexity.
- **Evaluate** games with elements of chance, understanding how to assign utility values to random outcomes and how to calculate the utility of chance nodes based on the probability of each outcome. Discuss the increased time complexity due to the random element and the potential for pruning.
- **Appreciate** the history and evolution of game AI, **recognize** key milestones and advancements in the field, and **reflect** on the power of deep reinforcement learning as demonstrated in various game-playing scenarios.

KB pages: [[CSCE 420 Lecture 2 — Search and Game Playing]] and every page it lists — in particular [[General Search Algorithm]], [[Uninformed Search]], [[Iterative Deepening Search]], [[Admissible Heuristics]], [[A* Search]], [[IDA*]], [[Hill Climbing]], [[Simulated Annealing]], [[Constraint Satisfaction Problems]], [[Minimax]], [[Alpha-Beta Pruning]], [[Expectimax]].

### Logic (slide03)

**Intro**

- **Explain** the role of logic and automated theorem proving in traditional or symbolic AI.
- **Identify** and differentiate between the two main classes of representations in traditional AI: logic-based methods and frame-based methods.

**Propositional logic + theorem proving**

- **Define** and **apply** the syntax and semantics of propositional logic, including the concept of interpretations and the assignment of truth values.
- **Recall** and **explain** the basic laws of Propositional Logic, such as the commutative, associative, distributive, identity, universal bound, negation, double negation, De Morgan's, and idempotent laws.
- **Utilize** inference rules, including *modus ponens* and unit resolution, to generate new, logically consistent sentences.
- **Explain** the concept of normal forms in propositional logic and apply various logical laws and rules to convert arbitrary formulas into normal forms.
- **Discuss** the concept of logical consequence and evaluate its importance in automated theorem proving and knowledge-based scenarios.
- **Translate** English statements into propositional logic formulas, **convert** these formulas into conjunctive normal form, and **apply** the resolution algorithm to prove theorems.
- **Evaluate** the limitations of propositional logic and consider the potential benefits of more expressive logic, such as first-order logic.

**First-order logic and standard forms**

- **Define** and **explain** key concepts in first-order logic, including terms, predicates, quantifiers, domain interpretation, and semantics. They will also be able to **identify** the properties of formulas, including consistency, inconsistency, validity, and invalidity.
- **Convert** first-order logic sentences into machine-friendly forms, such as Prenex Normal Form and Conjunctive Normal Form.
- **Understand** and apply the new concepts of skolemization, substitution, and unification.
- ~~**NOT COVERED**: Evaluate the advantages and disadvantages of resolution-based theorem proving.~~

KB pages: [[CSCE 420 Lecture 3 — Logic and Automated Theorem Proving]], [[Knowledge Representation]], [[Propositional Logic]], [[Normal Forms]], [[Inference Rules]], [[Logical Consequence]], [[Resolution]], [[First-Order Logic]], [[Prenex Normal Form]], [[Skolemization]], [[Substitution]], [[Unification]].

**Not on the midterm** (post-unification material): [[Resolvents and Factors]], [[Resolution Strategies]], [[Answer Extraction]], [[Prolog]].

## How to Use This Page

Work the practice exam first — he says repeatedly that the real exam mirrors it. Then use the objectives above as a checklist: every bold verb is a thing you should be able to *do*, not just recognize. The three hints that will cost points if ignored: copy the alpha-beta algorithm onto the cheat sheet; know the simulated-annealing accept/reject rule cold; be able to run a propositional resolution proof end to end.

## See Also

- [[CSCE 420 Final Review]]
- [[CSCE 420 Midterm Practice]]
- [[CSCE 420 Fall 2025 — Midterm Review Recording]]
- [[CSCE 420]]
