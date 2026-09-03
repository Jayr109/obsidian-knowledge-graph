---
title: "Overview"
type: overview
tags: [overview, synthesis]
sources: [lecture-2-proofs-programs-problem-solving, lecture-4-decidability-and-undecidability, lecture-5-undecidability-reductions, lecture-6-asymptotic-analysis, lecture-7-divide-and-conquer, lecture-8-graphs, lecture-9-bfs-and-dfs, lecture-10-sssp, lecture-11-msts, lecture-15-maximum-flow, lecture-16-bipartite-matching, lecture-18-backtracking, lecture-19-dynamic-programming-1, lecture-20-dynamic-programming-2, lecture-22-graph-dp, lecture-23-greedy-algorithms, lecture-24-linear-programming, lecture-25-linear-programming-2, lecture-26-np, lecture-27-np-verifiers, lecture-28-np-completeness, lecture-29-np-hardness-proofs, lecture-31-approximation-algorithms, csce313-lecture-01-introduction-to-operating-systems, csce313-lecture-02-architectural-support-for-os, csce313-lecture-05-ipc-pipes-and-fifo, csce313-lecture-06-process-api-part-i, csce313-lecture-07-process-api-part-ii, csce313-lecture-08-process-attributes, csce313-lecture-09-unix-file-io, csce313-lecture-10-file-descriptors-redirection-stdio, csce313-lecture-11-file-systems-ii, csce313-lecture-12-threads-introduction, csce313-lecture-14-thread-synchronization-i-mutexes, csce313-lecture-15-thread-synchronization-ii, csce313-lecture-16-thread-synchronization-iii-semaphores, csce313-lecture-18-introduction-to-networking, m03-annuity, m03-perpetuity, m03-mafia-loan, m03-payday-loan, m04-fischer-1, m04-fischer-2, m06-pe-ratios, m07-calculating-volatility, m07-diversification, m08-twitter-1, m08-twitter-2, m10-npv-rule-is-superior, m11-importance-of-accounting, m12-free-cash-flow, csce420-lecture-01-introduction, csce420-midterm-practice, csce420-final-practice, csce420-som-notebook, csce465-lecture-01-course-introduction, csce465-lecture-02-security-overview, csce465-hw1-build-and-threat-model-an-ai-agent]
updated: 2026-09-03
---

This knowledge base covers six university courses: [[CSCE 411]] (Design and Analysis of Algorithms, taught by [[Calvin Beideman]]), [[CSCE 313]] (Introduction to Computer Systems, taught by [[Sandeep Kumar]]), and [[Corporate Finance and Valuation]] (an undergraduate finance course). CSCE 411 spans algorithm design paradigms; CSCE 313 covers systems programming, OS concepts, and the POSIX API; the finance course covers asset valuation, capital budgeting, and risk measurement. [[CSCE 420]] (Artificial Intelligence, taught by [[Yoonsuck Choe]]) surveys search, logic, probabilistic reasoning, and machine learning through deep learning. [[CSCE 421]] (Machine Learning, taught by [[Shuiwang Ji]]) builds ML from linear models upward, deriving each method rather than cataloguing it. [[CSCE 465]] (Computer & Network Security, taught by [[Guofei Gu]]) surveys security across cryptography, OS/software, network, and AI-agent layers.

## Core Thesis

Every major algorithm design technique builds on **optimal substructure**. The key question is what additional structure a problem has:

- **Greedy choice property** → [[Greedy Algorithms]] (fastest; explore 1 subproblem per step)
- **Overlapping subproblems, no greedy shortcut** → [[Dynamic Programming]] (explore all, memoize)
- **Disjoint subproblems** → [[Divide and Conquer]] (explore all, no memoization needed)
- **Linear structure** → [[Linear Programming]] (general-purpose solver)

Decidability sits outside this hierarchy — it asks whether a problem is solvable at all before asking how efficiently.

