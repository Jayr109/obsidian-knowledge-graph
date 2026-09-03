# Index

Master catalog of all wiki pages. Updated on every ingest and after every filed query.
**Current count:** 307 pages (145 concepts, 53 algorithms, 1 data structure, 6 courses, 6 people, 95 sources, 1 overview) | **Last updated:** 2026-09-03

---

## Overview
- [[Overview]] — High-level synthesis; paradigm comparison table; full algorithm index

## Courses
- [[CSCE 411]] — Design and Analysis of Algorithms; Spring 2026; instructor: Calvin Beideman
- [[CSCE 313]] — Introduction to Computer Systems; instructor: Sandeep Kumar; POSIX/systems programming
- [[Corporate Finance and Valuation]] — undergraduate finance; TVM, NPV, risk, market efficiency; modules 3–12
- [[CSCE 420]] — Artificial Intelligence; instructor: Yoonsuck Choe; R&N 4th ed.; search, logic, probability, learning
- [[CSCE 421]] — Machine Learning; instructor: Shuiwang Ji; Learning From Data; linear models -> softmax
- [[CSCE 465]] — Computer & Network Security (465/765); instructor: Guofei Gu; crypto, OS, network, AI agent security

## People
- [[Calvin Beideman]] — CSCE 411 instructor; academic descendant of Robert Floyd
- [[Houngninou]] — CSCE 313 instructor (L22); data link layer / network security
- [[Sandeep Kumar]] — CSCE 313 primary instructor; OS as illusionist/referee/glue; OSSTEP + APUE
- [[Shuiwang Ji]] — CSCE 421 instructor; author of the softmax derivation notes
- [[Guofei Gu]] — CSCE 465 instructor; director of the SUCCESS Lab; BotHunter, FRESCO, SMASH
- [[Yoonsuck Choe]] — CSCE 420 instructor; brain-function perspective on AI; author of the SOM notebook

## Concepts — CSCE 313 (Systems)
- [[Operating Systems]] — three hats: illusionist/referee/glue; kernel vs. user mode
- [[Processes]] — process model, PCB, lifecycle states, context switch
- [[Virtual Memory]] — per-process address spaces, page tables, demand paging
- [[System Calls]] — traps, mode switches, x86-64 calling convention
- [[Interrupts and Exceptions]] — hardware interrupts, faults, aborts, traps; Intel exception table
- [[Inter-Process Communication]] — message passing vs. shared memory paradigms
- [[Pipes and FIFO]] — anonymous pipes, named pipes/FIFOs, dup2 for redirection
- [[Process API]] — fork/exec/wait/exit; zombie prevention
- [[Process Attributes]] — PID/UID/GID, signals (kill/raise/alarm), signal masks, sigaction
- [[UNIX File I/O]] — open/read/write/close/lseek; everything is a file
- [[File Descriptors]] — DT/FT/vnode three-table model; fork/dup sharing semantics
- [[File Systems]] — on-disk layout; inodes; indexed allocation; hard/soft links
- [[Threads]] — thread model, pthreads API, C++ std::thread, thread safety
- [[Thread Synchronization]] — race conditions, critical sections, atomicity
- [[Mutexes and Locks]] — pthread_mutex, unique_lock, coarse/fine-grained locking
- [[Condition Variables]] — wait/signal/broadcast, producer-consumer pattern
- [[Semaphores]] — counting semaphores, bounded buffer solution
- [[Computer Networking]] — TCP/IP, sockets API, DNS, client-server model
- [[Data Link Layer]] — OSI layer 2; Ethernet frames; MAC addresses; switch; packet encapsulation
- [[ARP]] — IP-to-MAC resolution via broadcast/cache; ARP spoofing MITM attack

