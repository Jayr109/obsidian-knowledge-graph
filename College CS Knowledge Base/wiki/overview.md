---
title: "Overview"
type: overview
tags: [overview, synthesis]
sources: [csce-313-lecture-22-data-link-layer, csce313-lecture-01-introduction-to-operating-systems, csce313-lecture-02-architectural-support-for-os, csce313-lecture-05-ipc-pipes-and-fifo, csce313-lecture-06-process-api-part-i, csce313-lecture-07-process-api-part-ii, csce313-lecture-08-process-attributes, csce313-lecture-09-unix-file-io, csce313-lecture-10-file-descriptors-redirection-stdio, csce313-lecture-11-file-systems-ii, csce313-lecture-12-threads-introduction, csce313-lecture-14-thread-synchronization-i-mutexes, csce313-lecture-15-thread-synchronization-ii, csce313-lecture-16-thread-synchronization-iii-semaphores, csce313-lecture-18-introduction-to-networking, csce420-final-practice, csce420-lecture-01-introduction, csce420-lecture-02-search-and-game-playing, csce420-lecture-03-logic, csce420-lecture-04-planning, csce420-lecture-05-probabilistic-reasoning, csce420-lecture-06-machine-learning, csce420-lecture-07-deep-learning, csce420-lecture-08-ai-ethics, csce420-midterm-practice, csce420-som-notebook, csce421-t01-linear-regression, csce421-t02-logistic-regression, csce421-t03-softmax-regression, csce421-t03-softmax-regression-notes, csce421-t04-overfitting, csce421-t05-loss-functions, csce421-t05-loss-functions-notes, csce421-t06-multilayer-perceptron, csce421-t07-backpropagation-examples, csce421-t08-convolution, csce421-t09-cnn, csce421-t10-attention-transformers-llms, csce421-hw1-solution, csce421-hw2-solution, csce421-t11-pca-autoencoders, csce421-t11-pca-notes, csce465-hw1-build-and-threat-model-an-ai-agent, csce465-lecture-01-course-introduction, csce465-lecture-02-security-overview, csce465-lecture-03-introduction-to-cryptography, csce465-lecture-03a-secret-key-cryptography-i, exam-1-solutions, exam-2-sample-solutions, exam-2-solutions, exam-3-solutions-sp26, final-exam-sp26, homework-6-solutions-sp26, homework-7-solutions-sp26, hw2-solutions, hw3-solutions, hw4-solutions, hw5-solutions, lecture-10-sssp, lecture-11-msts, lecture-15-maximum-flow, lecture-16-bipartite-matching, lecture-18-backtracking, lecture-19-dynamic-programming-1, lecture-2-proofs-programs-problem-solving, lecture-20-dynamic-programming-2, lecture-22-graph-dp, lecture-23-greedy-algorithms, lecture-24-linear-programming, lecture-25-linear-programming-2, lecture-26-np, lecture-27-np-verifiers, lecture-28-np-completeness, lecture-29-np-hardness-proofs, lecture-31-approximation-algorithms, lecture-4-decidability-and-undecidability, lecture-5-undecidability-reductions, lecture-6-asymptotic-analysis, lecture-7-divide-and-conquer, lecture-8-graphs, lecture-9-bfs-and-dfs, m03-annuity, m03-mafia-loan, m03-payday-loan, m03-perpetuity, m04-fischer-1, m04-fischer-2, m06-pe-ratios, m07-calculating-volatility, m07-diversification, m08-twitter-1, m08-twitter-2, m10-npv-rule-is-superior, m11-importance-of-accounting, m12-free-cash-flow, m13-integrating-concepts-part1, m13-integrating-concepts-part2, notes-chapter-3-decidability, notes-section-1-foundational-notation, notes-section-2-logic-and-proofs, np-hardness-scribbles, practice-asymptotic-analysis, practice-divide-conquer-graphs, practice-dp-and-greedy, practice-dynamic-programming, practice-np-hardness, practice-proofs, practice-shortest-paths-msts, practice-undecidability, csce465-lecture-03b-secret-key-cryptography-ii-modes-of-operation, csce465-lecture-05-public-key-cryptography, csce465-lecture-04-hash-functions, csce465-lecture-06a-user-authentication, csce465-lecture-07-operating-system-security, csce465-lecture-08-security-theory-policies-and-models, csce465-lecture-09-software-security-buffer-overflow, csce465-recitation-gdb-basics, csce465-lecture-10-network-basics, csce465-lecture-11-malware, csce465-lecture-12-vulnerability-analysis, csce465-lecture-13-firewall, csce465-lecture-14-intrusion-detection-system]
updated: 2026-11-16
---