## Course Arc

| Phase | Topics | Lectures |
|---|---|---|
| Foundations | Proofs, induction, loop invariants | 2 |
| Computability | Decidability, Turing machines, Halting problem | 4–5 |
| Analysis | Asymptotic analysis, Word-RAM model | 6 |
| Divide & Conquer | Reduction, binary search, Karatsuba, Master Theorem | 7 |
| Graph Basics | Graph ADT, representations, Handshake Lemma | 8 |
| Graph Traversal | BFS, DFS, toposort, SCCs, cycle detection | 9 |
| Shortest Paths | Dijkstra's, Bellman-Ford, DAG SP | 10 |
| MSTs | Prim-Jarník, Kruskal's, Union-Find | 11 |
| Network Flow | Max flow, Ford-Fulkerson, Edmonds-Karp | 15 |
| Matching | Bipartite matching, Gale-Shapley stable matching | 16 |
| DP Intro | Backtracking → memoization → bottom-up DP | 18–19 |
| DP Practice | LIS, Subset Sum, Graph DP | 20, 22 |
| Greedy | Interval Scheduling, Huffman Coding | 23 |
| Linear Programming | LP formulation, Simplex, duality | 24–25 |
| NP and Verifiers | P/NP/CoNP/EXP, certificates, verifier proofs | 26–27 |
| NP-Completeness | Karp reductions, Cook-Levin, NP-hard vs. NP-complete | 28 |
| NP-Hardness Proofs | Reduction chain (SAT→3-SAT→3-COL); gadgets and tips | 29 |
| Approximation | Vertex Cover 2-approx, Max-Cut greedy, FPTAS | 31 |

## Paradigm Map

| Paradigm | Key Property | Subproblems | Typical Complexity |
|---|---|---|---|
| [[Divide and Conquer]] | Optimal substructure | All (disjoint) | O(n log n) |
| [[Backtracking]] | — | All (brute force) | O(2ⁿ) |
| [[Dynamic Programming]] | Optimal substructure + overlapping | All (memoized) | Polynomial |
| [[Greedy Algorithms]] | Optimal substructure + greedy choice | 1 per step | O(n log n) |
| [[Linear Programming]] | Linear objective + constraints | — | Polynomial |

## Full Algorithm Index