## Concepts — CSCE 411 (Algorithms)
- [[Proofs and Induction]] — induction, loop invariants, algorithm correctness proofs
- [[Decidability and Undecidability]] — survey: decidable vs undecidable languages, deciders vs recognizers
- [[Turing Machines]] — infinite tape + finite control; accept/reject/loop; Church-Turing thesis; deciders vs recognizers
- [[Halting Problem]] — HALTS is undecidable by diagonalization; standard source language for reductions
- [[Loop Invariants]] — initialization/maintenance/termination; correctness of iterative algorithms
- [[Asymptotic Analysis]] — Big-O, Ω, Θ; Word-RAM model; worst-case runtime
- [[Master Theorem]] — closed-form solutions for D&C recurrences T(n)=aT(n/b)+f(n)
- [[Divide and Conquer]] — divide into independent subproblems; reduction; recurrences
- [[Graph Theory]] — graph ADT, types, representations, Handshake Lemma
- [[BFS and DFS]] — traversal algorithms; tree/back/forward/cross edges; O(n+m)
- [[Dynamic Programming]] — memoized overlapping subproblems; optimal substructure
- [[Graph DP]] — DP on graphs; subtree subproblems for trees
- [[Backtracking]] — recursive brute force; precursor to DP; DP = backtracking + memoization
- [[Greedy Algorithms]] — greedy choice property + optimal substructure; faster than DP
- [[SSSP]] — single source shortest paths; algorithm selection by graph type
- [[Minimum Spanning Trees]] — light edge property; Prim-Jarník and Kruskal's
- [[Maximum Flow]] — flow networks; max-flow min-cut theorem; augmenting paths
- [[Bipartite Matching]] — reduce to max flow; stable matching; Gale-Shapley
- [[Stable Matching]] — preference lists; no unstable pairs; Gale-Shapley produces one
- [[Linear Programming]] — linear objective + constraints; feasibility, convexity, duality
- [[NP and Complexity Classes]] — P, NP, Co-NP, EXP; verifier/certificate framework; P vs. NP
- [[NP Completeness]] — NP-hard, Cook-Levin theorem, Circuit-SAT; reduction chain; how to prove NP-completeness
- [[Karp Reductions]] — poly-time many-one reductions; the standard NP-hardness tool; vs. Turing reductions
- [[Vertex Cover]] — canonical NP-complete graph problem; tree DP, bipartite LP, 2-approximation
- [[Approximation Algorithms]] — approximation ratios; PTAS, FPTAS; VC 2-approx, Max-Cut 1/2-approx; greedy VC fails
- [[Balanced Brackets]] — detection and longest-subsequence for parentheses (greedy) and multi-type braces (stack + O(n³) DP)
- [[König's Theorem]] — max bipartite matching = min vertex cover; proved via LP duality and integrality
- [[LP Relaxation]] — removing integrality from IPs; totally unimodular matrices guarantee integral LP optima

## Concepts — CSCE 420 (Artificial Intelligence)
- [[Artificial Intelligence]] — four textbook definitions; R&N agent-based definition; why intelligence resists definition
- [[Strong AI and Weak AI]] — the two stances; other-minds problem; B&S pp. 6–7
- [[Turing Test]] — imitation game; behavior substituted for unobservable thought
- [[Chinese Room]] — Searle; syntax is not sufficient for semantics; AI ethics thread
- [[Philosophy of Mind]] — dualism, monism (idealism/materialism), epiphenomenalism
- [[Foundations of AI]] — philosophy, mathematics, psychology, cognitive science, linguistics, neuroscience
- [[History of AI]] — 1943 → present in six eras; AI@50 benchmark; major achievements
- [[Symbolic AI]] — 1950s–mid 80s; rule-based, theorem proving; cannot handle vagueness or learn
- [[Neurosymbolic AI]] — combining symbolic AI and deep learning; future-of-AI directions
- [[Heuristic Search]] — f = g + h; admissibility, consistency, contours; A* space problem
- [[Local Search]] — hill climbing; local maxima, plateaus, ridges; constant memory
- [[Constraint Satisfaction Problems]] — MRV, degree, least constraining value; map coloring
- [[Adversarial Search]] — game trees; MAX/MIN/chance nodes; why pruning matters
- [[First-Order Logic]] — clause form, skolemization; ∀∃ vs ∃∀ dependency
- [[Logical Inference]] — KB vs inference engine; domain independence good and bad
- [[Situation Calculus]] — possibility vs effect axioms; Poss/Result; frame problem
- [[Bayesian Networks]] — chain rule factorization; CPTs; causal node ordering
- [[Decision Tree Learning]] — entropy, information gain; ID3 root-attribute selection
- [[Machine Learning Paradigms]] — supervised / unsupervised / reinforcement; read it off the update rule
- [[Neural Networks]] — perceptron limits; hidden-unit counting; feature engineering vs depth
- [[Deep Learning]] — CNN/RNN/Transformer/deep RL; three fuels; four limitations
- [[Reinforcement Learning]] — reward, Q-function, credit assignment; why tables fail

## Concepts — Corporate Finance and Valuation
- [[Time Value of Money]] — present value, future value, discounting; perpetuity + PV formulas are all you need
- [[Perpetuity]] — infinite fixed-payment stream; PV = PMT/i; derived from interest definition
- [[CAPM]] — cost of equity r_e = r_f + β × ERP; supplies the equity leg of WACC
- [[Annuity]] — finite fixed-payment stream; derived as difference of two perpetuities
- [[Effective Annual Rate]] — true annual cost with compounding; EAR = (1 + r_period)^M − 1
- [[Fischer Equation]] — exact: (1+r_nom)=(1+r_real)(1+π); textbook approximation omits cross-product term
- [[PE Ratio]] — price/earnings comparables; rough ballpark only; varies widely even within same industry
- [[Volatility]] — std dev of returns; annualized by ×√(periods/year); Tesla ~70% annualized
- [[Diversification]] — combining imperfectly-correlated stocks reduces portfolio vol below least-volatile holding
- [[Efficient Market Hypothesis]] — strong/semi-strong/weak forms; Twitter 2022 tests semi-strong
- [[Net Present Value]] — only rule measuring value creation directly; IRR and payback period inferior
- [[Free Cash Flow]] — FCF = EBIT(1−t) + D&A − ΔGFA − ΔNWC; excludes interest tax shield
- [[WACC]] — weighted avg cost of capital; (E/V)×re + (D/V)×rd×(1−t); discount rate for FCF-based NPV

- [[Search Problem Formulation]] — <initial state, operators, goal, path cost>; state representation criteria
- [[Uninformed Search]] — BFS/UCS/DFS/DLS/IDS/BDS comparison; space is the binding constraint
- [[Repeated States]] — reversible operators make the space infinite; parent/cycle/hash-table strategies
- [[Admissible Heuristics]] — never overestimate; dominance; design by relaxation; h2 beats h1 539 vs 113 nodes
- [[Game Playing]] — contingency plans vs paths; game type table; evaluation functions; horizon effect
- [[Game AI Milestones]] — Deep Blue 1997 through AlphaGo, AlphaZero, MuZero, AlphaStar

- [[Knowledge Representation]] — logic vs frames; the representation hypothesis; subsymbolic alternatives
- [[Knowledge Base Systems]] — KB + inference engine; sound vs complete; the ontological/epistemological table
- [[Propositional Logic]] — wffs, semantics, validity vs inconsistency, the basic laws
- [[Normal Forms]] — CNF and DNF; literals, clauses, terms; distribution runs both ways
- [[Horn Clauses]] — at most one positive literal; implications with a single conclusion; tractable inference
- [[Inference Rules]] — modus ponens, unit resolution, resolution; resolution subsumes the others
- [[Logical Consequence]] — the refutation theorem; anything follows from False
- [[Prenex Normal Form]] — all quantifiers to the front; the quantifier equivalences
- [[Skolemization]] — eliminate existentials; constant vs function decided by quantifier order
- [[Substitution]] — bindings, instances, composition; the machinery under unification
- [[Resolvents and Factors]] — binary resolvent, factor of a clause, the four-case resolvent definition
- [[Resolution Strategies]] — level saturation, deletion/subsumption, unit preference, set of support
- [[Answer Extraction]] — the answer predicate; turning a prover into a question-answering system
- [[Prolog]] — logic programming on Horn clauses by backward chaining
- [[Planning]] — sequences of actions to achieve a goal; state-space, heuristic, partial-order
- [[Wumpus World]] — the entailment example; concluding from an absent percept
- [[Frame Problem]] — representing what does not change; successor-state axioms
- [[Truth Maintenance Systems]] — retraction and belief revision; where monotonic logic strains
- [[Uncertainty]] — laziness, theoretical and practical ignorance; prior vs posterior
- [[Decision Theory]] — probability + utility; the principle of maximum expected utility
- [[Probability Basics]] — notation, the three axioms, joint distributions, the 2^n problem
- [[Bayes Rule]] — inverting conditionals; the 1% base-rate result; causal vs diagnostic knowledge
- [[Conditional Independence]] — Bayesian updating; evidence combination becomes multiplication
- [[Belief Network Construction]] — the algorithm; why node ordering decides compactness
- [[Probabilistic Inference]] — diagnostic, causal, intercausal, mixed; explaining away
- [[Machine Learning]] — improving at a task through experience; the data deluge; ML poses no problems
- [[Supervised Learning Issues]] — generalization, sample complexity, catastrophic forgetting
- [[Curse of Dimensionality]] — 10^d samples for d dimensions; why coverage is impossible
- [[Inductive Bias]] — choosing among hypotheses that all fit; Ockham's razor
- [[Entropy and Information Gain]] — average surprisal; the criterion behind CHOOSE-ATTRIBUTE
- [[Linear Separability]] — what a perceptron can represent; XOR cannot be (Minsky & Papert 1969)
- [[Unsupervised Learning]] — no teacher; requires redundancy; clustering to feature mapping
- [[Recurrent Neural Networks]] — cycles give memory; the Elman/SRN context layer
- [[Convolutional Neural Networks]] — AlexNet; learned kernels resemble mammalian receptive fields
- [[Transformers]] — self-attention over Q/K/V; parallelizable; the basis of LLMs
- [[Long Short-Term Memory]] — input/forget/output gates; long-term retention in RNNs
- [[Deep Reinforcement Learning]] — deep for perception, RL for action; value/policy/actor-critic/model-based
- [[AI Ethics]] — bias, accountability, privacy, the future of work, regulation, developer responsibility

## Concepts — CSCE 421 (Machine Learning)
- [[Linear Models]] — the linear signal wTx; linear in x gives the hyperplane, linear in w makes algorithms work
- [[In-Sample and Out-of-Sample Error]] — Ein computable, Eout is what matters; the generalization gap
- [[Sigmoid Function]] — theta(s) = 1/(1+e^-s); three properties and what each one buys
- [[Softmax Function]] — R^K to a distribution; shift-invariant; Jacobian p_i(delta_ij - p_j)
- [[Cross-Entropy Loss]] — distance between distributions; one-hot collapses it to -log of the true class
- [[Maximum Likelihood Estimation]] — why cross-entropy is derived rather than chosen

## Concepts — CSCE 465 (Security)
- [[Computer Security]] — the umbrella; threat/attack/attacker/asset; four goals; why security is hard; InfoSec = CompSec + ComSec
- [[CIA Triad]] — confidentiality (data/existence/configuration), integrity (data + origin = authentication), availability; commercial vs military examples
- [[Security Attack Taxonomy]] — interception, tampering, fabrication, interruption; active vs passive; MITM; crypto does not hide metadata
- [[Security Policy and Mechanism]] — what/how/how-well; prevention vs detection; why prevention is more fundamental; trust and assumptions
- [[Security Services]] — confidentiality, authentication, integrity, non-repudiation, access control, monitor & response
- [[Security Assurance]] — security/functionality/ease-of-use/cost trade-off; obscurity and legislation rejected; the security life-cycle
- [[Security Design Principles]] — the ten Saltzer & Schroeder principles, from economy of mechanism to compromise recording
- [[Security Threat Landscape]] — malware, spam, botnet, DDoS, phishing, ransomware, AI/agentic attacks; a composition chain, not a taxonomy
- [[AI Agent Security]] — the agent loop; LLM output driving real execution; four trust boundaries that fail; the context window has no content/command type
- [[Prompt Injection]] — direct vs indirect as a channel distinction; why encryption cannot fix it; required/helpful/irrelevant
- [[OpenClaw]] — HW1 platform; 10-interface attack surface, 470 advisories; ask=off by default; per-layer checks, no unified policy
- [[CVE-2024-5565]] — Vanna.AI prompt-injection-to-RCE; exec() on LLM output; the Task 4 advisory template

## Algorithms
- [[Turing Reductions]] — prove undecidability by reducing FROM known undecidable language
- [[Binary Search]] — O(log n) search in sorted array; T(n)=T(n/2)+O(1)
- [[Karatsuba's Algorithm]] — O(n^log₂3) multiplication; 3 multiplications instead of 4
- [[Topological Sort]] — reverse postorder DFS; linear ordering of DAG vertices; O(n+m)
- [[Strongly Connected Components]] — two-pass DFS on G and G^R; O(n+m)
- [[Dijkstra's Algorithm]] — SSSP for non-negative weights; O((n+m) log n) with binary heap
- [[Bellman-Ford Algorithm]] — SSSP with negative edges; O(nm); detects negative cycles
- [[Floyd-Warshall]] — APSP via DP over intermediate vertices; O(V³)
- [[Prim-Jarník Algorithm]] — MST by growing one tree; O((n+m) log n)
- [[Kruskal's Algorithm]] — MST by sorted edges + union-find; O(m log m)
- [[Ford-Fulkerson Algorithm]] — max flow via augmenting paths; O(|f*|·m)
- [[Edmonds-Karp Algorithm]] — Ford-Fulkerson with BFS; O(nm²); always polynomial
- [[Gale-Shapley Algorithm]] — stable matching in O(n²); hospital-optimal
- [[Longest Increasing Subsequence]] — DP; O(n²) or O(n log n)
- [[Longest Valley Subsequence]] — 2D anchor-both-ends DP; O(n³); valley = decrease then increase
- [[Subset Sum]] — DP; O(n·T) pseudopolynomial decision problem
- [[Maximum Weight Independent Set]] — NP-hard general; O(n) tree DP
- [[Interval Scheduling]] — greedy earliest-finish-time; O(n log n)
- [[Huffman Coding]] — greedy optimal prefix-free code; O(n log n)
- [[Simplex Algorithm]] — LP solver; vertex-walking; Dantzig 1947
- [[Interval Covering]] — minimum integer points stabbing all intervals; greedy sort by finish, O(n log n)
- [[Max-Weight Matching in Trees]] — tree DP on edge weights; 2-case recurrence; O(n)
- [[Increment and Triple]] — greedy backward to 1 (triple if divisible by 3); O(log³ y)
- [[Blue-Green Trees]] — 3-state tree DP counting valid 2-colorings; O(n^{1+log₂3}) via Karatsuba

## Algorithms — CSCE 420 (Artificial Intelligence)
- [[Forward and Backward Chaining]] — data-driven vs goal-driven proof; backward suits Horn form
- [[Perceptron]] — one threshold unit; boolean gates; the geometric line; the learning rule
- [[Backpropagation]] — gradient descent through hidden layers; the sigmoid derivative trick
- [[Genetic Algorithms]] — population, fitness, crossover, mutation; diversity; neuroevolution
- [[General Search Algorithm]] — one skeleton, one queuing function per strategy; visit != expand
- [[Breadth-First Search]] — enqueue at end; complete and optimal; O(b^(d+1)) space is the problem
- [[Depth-First Search]] — enqueue at front; incomplete; O(bm) space
- [[Uniform-Cost Search]] — BFS by lowest g(n); the h=0 case of A*
- [[Depth-Limited Search]] — DFS with a depth cap; complete only if l >= d
- [[Iterative Deepening Search]] — DFS space with BFS guarantees; the uninformed default
- [[Bidirectional Search]] — O(b^(d/2)); needs explicit goals and reversible operators
- [[Best-First Search]] — the informed skeleton; sorted by an evaluation function
- [[Greedy Best-First Search]] — h(n) alone; incomplete and non-optimal; Romania 450 vs A*'s 418
- [[Beam Search]] — best-first with a fixed beam width; bounded memory, incomplete
- [[Hill Climbing]] — iterative improvement; local maxima, plateau, ridge; random restart
- [[A* Search]] — best-first on f = g + h; complete and optimal; exponential space
- [[IDA*]] — iterative-deepening A* via DFS-CONTOUR; linear space (call stack)
- [[Simulated Annealing]] — accept worsening moves with P = e^(−ΔE/T); cooling schedule
- [[Minimax]] — back up max/min through the game tree; O(b^d)
- [[Alpha-Beta Pruning]] — exact minimax in O(b^(d/2)); cut needs two finite bounds
- [[Expectimax]] — chance nodes as probability-weighted averages; utility magnitudes matter
- [[Resolution]] — refutation-complete; negate conclusion, clausify, derive False
- [[Unification]] — MGU by parallel descent; variable binding, function clash, occurs check
- [[Self-Organizing Map]] — Kohonen; BMU in input space, neighborhood on the grid; unsupervised
- [[Deep Q-Network]] — one Q-value output per action; argmax to act; Atari from raw frames

## Data Structures
- [[Disjoint Sets]] — union-find; make_set/find/union; near-O(α(n)) with path compression

## Sources — Corporate Finance and Valuation
- [[M3: Annuity]] — derives annuity PV as difference of two perpetuities; only two formulas needed for all TVM
- [[M3: Perpetuity]] — derives PV = PMT/i from British consol bonds; one algebra step
- [[M3: Mafia Loan]] — 2%/week vig → EAR 180%, APR 104%; illustrates compounding and EAR vs. APR
- [[M3: Payday Loan]] — 15%/biweekly fee → EAR 3,686%; payday lenders charge more than loan sharks
- [[M4: Fischer Equation — Part 1]] — supply/demand model of real rates; motivation for inflation adjustment
- [[M4: Fischer Equation — Part 2]] — exact Fischer equation derived; approximate vs. exact; $4,200 error on $2M
- [[M6: PE Ratios]] — PE valuation method; hotel industry example shows ratios from 20 to 79; rough ballpark only
- [[M7: Calculating Volatility]] — Yahoo Finance → weekly returns → STDEV.S → ×√52; Tesla = 70% annualized
- [[M7: Diversification]] — Tesla/NVIDIA/Ford/ExxonMobil portfolio; 50% EXXON combo beats EXXON alone
- [[M8: Twitter Acquisition — Part 1]] — EMH review; strong form rejected (Enron); weak/semi-strong defined
- [[M8: Twitter Acquisition — Part 2]] — instructor trades Twitter; price at $37–49 vs. $54.20 binding deal; both sides argued
- [[M10: NPV Rule Is Superior]] — NPV vs. IRR, payback period, profitability index; NPV is the only correct rule
- [[M11: Importance of Accounting]] — accounting review intro; essential prerequisite for FCF analysis
- [[M12: Free Cash Flow]] — FCF formula built from EBIT; each adjustment explained conceptually; WACC double-count warning
- [[M13: Integrating Concepts, Part 1]] — Amcor FCF model: sunk cost, DDB depreciation, inflation, NWC, asset disposal
- [[M13: Integrating Concepts, Part 2]] — Amcor WACC + NPV: CAPM, beta sourcing, Damodaran ERP, full pipeline

## Sources — CSCE 313 Lectures
- [[CSCE 313 Lecture 1 — Introduction to Operating Systems]] — OS three hats, processes, virtual memory, compilation pipeline; 36 pages
- [[CSCE 313 Lecture 2 — Architectural Support for Operating Systems]] — privilege levels, interrupts/exceptions, system calls; 28 pages
- [[CSCE 313 Lecture 5 — Inter-Process Communication: Pipes and FIFO]] — pipe(), FIFO, fork+pipe, dup2, Unix philosophy; 45 pages
- [[CSCE 313 Lecture 6 — Process API Part I]] — exec family, fork+exec pattern, process states; 24 pages
- [[CSCE 313 Lecture 7 — Process API Part II]] — wait/waitpid, zombie processes, zombie prevention; 22 pages
- [[CSCE 313 Lecture 8 — Process Attributes]] — PCB fields, state machine, context switch, ucontext; 28 pages
- [[CSCE 313 Lecture 9 — UNIX File I/O]] — open/read/write/close, permissions, three-table model; 35 pages
- [[CSCE 313 Lecture 10 — UNIX I/O: File Descriptors, Redirection, and Standard I/O]] — dup2, fork+fd, stdio; 23 pages
- [[CSCE 313 Lecture 11 — File Systems II]] — disk layout, inodes, indexed allocation, links, directory API; 39 pages
- [[CSCE 313 Lecture 12 — Threads Introduction]] — signals API + pthreads intro, race conditions; 35 pages
- [[CSCE 313 Lecture 14 — Thread Synchronization I: Mutexes and Locks]] — mutexes, critical sections, producer-consumer intro; 31 pages
- [[CSCE 313 Lecture 15 — Thread Synchronization II]] — condition variables, correct producer-consumer, C++ thread API; 31 pages
- [[CSCE 313 Lecture 16 — Thread Synchronization III: Condition Variables and Semaphores]] — semaphores, bounded buffer; 21 pages
- [[CSCE 313 Lecture 18 — Introduction to Networking/Internet]] — TCP/IP, sockets, DNS, client-server; 51 pages
- [[CSCE 313 Lecture 22 — Network Security: The Data Link Layer]] — OSI model, Ethernet, MAC addresses, ARP, ARP spoofing; 18 slides

## Sources — CSCE 411 Lectures
- [[Lecture 2 — Proofs, Programs & Problem Solving]] — induction, loop invariants, GCD, InsertionSort; 15 slides
- [[Lecture 4 — Decidability and Undecidability]] — TMs, Halting problem, Turing reductions; 19 slides
- [[Lecture 5 — Undecidability Reductions]] — reduction proofs practice; 10 slides
- [[Lecture 6 — Asymptotic Analysis]] — Big-O, Word-RAM, runtime analysis; 21 slides
- [[Lecture 7 — Divide and Conquer]] — reduction, binary search, Karatsuba, master theorem; 19 slides
- [[Lecture 8 — Graphs]] — graph ADT, representations, Handshake Lemma; 28 slides
- [[Lecture 9 — BFS and DFS]] — WFS, DFS/BFS trees, cycles, toposort, SCCs; 36 slides
- [[Lecture 10 — Single Source Shortest Paths]] — BFS, Dijkstra, Bellman-Ford, DAG SP; 49 slides
- [[Lecture 11 — Minimum Spanning Trees]] — graph layering, Prim-Jarník, Kruskal, union-find; 38 slides
- [[Lecture 15 — Maximum Flow]] — flow networks, Ford-Fulkerson, Edmonds-Karp, max-flow min-cut; 29 slides
- [[Lecture 16 — Bipartite Matching]] — matching via flow, Gale-Shapley, stable matching; 27 slides
- [[Lecture 18 — Recursive Backtracking]] — backtracking design, memoization intro; 22 slides
- [[Lecture 19 — Dynamic Programming (I)]] — top-down vs bottom-up DP, design framework; 14 slides
- [[Lecture 20 — Dynamic Programming (II)]] — LIS, Subset Sum, Cherry Collecting; 15 slides
- [[Lecture 22 — Graph DP]] — Floyd-Warshall, MWIS in trees, Beideman's lineage; 15 slides
- [[Lecture 23 — Greedy Algorithms]] — Interval Scheduling, Huffman, exchange arguments; 45 slides
- [[Lecture 24 — Linear Programming]] — LP formulation, feasibility, convexity; 12 slides
- [[Lecture 25 — Linear Programming (II)]] — standard form, Simplex, LP duality; 21 slides
- [[Lecture 26 — NP]] — P, NP, Co-NP, verifiers, 2-COL vs 3-COL; 25 slides
- [[Lecture 27 — NP Verifiers]] — verifier proofs, Cook-Levin, Circuit-SAT, SAT, VC, TSP, Clique; 26 slides
- [[Lecture 28 — NP-Completeness]] — Karp vs Turing reductions, NP-hard vs NP-complete, HALTS, Cook-Levin; 21 slides
- [[Lecture 29 — NP-Hardness Proofs]] — full chain SAT→3-SAT→3-COL; Karp reduction tips and gadgets; 31 slides
- [[Lecture 31 — Approximation Algorithms]] — approximation ratio, FPTAS, VC 2-approx via matching, Max-Cut greedy; 26 slides

## Algorithms — CSCE 421 (Machine Learning)
- [[Linear Regression]] — least squares; normal equations; closed form w = (XTX)^-1 XTy via pseudoinverse
- [[Logistic Regression]] — sigmoid on the linear signal; cross-entropy from MLE; no closed form
- [[Softmax Regression]] — K-class LR; shift-invariance; binary LR is the K=2 case
- [[Gradient Descent]] — negative gradient is steepest by Taylor; fixed rate, SGD, mini-batch

## Sources — CSCE 420 (Artificial Intelligence)
- [[CSCE 420 Lecture 3 — Logic and Automated Theorem Proving]] — 145 slides; propositional + first-order logic, resolution, Prolog
- [[CSCE 420 Lecture 4 — Planning]] — 27 slides; Wumpus World, situation calculus, the frame problem
- [[CSCE 420 Lecture 5 — Uncertainty and Probabilistic Reasoning]] — 67 slides; Bayes, belief networks, decision theory
- [[CSCE 420 Lecture 6 — Machine Learning]] — 124 slides; decision trees, perceptrons, backprop, SOM, GAs
- [[CSCE 420 Lecture 7 — Deep Learning]] — 84 slides; CNNs, DQN, LSTM, transformers, limitations
- [[CSCE 420 Lecture 8 — AI Ethics]] — 20 slides; fairness, accountability, future of work, regulation
- [[CSCE 420 Lecture 2 — Search and Game Playing]] — 138 slides; uninformed + informed search, CSP, minimax, alpha-beta, game AI history
- [[CSCE 420 Lecture 1 — Introduction to AI]] — what AI is, six foundational disciplines, full history, deep learning summary; 42 slides
- [[CSCE 420 Midterm Practice]] — 10 problems: strong/weak AI, A* vs IDA*, annealing, CSP/LCV, expectimax, alpha-beta, inference engines, skolemization, unification, resolution
- [[CSCE 420 Final Exam Practice]] — 10 problems: FOL resolution, situation calculus, belief networks, info gain, network expressiveness, spiral features, SOM, deep learning domains, DQN

## Sources — CSCE 421 (Machine Learning)
- [[CSCE 421 T01 — Introduction and Linear Regression]] — what needs learning, perceptron hypothesis set, least squares in closed form; 20 slides
- [[CSCE 421 T02 — Logistic Regression for Binary Classification]] — sigmoid, cross-entropy from MLE, gradient descent and SGD; 30 slides
- [[CSCE 421 T03 — Logistic Regression: From Binary to Multi-Class]] — softmax, shift-invariance, K=2 equivalence to sigmoid; 20 slides
- [[CSCE 421 T03 Notes — Softmax Regression Derivations]] — typed notes; softmax Jacobian and the dL/da = p - y result; 6 pages
- [[SOM Notebook — Self-Organizing Maps (2D Grid)]] — NumPy SOM on an n×n grid; BMU, Gaussian neighborhood, decay schedule; three input distributions

## Sources — CSCE 465 (Computer & Network Security)
- [[CSCE 465 Lecture 1 — Course Introduction]] — logistics, grading, mini-research project; security definition, goals, CIA triad; 39 slides (7–18 image-only)
- [[CSCE 465 Lecture 2 — Security Overview]] — the foundations lecture; attack taxonomy, policy/mechanism/assurance, the ten design principles; 50 slides
- [[CSCE 465 HW1 — Build and Threat-Model an AI Agent]] — assignment brief; 120 pts + 200 bonus; AI agent security and prompt injection; 31 slides

## Sources — Course Notes
- [[Course Notes — Section 1: Foundational Notation]] — mathematical notation reference
- [[Course Notes — Section 2: Review of Logic and Proofs]] — logic, proof techniques
- [[Course Notes — Chapter 3: Decidability and Undecidability]] — official notes; duplicate PDF noted

## Sources — Exams
- [[Exam 1 Solutions — Spring 2026]] — covers proofs through graphs; T/F key results documented
- [[Exam 2 Solutions — Spring 2026]] — covers BFS/DFS through bipartite matching; T/F documented
- [[Exam 2 Sample Solutions — Spring 2026]] — practice exam; same coverage as Exam 2
- [[Exam 3 Solutions — Spring 2026]] — covers DP, greedy, LP duality, interval covering, max-weight matching in trees
- [[Final Exam Solutions — Spring 2026]] — covers full semester; T/F key results; array rotation, LVS DP, fruit salad flow, Half-Cycle NP-completeness

## Sources — Homework
- [[Homework 2 Solutions — Spring 2026]] — decidability closure properties, semi-decidable → decidable
- [[Homework 3 Solutions — Spring 2026]] — Big-O properties, D&C recurrences
- [[Homework 4 Solutions — Spring 2026]] — shortest paths with constraints, graph layering, tournament ranking
- [[Homework 5 Solutions — Spring 2026]] — bipartite matching, perfect matching game strategy
- [[Homework 6 Solutions — Spring 2026]] — 5 scheduling greedy variants, balanced brackets, delivering pizzas DP, increment-and-triple, blue-green trees
- [[Homework 7 Solutions — Spring 2026]] — LP formulation, bipartite matching LP relaxation, König's theorem, Primes ∈ Co-NP, NP closure properties

## Sources — Practice Sets
- [[Practice — Asymptotic Analysis]] — Big-O proofs, ExchangeSort Θ(n³) analysis
- [[Practice — Divide & Conquer and Graphs]] — fixed-point binary search, flawed tree proof
- [[Practice — DP and Greedy]] — minimum vertex cover in trees, (d+1)-coloring greedy
- [[Practice — Dynamic Programming]] — longest decreasing subsequence (1- and 2-parameter DP)
- [[Practice — Proofs]] — induction and proof technique exercises
- [[Practice — Shortest Paths and MSTs]] — Dijkstra, Bellman-Ford, MST algorithms
- [[Practice — Undecidability]] — Turing reduction proofs
- [[Practice — NP-Hardness]] — five reductions: kCol, kCycle, Partition, HalfClique, NAE-4SAT

## Sources — Worked Examples
- [[NP-Hardness Scribbles]] — handwritten 3-COL ≤_p kCol reduction (parameter hard-coding)