This knowledge base covers six university courses: [[CSCE 411]] (Design and Analysis of Algorithms, taught by [[Calvin Beideman]]), [[CSCE 313]] (Introduction to Computer Systems, taught by [[Sandeep Kumar]]), and [[Corporate Finance and Valuation]] (an undergraduate finance course). CSCE 411 spans algorithm design paradigms; CSCE 313 covers systems programming, OS concepts, and the POSIX API; the finance course covers asset valuation, capital budgeting, and risk measurement. [[CSCE 420]] (Artificial Intelligence, taught by [[Yoonsuck Choe]]) surveys search, logic, probabilistic reasoning, and machine learning through deep learning. [[CSCE 421]] (Machine Learning, taught by [[Shuiwang Ji]]) builds ML from linear models upward, deriving each method rather than cataloguing it, and now runs the full arc from [[Linear Regression]] through [[Overfitting]] and generalization, a unified treatment of [[Loss Functions]], the [[Multilayer Perceptron]] with [[Backpropagation]], [[Convolutional Neural Networks]] with [[Batch Normalization]], on to [[Attention Mechanism|attention]], [[Transformers]] and [[Large Language Models]], and finally into unsupervised territory with [[Principal Component Analysis]] and [[Autoencoders]]. [[CSCE 465]] (Computer & Network Security, taught by [[Guofei Gu]]) surveys security across cryptography, OS/software, network, and AI-agent layers.

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

[[CSCE 465]] is the security course, taught by [[Guofei Gu]]. **Eighteen sources are ingested:** the logistics lecture, the foundations lecture, the first homework brief, five cryptography lectures (3, 3a, 3b, 4, 5) and user authentication (6a), the two OS-and-system-security decks — Lecture 7 (mechanisms) and Lecture 8 (theory) — the software-security opener, Lecture 9 (buffer overflow) with its companion gdb recitation, and five network-security decks — Lecture 10 (TCP/IP background), Lecture 11 (malware), Lecture 12 (vulnerability analysis), Lecture 13 (firewalls) and Lecture 14 (intrusion detection). **Applied cryptography is complete** across secret key, hashes and public key. **Still outstanding: web security**, the last topic in the outline's network security row. The KB holds the course's conceptual apparatus, one worked modern attack class (AI agents, which arrived early via the homework), the full cryptography unit, and — with Lecture 8 — the formal half of access control: the [[Safety Problem|undecidability of safety]] and the four classical [[Security Models|models]] ([[Bell-LaPadula Model|BLP]], [[Biba Integrity Model|Biba]], [[Chinese Wall Model|Chinese Wall]], [[Role-Based Access Control|RBAC]]). Lecture 9 then turns from models to code: [[Buffer Overflow|buffer overflow]] end to end, from [[Stack Smashing|stack smashing]] and [[Shellcode|shellcode]] through [[Format String Vulnerabilities|format strings]] to [[Buffer Overflow Defenses|NX, ASLR and bounds checking]]. Lectures 10 and 11 open **network security**: the protocol background ([[Internet Protocol|IP]], [[TCP]], [[ICMP]], [[HTTP]], [[SMTP]]) and then [[Malware|malware]] — [[Computer Viruses|viruses]], [[Worms|worms]] from [[Notable Worms|Morris to Slammer]], [[Botnets|botnets]] and [[Stuxnet]].

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

**Applied cryptography (from Lecture 3).** The first *mechanism* the course teaches, rather than a framework:

- [[Cryptography]] — the five definitions; encryption is not compression; Kerckhoffs's principle as "secret keys vs. secret algorithms"; cryptography is rarely the weakest link
- [[Cryptanalysis]] — ciphertext-only / known-plaintext / chosen-plaintext; brute force economics; the recognition problem
- [[Cipher Security Models]] — unconditional (`H(p) = H(p|c)`), provable (reduction to a hard problem), computational (the one everything actually meets)
- [[Classical Ciphers]] — Caesar, mono-alphabetic + frequency analysis, permutation ciphers; **a large key space is necessary but not sufficient**
- [[One-Time Pad]] — Shannon's two requirements; XOR; why reuse cancels the key
- [[Cryptography Taxonomy]] — by key count (none/one/two — hash/secret/public) and by processing (stream/block)

**Secret key cryptography (from Lecture 3a).** The first complete algorithms in the course, and the theory they share:

- [[Secret Key Cryptography]] — four applications (channel, storage, integrity via MIC, authentication); five key bits per decade; out-of-band key agreement is the structural limit
- [[Confusion and Diffusion]] — Shannon's principles; confusion by substitution, diffusion by permutation, **alternating**; the avalanche effect with DES's round-by-round numbers
- [[Block Ciphers]] — the generic model; block size trade-off; the seven operations; **the S-box is the only nonlinear part**
- [[Feistel Cipher]] — the template that makes *any* function invertible; `f` is only ever computed forward; the final swap is what makes decryption reuse the hardware
- [[DES]] — 64-bit block, 16 rounds, 56-bit key; IP/FP, key schedule, mangler (E → XOR → S-boxes → P); weak keys; sound design, key too short
- [[Triple DES]] — why Double DES buys one bit (meet-in-the-middle, 2⁵⁷); why EDE with two keys; 112-bit strength at one third of DES's speed
- [[AES]] — Rijndael; 128-bit block, 128/192/256 key; the 4×4 byte state; SubBytes / ShiftRows / MixColumns / AddRoundKey; not Feistel, and decryption pays for it; 2⁷² times DES
- [[Side-Channel Attacks]] — timing and power; the implementation as target; why they escape every security model

**Modes, integrity, and stream ciphers (from Lecture 3b).** A cipher encrypts one block; using it on a real message is a separate design decision:

- [[Block Cipher Modes of Operation]] — ECB, CBC, OFB, CFB, CTR against four criteria (leakage, manipulation, parallelism, error propagation); **ECB is not secure**, CBC is the most common, CTR is the only one parallel both ways
- [[Initialization Vector]] — public, but must never repeat under one key
- [[Message Authentication Code]] — **no mode provides integrity**; CBC residue as a MAC; separate keys for encryption and authentication
- [[Stream Ciphers]] — the one-time pad with *pseudo*-random; LFSRs; RC4; the two XOR weaknesses
- [[Content Scrambling System]] — DVD encryption failing three independent ways at once; the course's first full post-mortem of a deployed system

**Public key cryptography (from Lecture 5).** The answer to the limitation secret key crypto ended on:

- [[Public Key Cryptography]] — public/private pairs; five applications; the trapdoor one-way function as the design goal
- [[RSA]] — the only algorithm here that encrypts *and* signs; security is the hardness of factoring; four attack classes including the timing attack and blinding
- [[Diffie-Hellman Key Exchange]] — shared secret over a public channel; **no authentication**, hence the man-in-the-middle attack; phone-book mode and DH encryption
- [[Digital Signatures]] — sign with your private key, encrypt with theirs; **non-repudiation is only achievable with public key cryptography**
- [[Public Key Infrastructure]] — CAs, certificates and chains, why a CA can be offline and why that makes revocation hard; the Comodo breach

**Hash functions (from Lecture 4).** The keyless third family, and the primitive the other two lean on:

- [[Hash Functions]] — four properties; weak vs strong collision resistance differ in *who picks the messages*; why ≥128 bits; why encryption makes a poor hash
- [[Birthday Attack]] — the paradox, `k = 1.18√n`, and the **2^(m/2)** bound — a hash's collision resistance is **half** its output length
- [[Hash Function Applications]] — six of them; five add a secret key, a nonce, or both. Commitment protocols, challenge-response, C+H encryption
- [[MD5]] — 128-bit, Merkle–Damgard, four passes, the `sin`-derived T table; broken, with colliding X.509 certificates
- [[SHA-1]] — 160-bit, 80 steps, 16 words expanded to 80; "broken, but not yet cracked" at 2⁶⁹ vs 2⁸⁰
- [[HMAC]] — the extension attack (a Merkle–Damgard digest is a *resumable state*) and the nested fix

**Authentication (from Lecture 6a).** The first unit after cryptography, and a change of subject — the thing verified is a *person*:

- [[User Authentication]] — **identification is a search, authentication is a comparison**; the four bases (know / where / are / have) and why you combine them
- [[Password Authentication]] — store `F(password)`; the password study (86% easily guessed); three dictionary attacks, and **salt only defeats the precomputed one**
- [[S/Key Protocol]] — Lamport's hash: walk the chain forwards to build, backwards to spend; it does **not** authenticate the server
- [[Biometrics]] — **passwords are exact, biometrics are statistical**; not revocable; the multifactor formulas make *both* error rates worse
- [[Authentication Tokens]] — passive tokens can be cloned by reading them, active ones cannot

**OS and system security (from Lecture 7).** Where the OS is attacked — mostly before and around it:

- [[Operating System Security]] — **the boot chain is the attack surface**; hibernation; the **cold boot attack** defeating five full-disk encryption systems without breaking a cipher; the TCB
- [[Access Control Models]] — ACE/ACL; DAC vs MAC and read-down/write-up; closed vs open policy; **Linux pays at check time, Windows at set time**
- [[Unix File Permissions]] — directory bits mean different things; the file-sharing challenge fails twice; setuid is least privilege suspended; octal notation
- [[NTFS Permissions]] — cumulative, explicit-beats-inherited, deny-beats-allow; move vs copy carries permissions the surprising way

**Network security: attack, prevent, detect (from Lectures 12–14).** Three decks that read as one argument. Lecture 12 attacks the protocols Lecture 10 introduced, Lecture 13 puts a checkpoint in front of them, and Lecture 14 watches for what gets past the checkpoint:

- [[Vulnerability Analysis]] — threat / vulnerability / attack; the map of TCP/IP examples. Every one is the same flaw: a protocol accepts a claim it cannot check
- [[Port Scanning]] and [[OS Fingerprinting]] — finding targets; each OS implements its TCP stack differently, and that is a fingerprint
- [[IP Spoofing]] — the source address is never verified; the handshake makes spoofing blind, not impossible
- [[SYN Flooding]], [[TCP Reset Attack]], [[TCP Session Hijacking]] — the three TCP attacks, needing no, some, and exact knowledge of sequence numbers; SYN cookies as the fix for the first
- [[ARP Poisoning]], [[Smurf Attack]], [[ICMP Redirect Attack]] — unauthenticated replies, pings and redirects; reflection and amplification
- [[Firewalls]] — a mechanism enforcing a policy at a choke point; four types and one trade-off table (security 3/2/2/1 against performance 1/2/3/4)
- [[Packet Filtering]], [[Session Filtering]], [[Proxy Firewalls]] — stateless ACLs, state tables, and connection relays; [[FTP]] is the protocol that tells them apart, and [[Network Address Translation]] the side effect that hides hosts
- [[Intrusion Detection Systems]] — prevent, detect, react/survive; two assumptions (observable, distinct) that every weakness violates
- [[Misuse and Anomaly Detection]] — signatures cannot see new attacks; anomaly detection flags new normal behaviour
- [[IDS Performance Metrics]] and [[Base-Rate Fallacy]] — perfect detection plus a 10⁻⁵ false alarm rate still leaves one alarm in three false. The same arithmetic as CSCE 420's [[Bayes Rule]] disease example, and the KB's first link between the two courses
- [[Host-Based Intrusion Detection]] and [[Network Intrusion Detection]] — system-call sequences on the host; a layered event engine on the wire; firewall fail-close against IDS fail-open
- [[Insertion and Evasion Attacks]] — what the IDS sees may not be what the end system gets