### Foundations & Computability
- [[Turing Reductions]] — reduce FROM undecidable TO new language to prove undecidability
- [[Binary Search]] — O(log n) search in sorted arrays
- [[Karatsuba's Algorithm]] — O(n^log₂3) integer multiplication

### Graph Algorithms
- [[Topological Sort]] — reverse postorder DFS; O(n+m)
- [[Strongly Connected Components]] — two-pass DFS; O(n+m)
- [[Dijkstra's Algorithm]] — SSSP, non-negative weights; O((n+m) log n)
- [[Bellman-Ford Algorithm]] — SSSP, negative edges; O(nm)
- [[Floyd-Warshall]] — APSP via DP; O(V³)
- [[Prim-Jarník Algorithm]] — MST; O((n+m) log n)
- [[Kruskal's Algorithm]] — MST; O(m log m)
- [[Ford-Fulkerson Algorithm]] — max flow; O(|f*|·m)
- [[Edmonds-Karp Algorithm]] — max flow with BFS; O(nm²)
- [[Gale-Shapley Algorithm]] — stable matching; O(n²)

### Dynamic Programming
- [[Longest Increasing Subsequence]] — O(n²) or O(n log n)
- [[Subset Sum]] — O(n·T) pseudopolynomial
- [[Maximum Weight Independent Set]] — tree DP; O(n)

### Greedy
- [[Interval Scheduling]] — earliest finish time; O(n log n)
- [[Huffman Coding]] — optimal prefix-free code; O(n log n)

### Linear Programming
- [[Simplex Algorithm]] — vertex-walking LP solver (Dantzig, 1947)

### NP-Completeness and Approximation
- [[Karp Reductions]] — poly-time many-one reductions; the standard NP-hardness tool
- [[NP and Complexity Classes]] — P, NP, Co-NP, EXP; verifier framework
- [[NP Completeness]] — Cook-Levin; reduction chain CIRCUIT-SAT → SAT → 3-SAT → 3-COL
- [[Vertex Cover]] — canonical NP-complete problem; tractable special cases (trees, bipartite)
- [[Approximation Algorithms]] — approximation ratios, PTAS, FPTAS; VC 2-approx, Max-Cut 1/2-approx

## Data Structures
- [[Disjoint Sets]] — union-find; near-O(α(n)) with path compression + union by rank

## CSCE 313 — Systems Programming

[[CSCE 313]] introduces the programmer's view of operating systems via the POSIX API. Instructor: [[Sandeep Kumar]]. Textbooks: OSSTEP, APUE.

### OS Foundations
- [[Operating Systems]] — three hats: illusionist, referee, glue
- [[Processes]] — process model, PCB, lifecycle states, context switch
- [[Virtual Memory]] — per-process address spaces, page tables, demand paging
- [[System Calls]] — kernel/user mode boundary, x86-64 calling convention
- [[Interrupts and Exceptions]] — hardware interrupts, faults, aborts, traps

### IPC and Process Management
- [[Inter-Process Communication]] — message passing vs. shared memory paradigms
- [[Pipes and FIFO]] — anonymous pipes, named pipes, dup2 for redirection
- [[Process API]] — fork/exec/wait/exit; zombie prevention
- [[Process Attributes]] — PID/UID/GID, signals (kill/raise/alarm), signal masks

### File I/O and Storage
- [[UNIX File I/O]] — open/read/write/close/lseek; everything is a file
- [[File Descriptors]] — DT/FT/vnode three-table model; fork/dup sharing
- [[File Systems]] — on-disk layout; inodes; indexed allocation; hard/soft links

### Concurrency and Synchronization
- [[Threads]] — thread model, pthreads API, C++ std::thread
- [[Thread Synchronization]] — race conditions, critical sections, atomicity
- [[Mutexes and Locks]] — pthread_mutex, unique_lock, coarse/fine-grained locking
- [[Condition Variables]] — wait/signal/broadcast, producer-consumer pattern
- [[Semaphores]] — counting semaphores, bounded buffer solution

### Networking
- [[Computer Networking]] — TCP/IP, sockets API, DNS, client-server model

## CSCE 420 — Artificial Intelligence

[[CSCE 420]] (instructor [[Yoonsuck Choe]]; Russell & Norvig 4th ed.) surveys AI from its philosophical framing to modern deep learning. Its organizing question is **where knowledge comes from**, and the course arc is the historical answer to that question: hand-coded logic, then probabilistic models fit to data, then representations learned end-to-end.

### The Arc as a Single Thesis

| Era | Knowledge source | Course unit | Fails at |
|---|---|---|---|
| [[Symbolic AI]] | Written down by humans | Search, [[Logical Inference]], [[Resolution]] | Vagueness; cannot learn from data |
| Probabilistic | Estimated from structured data | [[Bayesian Networks]], [[Decision Tree Learning]] | Needs the model structure specified |
| [[Deep Learning]] | Learned from raw data | [[Neural Networks]], [[Deep Q-Network]] | Reasoning, common sense, interpretability |

Each era's failure is the next era's motivation, and the last row's failures are why [[Neurosymbolic AI]] closes the course by pointing back at the first row.

### Search and Games
- [[Heuristic Search]] — f = g + h; [[A* Search]] is optimal but exponential in space; [[IDA*]] trades re-expansion for a linear-space call stack
- [[Local Search]] — no path, just a current state; [[Simulated Annealing]] escapes local optima via P = e^(−ΔE/T)
- [[Constraint Satisfaction Problems]] — structured states admit domain-independent heuristics: MRV picks the variable most likely to fail, LCV picks the value most likely to succeed
- [[Adversarial Search]] — [[Minimax]], the exact speedup [[Alpha-Beta Pruning]], and [[Expectimax]] for chance

### Logic and Planning
- [[First-Order Logic]] — clause form and skolemization; Skolem *function* vs. *constant* encodes quantifier dependency
- [[Resolution]] — one refutation-complete rule; negate the conclusion and derive False
- [[Unification]] — what lifts resolution from propositional to first-order
- [[Logical Inference]] — domain independence buys universality and costs efficiency
- [[Situation Calculus]] — possibility vs. effect axioms; the frame problem

### Learning
- [[Machine Learning Paradigms]] — supervised / unsupervised / reinforcement, identifiable from the update rule
- [[Decision Tree Learning]] — entropy and information gain
- [[Neural Networks]] — a unit is always linear; expressiveness comes from layers or from features
- [[Self-Organizing Map]] — competition in input space, cooperation on the grid
- [[Reinforcement Learning]] and [[Deep Q-Network]] — learning to act from reward

### Recurring Exam Patterns
- Both practice exams grade *setup*, not arithmetic — several problems say outright not to reduce to a single value.
- Clause-form conversion is the most-flagged trap: a conjunction must split into separate clauses.
- Several answers are readable directly off a given formula ([[Simulated Annealing]]'s acceptance probability, the [[Self-Organizing Map]] update rule) without recalling the surrounding theory.

### The Full Lecture Series (Decks 1-8)

All eight slide decks are now ingested. Two through eight were added on 2026-09-01 and are the **instructor's own framing** of material previously reconstructed here from the practice exams; 20 pre-existing pages were reconciled against them rather than duplicated.

| Deck | Slides | Central idea |
|---|---|---|
| 1 Introduction | 42 | What AI is; six foundational disciplines |
| 2 [[CSCE 420 Lecture 2 — Search and Game Playing\|Search & Games]] | 138 | Every strategy is one algorithm with a different **queuing function**; space, not time, is the binding constraint |
| 3 [[CSCE 420 Lecture 3 — Logic and Automated Theorem Proving\|Logic]] | 145 | A chain of reductions ending in **one normal form and one rule** |
| 4 [[CSCE 420 Lecture 4 — Planning\|Planning]] | 27 | Effect axioms say what changes, never what stays — the [[Frame Problem]] |
| 5 [[CSCE 420 Lecture 5 — Uncertainty and Probabilistic Reasoning\|Probability]] | 67 | Degrees of belief where logic demanded T/F; $n2^k$ beats $2^n$ |
| 6 [[CSCE 420 Lecture 6 — Machine Learning\|Machine Learning]] | 124 | Successive relaxation: symbolic → linear → multilayer → unsupervised → gradient-free |
| 7 [[CSCE 420 Lecture 7 — Deep Learning\|Deep Learning]] | 84 | Learned representations replace designed features |
| 8 [[CSCE 420 Lecture 8 — AI Ethics\|AI Ethics]] | 20 | We do not fully understand why it works or how to control it |

**The through-line the decks make explicit.** Each unit is a response to the previous unit's stated failure. The pattern recurs throughout: uninformed search is bounded by memory, so [[Iterative Deepening Search]] and [[IDA*]] trade recomputation for space; propositional logic cannot express general rules, so [[First-Order Logic]] adds objects and quantifiers; logic cannot represent persistence, so planning needs successor-state axioms; logic cannot represent doubt, so probability replaces truth values with degrees of belief; hand-specified models do not scale, so learning fits them from data; hand-designed features do not scale, so deep learning learns those too. The final deck observes that the last step cost us reasoning, causality, and explainability — the very things the first deck had.

**Two results recur across the whole course.** The *predicted minus true* gradient shape appears in the [[Perceptron]] rule, in [[Backpropagation]], and in [[CSCE 421]]'s [[Softmax Regression]]. And the pattern of buying tractability with expressiveness appears in [[Horn Clauses]] (vs. full CNF), in [[Admissible Heuristics]] (relaxation), and in [[Conditional Independence]] (vs. the full joint table).


## CSCE 421 — Machine Learning

[[CSCE 421]] is the counterpart to CSCE 420's breadth: where 420 surveys AI, 421 derives a small number of models carefully. Instructor: [[Shuiwang Ji]]. Text: *Learning From Data*.

The first three topic decks are one continuous argument rather than three subjects. Every model is a [[Linear Models|linear model]] built on the signal $s = \mathbf{w}^T\mathbf{x}$; they differ only in what is applied to $s$ and what error is minimized:

| Model | Applied to $s$ | Target | Error | Optimizer |
|---|---|---|---|---|
| [[Linear Regression]] | nothing | $y \in \mathbb{R}$ | Squared error | Closed form (pseudoinverse) |
| [[Logistic Regression]] | [[Sigmoid Function]] | $y \in [0,1]$ | [[Cross-Entropy Loss]] | [[Gradient Descent]] / SGD |
| [[Softmax Regression]] | [[Softmax Function]] | $K$-class distribution | Cross-entropy | Gradient descent |

Two structural results tie the arc together. [[Maximum Likelihood Estimation]] shows cross-entropy is *derived*, not chosen — it is what maximizing the likelihood of the data reduces to. And [[Softmax Regression]] proves binary logistic regression is exactly the $K=2$ case of the multi-class model, via softmax shift-invariance.

The recurring payoff is a gradient of the form **predicted minus true**: $\partial L/\partial a_k = p_k - y_k$ for softmax cross-entropy, matching the $X^T(\hat{\mathbf{y}}-\mathbf{y})$ shape in linear regression. One optimizer serves all of them.

This course connects directly to CSCE 420's [[Neural Networks]] and [[Deep Learning]] pages: logistic regression is a single neuron, and deep learning is the same softmax head over *learned* rather than hand-designed features.

## CSCE 465 — Computer & Network Security

[[CSCE 465]] is the security course, taught by [[Guofei Gu]]. Three sources are ingested: the logistics lecture, the foundations lecture, and the first homework brief. The classical mechanisms (cryptography, OS, network, web) are still outstanding — but the AI agent unit, which the course places last, arrived first via the homework, so the KB currently holds the course's *conceptual apparatus* plus one worked modern attack class.

The framing: **security is the prevention of certain intentional actions**, or more formally, a state in which successful yet *undetected* theft, tampering, and disruption is kept low or tolerable. Everything decomposes from two words — *intentional* and *undetected*.

The course asks three questions in order, and the concept pages follow that order:

| Question | Page |
|---|---|
| What is being protected, and how is an attack classified? | [[CIA Triad]], [[Security Attack Taxonomy]], [[Security Threat Landscape]] |
| **What?** — what is allowed | [[Security Policy and Mechanism]] |
| **How?** — what enforces it | [[Security Services]], [[Security Design Principles]] |
| **How well?** — and at what cost | [[Security Assurance]] |

- [[Computer Security]] — the umbrella: threat/attack/attacker/asset vocabulary, the four goals, why security is hard, InfoSec = CompSec + ComSec
- [[CIA Triad]] — confidentiality (data / existence / configuration), integrity (data + origin, where origin integrity *is* authentication), availability
- [[Security Attack Taxonomy]] — interception, tampering, fabrication, interruption; active vs passive; MITM; why cryptography does not guarantee confidentiality
- [[Security Policy and Mechanism]] — policy defines security; prevention is more fundamental than detection, because detection depends on an audit trail prevention must protect
- [[Security Services]] — confidentiality, authentication, integrity, non-repudiation, access control, monitor & response
- [[Security Assurance]] — the security/functionality/ease-of-use/cost trade-off; why obscurity and legislation are not strategies; the security life-cycle
- [[Security Design Principles]] — the ten Saltzer & Schroeder principles; the most durable material in the course

**The AI agent unit (from HW1).** The course's newest material, and the only place so far where a concrete modern attack is worked end to end:

- [[AI Agent Security]] — the agent loop; four trust boundaries that fail; why *the context window is the program* with no type distinction between content and commands
- [[Prompt Injection]] — direct vs. indirect as a **channel** distinction, not a wording one; why encrypting the channel cannot fix it
- [[OpenClaw]] — the homework platform; 10-interface attack surface across 470 advisories; per-layer checks with no unified policy
- [[CVE-2024-5565]] — Vanna.AI prompt-injection-to-RCE, worked end to end as the advisory-analysis template

**The through-line from 1975 to 2026.** The AI agent material is not a separate subject bolted on. [[OpenClaw]] runs tool calls with `ask=off` by default (fail-safe defaults inverted); its layers each check locally with no unified policy (complete mediation failing at the level of *composition*, exactly the policy-composition hazard [[Security Policy and Mechanism]] warns about); and the durable fix for [[CVE-2024-5565]] is to constrain the tool so a permitted call cannot be repurposed (economy of mechanism and least privilege at the model boundary). [[Prompt Injection]] also gives the cleanest statement of Lecture 2's argument that cryptography is not confidentiality: an encrypted, authenticated pipe delivers the poisoned page **intact**, because *"did this arrive unmodified?"* is an integrity question and *"should the agent act on it?"* is an authorization one.

**The one asymmetry that explains the field.** Defense is inherently more expensive than offense, because the attacker needs only the weakest link while the defender must secure every path. Two of the ten design principles (work factor, compromise recording) exist purely to ration defensive effort against that asymmetry, and the whole prevention/detection/recovery split is a response to it.

**Where it connects to the rest of the KB.** CSCE 465 lists [[CSCE 313]] as a prerequisite and reuses it directly: [[Computer Networking]] and [[Data Link Layer]] are the substrate for the network security unit, and [[ARP]] spoofing is already in the KB as an origin-integrity failure — CSCE 313 taught it as a protocol flaw, CSCE 465 names the property it violates and the attack family (fabrication) it belongs to. The lecture's claim that *most TCP/IP protocols were not built with security in mind* is the general form of what the ARP page documents in one protocol. The [[Processes]] / [[Virtual Memory]] / [[File Descriptors]] material underlies the OS security unit, and [[Virtual Memory]] reappears in this course as an instance of least common mechanism. In the other direction the course closes on AI agent security, which touches [[CSCE 420]] and [[CSCE 421]] from a direction neither covers: those courses ask whether a model is *accurate*, this one asks whether it is *attackable*.

## Open Questions / Gaps

### CSCE 411
- Cherry Collecting (Lecture 20): recurrence details visual — not captured by text extraction.
- LP formulations (Lectures 24–25): equation slides visual — see raw PPTX for formal definitions.
- LP Duality: proof of strong duality not captured.
- Lecture 28–29 reduction-construction slides (CIRCUIT-SAT→SAT, SAT→3-SAT, 3-SAT→3-COL gadgets) are visual-only; gadget structures sketched in source pages from prose alone.
- Lecture 31 approximation-ratio analyses (proofs that VertexCoverApprox is a 2-approximation, Greedy Max-Cut is a 1/2-approximation) are visual-only on slides; reasoning sketched in source page.
- CSCE 411 Lectures 3, 12, 13, 14, 17, 21, 30 not yet ingested.

### CSCE 313
- Lectures 3, 4, 13, 17, and others not yet ingested (scheduling, advanced FS, security).
- Many slides are diagram-heavy (memory layouts, CPU diagrams, OS tables) — flagged in source pages.
- x86-64 register table slide (Lecture 1) garbled during text extraction.

### CSCE 465
- Lectures 1–2 and the HW1 brief are ingested. Cryptography, OS/software security, network security, and web security are all outstanding; the AI agent unit is covered early via the homework.
- Slides 7–18 of Lecture 1 are image-only (news headlines, incident screenshots, botnet diagram) — the specific incidents cited in lecture are not recoverable. Lecture 2 and the HW1 deck have no image-only slides.
- No **cryptographic primitive or protocol** has been worked through yet; the only concrete vulnerability in the KB is [[CVE-2024-5565]], which came from the homework rather than a lecture.
- The [[OpenClaw]] advisory distribution beyond the four largest interface categories exists only in a pie chart and was not extractable. The instructor's paper (Suwansathit, Zhang & Gu, 2026) would close that gap and is assigned reading; it is not in the KB.
- Three discussion questions Lecture 2 poses and does not answer are recorded on its source page (switched-network sniffing, where else caching breaks complete mediation, whether root violates least privilege). They read like exam prompts.
- The HW1 deck labels two different sections "Part 4" and titles a three-phase diagram "6 stages"; both recorded rather than guessed at.

### CSCE 420
- Only Lecture 1 has been ingested; the lectures covering search, logic, probability, and learning are not yet in the KB. Concept pages for those topics were reconstructed from the two practice exams plus standard R&N material, so they carry exam framing rather than this instructor's slide framing.
- Both practice exams ship **without answer keys**. Worked solutions in this KB were derived during ingest and are marked as such on each page.
- Final Practice Problem 7(2) is ambiguous as worded; both readings are recorded on [[Neural Networks]] rather than one being asserted.
- Lecture 1 slides 33–42 are image-only; their content was transcribed by rendering the pages, but the figures themselves are not extracted into the KB.
- Uninformed search, propositional model checking, MDPs, and HMMs appear in R&N but in neither practice exam — coverage unknown.

## Corporate Finance and Valuation

[[Corporate Finance and Valuation]] is an undergraduate finance course covering asset pricing, capital budgeting, risk measurement, and market efficiency. The central principle: the value of any financial instrument is a function of its expected future cash flows, the timing of those cash flows, and their riskiness.

### Time Value of Money (Module 3)
- [[Perpetuity]] — infinite fixed payments; PV = PMT/i; foundational formula
- [[Annuity]] — finite fixed payments; derived as difference of two perpetuities
- [[Effective Annual Rate]] — true annual cost accounting for compounding; EAR = (1 + r_period)^M − 1

### Interest Rates and Inflation (Module 4)
- [[Fischer Equation]] — exact relation: (1 + r_nom) = (1 + r_real)(1 + π); textbook omits the cross-product term

### Equity Valuation (Module 6)
- [[PE Ratio]] — quick comparables tool only; varies wildly even within industries; not a substitute for DCF

### Risk and Return (Module 7)
- [[Volatility]] — standard deviation of returns; annualized by multiplying by √(periods/year)
- [[Diversification]] — combining imperfectly-correlated assets reduces portfolio volatility below any individual holding

### Market Efficiency (Module 8)
- [[Efficient Market Hypothesis]] — three forms (strong/semi-strong/weak); Twitter 2022 case tests semi-strong form

### Capital Budgeting (Module 10)
- [[Net Present Value]] — only rule that directly measures value creation; IRR and payback period are inferior

### Cash Flow Analysis (Modules 11–12)
- [[Free Cash Flow]] — FCF = EBIT(1−t) + D&A − ΔGFA − ΔNWC; excludes interest tax shield (captured in WACC)

## See Also

- [[CSCE 411]]
- [[CSCE 313]]
- [[Calvin Beideman]]
- [[CSCE 420]]
- [[Yoonsuck Choe]]
- [[CSCE 465]]
- [[Guofei Gu]]
- [[Corporate Finance and Valuation]]