**What Lectures 12–14 settle.** Three predictions the KB derived from Lecture 10's protocol slides — the SYN flood, sequence-number prediction, and spoofing-driven reflection — are now taught as attacks, by name, twelve days after they were written down. And one fact turns out to be used three times: *each OS implements its TCP stack differently* is how [[OS Fingerprinting]] identifies a host, why a [[Network Intrusion Detection|network IDS]] cannot be sure what a host will reconstruct, and what a [[Proxy Firewalls|proxy]] removes by rebuilding the connection.

**What Lecture 3 confirms about the course's structure.** The cryptography lecture is not a new subject — it is the design principles instantiated. "Secret keys vs. secret algorithms" *is* [[Security Design Principles|open design]]; [[Cipher Security Models|computational security]] *is* work factor; and *cryptography is rarely the weakest link* restates Lecture 2's claim that defense is more expensive than offense, since the attacker goes after implementation and key management instead. The mathematics is the part that already works — which is the argument for the other three quarters of the syllabus.

**The through-line from 1975 to 2026.** The AI agent material is not a separate subject bolted on. [[OpenClaw]] runs tool calls with `ask=off` by default (fail-safe defaults inverted); its layers each check locally with no unified policy (complete mediation failing at the level of *composition*, exactly the policy-composition hazard [[Security Policy and Mechanism]] warns about); and the durable fix for [[CVE-2024-5565]] is to constrain the tool so a permitted call cannot be repurposed (economy of mechanism and least privilege at the model boundary). [[Prompt Injection]] also gives the cleanest statement of Lecture 2's argument that cryptography is not confidentiality: an encrypted, authenticated pipe delivers the poisoned page **intact**, because *"did this arrive unmodified?"* is an integrity question and *"should the agent act on it?"* is an authorization one.

**The two new units reuse the crypto unit rather than leaving it.** [[Password Authentication|Password storage]] and [[S/Key Protocol|S/Key]] are [[Hash Functions|one-wayness]] in use; crypto-based [[User Authentication|authentication]] is the challenge-response pattern already seen twice; the [[Authentication Tokens|eToken]] holds an X.509 private key and so is a [[Public Key Infrastructure|PKI]] endpoint. And both units supply fresh evidence for the course's central claim: a [[Operating System Security|cold boot attack]] reads the key out of RAM and defeats five full-disk encryption systems with no cipher broken, while the attacks that beat strong passwords — keylogging, fake login prompts, phishing — are not cryptographic at all. [[Cryptography|"Cryptography is rarely the weakest link"]] now has instances in every unit.

**Hashing is the primitive the other two families lean on.** [[Digital Signatures]] sign `H(m)` rather than `m`, so a hash collision *is* a signature forgery — which is exactly what [[MD5]]'s colliding X.509 certificates demonstrated, breaking [[Public Key Infrastructure\|PKI]] at the hash layer with the CA behaving perfectly. [[HMAC]] and the [[Message Authentication Code\|CBC residue]] are the course's two MAC constructions, on hashes and block ciphers respectively, and neither delivers non-repudiation. And **meet-in-the-middle** appears a third time, as a reason not to build a hash from a block cipher.

**What Lecture 5 completes, and what it confirms.** The [[Cryptography Taxonomy|three-family taxonomy]] from Lecture 3 (no key / one key / two keys) is now fully developed. Lecture 5 also *confirms* a claim the KB had derived rather than read: **non-repudiation is only achievable with public key cryptography**, because a [[Message Authentication Code|MAC]] convinces only the other key holder while a [[Digital Signatures|signature]] convinces a third party.

The unit's two real-world post-mortems now bracket the field's central claim from both ends. [[Content Scrambling System|CSS]] failed with weak cryptography *and* bad key management. **Comodo failed with intact cryptography** — the HSMs held, the root keys never leaked, and nine fraudulent certificates for Google, Yahoo, Skype, Live and Mozilla were issued anyway. [[Cryptography|"Cryptography is rarely the weakest link"]] is no longer an assertion in the KB; it has two worked cases.

**The lesson Lecture 3b adds.** A strong cipher wired badly is not a strong system. The same [[AES]] in ECB and in CTR are not equally secure, and **none of the five modes provides integrity** — every one permits some targeted modification, with the keystream modes worst because they permit it with no collateral damage to signal that anything happened. That is the gap [[Message Authentication Code|MACs]] exist to close, and it is why confidentiality and integrity must be treated as independent properties rather than two words for the same thing.

The [[One-Time Pad]]'s key-reuse catastrophe also stops looking like a historical aside: it recurs three times in one deck — the OFB pad warning, the [[Initialization Vector|IV]] uniqueness rule, and the second [[Stream Ciphers|stream cipher]] weakness — because every construction that XORs a keystream against plaintext inherits it.

**What Lecture 3a settles.** Three claims from the earlier lectures now have concrete instances. *Cryptography is rarely the weakest link* — [[Side-Channel Attacks]] break implementations of algorithms with no known weakness. *A large key space is necessary but not sufficient* — [[Triple DES|Double DES]] has 112 bits of key material and about 57 bits of strength. And *computational security erodes* — [[DES]] is architecturally sound and still obsolete, purely because 2⁵⁶ stopped being enough. The lecture also delivers the design theory [[Classical Ciphers]] was missing: substitution alone leaks, transposition alone leaks, and [[Confusion and Diffusion|alternating them many times under per-round keys]] is the entire design of modern symmetric cryptography.

**The one asymmetry that explains the field.** Defense is inherently more expensive than offense, because the attacker needs only the weakest link while the defender must secure every path. Two of the ten design principles (work factor, compromise recording) exist purely to ration defensive effort against that asymmetry, and the whole prevention/detection/recovery split is a response to it.

**Where it connects to the rest of the KB.** CSCE 465 lists [[CSCE 313]] as a prerequisite and reuses it directly: [[Computer Networking]] and [[Data Link Layer]] are the substrate for the network security unit, and [[ARP]] spoofing is already in the KB as an origin-integrity failure — CSCE 313 taught it as a protocol flaw, CSCE 465 names the property it violates and the attack family (fabrication) it belongs to. The lecture's claim that *most TCP/IP protocols were not built with security in mind* is the general form of what the ARP page documents in one protocol. The [[Processes]] / [[Virtual Memory]] / [[File Descriptors]] material underlies the OS security unit, and [[Virtual Memory]] reappears in this course as an instance of least common mechanism. In the other direction the course closes on AI agent security, which touches [[CSCE 420]] and [[CSCE 421]] from a direction neither covers: those courses ask whether a model is *accurate*, this one asks whether it is *attackable*.

## Open Questions / Gaps

### CSCE 411
- Cherry Collecting (Lecture 20): recurrence details visual — not captured by text extraction.
- LP formulations (Lectures 24–25): equation slides visual — see raw PPTX for formal definitions.
- LP Duality: proof of strong duality not captured.
- Lecture 28–29 reduction-construction slides (CIRCUIT-SAT→SAT, SAT→3-SAT, 3-SAT→3-COL gadgets) are visual-only; gadget structures sketched in source pages from prose alone.
- Lecture 31 approximation-ratio analyses (proofs that VertexCoverApprox is a 2-approximation, Greedy Max-Cut is a 1/2-approximation) are visual-only on slides; reasoning sketched in source page.
- CSCE 411 Lectures 1, 3, 12, 13, 14, 17, 21, 30 not yet ingested.

### CSCE 313
- Lectures 3, 4, 13, 17, and others not yet ingested (scheduling, advanced FS, security).
- Many slides are diagram-heavy (memory layouts, CPU diagrams, OS tables) — flagged in source pages.
- x86-64 register table slide (Lecture 1) garbled during text extraction.

### CSCE 465
- Lectures 1–3, 3a, 3b, 4, 5, 6a, 7, 8, 9, 10, 11, 12, 13, 14, a gdb recitation and the HW1 brief are ingested. **Applied cryptography is complete** — secret key, hashes, and public key. **OS and system security is now two decks deep:** Lecture 7 gives the mechanisms (ACLs, DAC/MAC, Unix and NTFS permissions), Lecture 8 the theory (safety undecidability, BLP, Biba, Chinese Wall, RBAC). **Software security opened with Lecture 9** (memory corruption: stack smashing, heap and off-by-one, format strings, and the five defense families). **Network security is five decks deep** — TCP/IP background (10), malware (11), vulnerability analysis (12), firewalls (13) and intrusion detection (14). Still outstanding: **web security**; the AI agent unit is covered early via the homework and has no lecture deck.
- **Lecture 15 is predicted to be web security.** The outline lists *vulnerability analysis; firewalls; intrusion detection; web security*, and Lectures 12–14 followed that order exactly. (The KB's own earlier guess, that intrusion detection would follow malware directly, was wrong; the outline was the better predictor.)
- **Three Lecture 14 passages rest on sources the slides do not cite** — the base-rate example (Axelsson 1999), the layered NIDS architecture (Bro), and insertion/evasion (Ptacek and Newsham 1998). The attributions were made during ingest and are marked as such on each page.
- **Two Lecture 14 figures are only partly recoverable.** The ROC plot has no axis ticks, so the plateau and crossing point on [[IDS Performance Metrics]] are estimates; the anomaly-detection bar chart leaves two of its four measures unlabelled on the slide itself.
- **Lecture 12's six image-only slides were all recovered by rendering** — the stealth-scan captures, the TTL table, the two-SYN comparison, and the IP and ARP header figures. Nothing in that deck is missing from the KB.
- **Lecture 13 names IPSec and explains nothing about it.** No VPN or IPSec material is in the KB.
- **No defences are given in lecture for the smurf or DNS amplification attacks**; the ones on [[Smurf Attack]] are derived and marked.
- **A prediction recorded on 2026-09-01 is closed.** [[Security Threat Landscape|Lecture 2's threat survey]] said malware analysis was one of the course's network security topics, and that botnets had their own slide because of [[Guofei Gu]]'s BotHunter work. Lecture 11 delivered both, BotHunter by name. Same pattern as the Lecture 4 gap: a gap recorded with a testable hypothesis.
- **Lecture 11's measurement plots are caption-only.** The Code Red infection-rate curve, the Paxson Code Red I/II plot, the two Slammer world maps and the Google/MyDoom query graph extract as captions. Their *findings* are recorded; the underlying curves and geographic distributions are not in the KB.
- **Lecture 9 slide 40 was font-mangled** — the source-code-analysis defect list extracted as a substitution cipher and was recovered by rendering the page, not by guessing. All 20 defect classes are on [[Unsafe C Functions]].
- **Only HW1 is in the KB, and only as its briefing deck** — the assignment's own handout (referenced as §7 by the brief) has never been seen, and HW2, HW3 and HW4 are absent. The instructor has told students to study the lecture slides *and the homeworks*, so this is a live gap, not a cosmetic one.
- **Lecture 8 slide 35 is an unanswered in-class exercise** — the BLP lattice cast re-posed under Biba, captioned `?????`. Recorded as open on [[Biba Integrity Model]]; no answer invented.
- The Lecture 4 gap the KB carried from 2026-09-26 to 2026-10-01 is **closed**: Lecture 4 is hashes and message digests, exactly as the course outline predicted.
- **Two new numbering gaps.** Decks now run 1, 2, 3, 3a, 3b, 4, 5, **6a**, 7 — there is no **Lecture 6**, and the **6a** label implies a **6b**. Per the course outline the authentication unit also covers *authentication and security handshake pitfalls*, which is the likely content of 6b. Recorded with that hypothesis, the same way the Lecture 4 gap was.
- Lecture 6a's biometric **"Scorecard From One Study"** (slide 39) is image-only; the comparative ratings are not in the KB. Lecture 7's **"Basic NTFS Permissions"** table (slide 37, 28 images / 272 characters) is likewise image-only, as is the measured/trusted-boot figure. Lecture 7's internal slide numbering also jumps 40 to 42.
- Lecture 4's properties slide annotates both collision-resistance entries with a parenthetical **"(free)"** whose meaning did not survive text extraction; recorded on [[Hash Functions]] rather than guessed at.
- Slides 7–18 of Lecture 1 are image-only (news headlines, incident screenshots, botnet diagram) — the specific incidents cited in lecture are not recoverable. Lecture 2 and the HW1 deck have no image-only slides.
- [[DES]], [[Triple DES]], [[AES]], and all five [[Block Cipher Modes of Operation|modes]] are worked through; IDEA and RC4 are named only. The hash constructions ([[MD5]], [[SHA-1]]) and public-key algorithms ([[RSA]], [[Diffie-Hellman Key Exchange|Diffie-Hellman]]) followed in Lectures 4 and 5.
- **The AES key schedule is still unanswered.** Lecture 3a deferred it ("Q2: how are round keys generated?") and the 3a source page predicted Lecture 3b would cover it; 3b covered modes of operation instead. Both pages corrected. Where it gets answered is unknown.
- Lecture 3b's mode diagrams extract as loose label clouds — the boxes and arrows are lost, the labels survive. The diagrams on the derived pages were reconstructed from labels plus property text, not read off the slide; the raw deck is authoritative for exact figure layout.
- Lecture 3a's DES permutation tables (IP, PC-1, PC-2, E, S1, P) extracted with their row structure scrambled; first rows are on [[DES]], the complete tables are in the raw slides or the textbook. The S1 worked example survived intact.
- Two Lecture 3a slides are borrowed from Peng Ning's NC State course (watermarked); noted on the source page for provenance.
- Lecture 3's English letter-frequency histogram and the `letter` program output (slides 17–18) are image-only — the actual frequency distribution is not in the KB. The permutation-cipher worked example on slide 20 is partially garbled by text extraction.
- Four questions Lecture 3 poses and does not answer are recorded with *derived* answers, each marked as derived: compression-before-encryption ordering, the brute-force recognition problem, the bit length of a mono-alphabetic key, and why an OTP key cannot be reused.
- The [[OpenClaw]] advisory distribution beyond the four largest interface categories exists only in a pie chart and was not extractable. The instructor's paper (Suwansathit, Zhang & Gu, 2026) would close that gap and is assigned reading; it is not in the KB.
- Three discussion questions Lecture 2 poses and does not answer are recorded on its source page (switched-network sniffing, where else caching breaks complete mediation, whether root violates least privilege). They read like exam prompts.
- The HW1 deck labels two different sections "Part 4" and titles a three-phase diagram "6 stages"; both recorded rather than guessed at.

### CSCE 420
- All eight lectures plus both practice exams and the SOM notebook are ingested. Several concept pages **predate** the lecture ingests — they were reconstructed from the practice exams plus standard R&N material before the slides arrived — so where a page's framing differs from the instructor's, the lecture source page is authoritative. (Recorded on [[CSCE 420]].)
- Both practice exams ship **without answer keys**. Worked solutions in this KB were derived during ingest and are marked as such on each page.
- Final Practice Problem 7(2) is ambiguous as worded; both readings are recorded on [[Neural Networks]] rather than one being asserted.
- Extraction gaps are recorded per deck on each source page. Lecture 1 slides 33–42 are image-only. Lecture 7's figures are almost entirely external images (LeCun's tutorial, colah's LSTM diagrams, Jalammar's transformer illustrations) and are not in the KB. Lecture 6's restaurant dataset table extracted as an unstructured column; its content is captured in prose. Lectures 4 and 8 each end on a LaTeX "Temporary page!" artifact with no content.
- MDPs and HMMs appear in R&N but are mentioned only in passing in the ingested decks ([[Reinforcement Learning]], [[History of AI]]); neither has a page. Whether they are examined is still unknown.

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
