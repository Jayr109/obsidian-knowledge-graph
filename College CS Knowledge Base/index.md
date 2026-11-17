# Index

Master catalog of all wiki pages. Updated on every ingest and after every filed query.
**Current count:** 493 pages (242 concepts, 65 algorithms, 1 data structure, 6 courses, 6 people, 172 sources, 1 overview) | **Last updated:** 2026-11-16

---

## Overview
- [[Overview]] — High-level synthesis; paradigm comparison table; full algorithm index

## Courses
- [[CSCE 411]] — Design and Analysis of Algorithms; Spring 2026; instructor: Calvin Beideman
- [[CSCE 313]] — Introduction to Computer Systems; instructor: Sandeep Kumar; POSIX/systems programming
- [[Corporate Finance and Valuation]] — undergraduate finance; TVM, NPV, risk, market efficiency; modules 3–12
- [[CSCE 420]] — Artificial Intelligence; instructor: Yoonsuck Choe; R&N 4th ed.; search, logic, probability, learning
- [[CSCE 421]] — Machine Learning; instructor: Shuiwang Ji; linear models -> softmax -> loss functions -> MLPs -> CNNs -> transformers/LLMs
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
- [[Autoencoders]] (CSCE 420 + 421) — input copied to target; bottleneck = compression; hidden code = embedding; self-supervised
- [[Large Language Models]] — masked-LM / next-sentence pretraining, BERT vs GPT, RLHF three steps, agentic AI

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
- [[Unsupervised Learning]] (CSCE 420 + 421) — no teacher; requires redundancy; clustering to feature mapping
- [[Recurrent Neural Networks]] — cycles give memory; the Elman/SRN context layer
- [[Convolutional Neural Networks]] (CSCE 420 + 421) — AlexNet; learned kernels resemble mammalian receptive fields
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
- [[Overfitting]] — the M=9 polynomial; zero training error, garbage between the points
- [[Regularization]] — penalty on weight size; lambda dials between overfit and underfit
- [[Model Selection]] — hyperparameters training error cannot pick; train/validation/test, k-fold CV
- [[Loss Functions]] — six losses unified by the margin y_i s_i; convex surrogates for zero-one
- [[Convexity]] — no local minima that are not global; the criterion that licenses gradient descent
- [[Convolution]] — sliding dot product; box filter, Sobel; (N-F)/stride+1; CNNs learn the kernel
- [[Batch Normalization]] — zero-mean unit-variance per feature, learnable gamma/beta; train vs test differ; FINAL EXAM topic
- [[Activation Functions]] — sign, tanh, ReLU; saturation and the vanishing gradient; dead ReLU
- [[Dropout]] — randomly zero units; redundancy and ensemble views; the add-noise/average-out pattern
- [[Transfer Learning]] — freeze generic early layers, finetune the specific late ones; the 2x2 decision table
- [[CNN Architectures]] — LeNet, AlexNet, VGG, GoogLeNet, ResNet; why 3x3 stacks and why identity shortcuts
- [[Attention Mechanism]] — data-dependent weights; Q/K/V; sqrt(Dk) scaling; multi-head; positional encoding
- [[Eigendecomposition]] — S = QLQ^T for symmetric S; orthogonal matrices; the spectral rank-1 form
- [[Singular Value Decomposition]] — R = USV^T for any matrix; truncated SVD is the best low-rank approximation

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
- [[Cryptography]] — plaintext/ciphertext/key; not compression; Kerckhoffs (secret keys vs secret algorithms); rarely the weakest link
- [[Cryptanalysis]] — ciphertext-only / known-plaintext / chosen-plaintext; brute force cost table; the recognition problem
- [[Cipher Security Models]] — unconditional H(p)=H(p|c), provable (reduction), computational (what everything actually meets)
- [[Classical Ciphers]] — Caesar, mono-alphabetic + frequency analysis, permutation; a large key space is necessary but not sufficient
- [[One-Time Pad]] — Shannon's two requirements; XOR construction; key reuse gives c1 XOR c2 = p1 XOR p2
- [[Cryptography Taxonomy]] — by key count (hash/secret/public) and processing (stream/block); which family delivers which service
- [[Secret Key Cryptography]] — same key both ways; four applications incl. MIC and authentication; 5 key bits per decade; needs out-of-band key agreement
- [[Confusion and Diffusion]] — Shannon's principles; substitution for confusion, permutation for diffusion, alternating; avalanche effect with DES round data
- [[Block Ciphers]] — fixed k-bit blocks; block size trade-off; the seven operations; the S-box is the only nonlinear part; HW vs SW
- [[Side-Channel Attacks]] — timing and power analysis; the implementation as target; escapes every security model's input/output assumption
- [[Block Cipher Modes of Operation]] — ECB/CBC/OFB/CFB/CTR vs four criteria; ECB is not secure; CTR is parallel both ways and random-access
- [[Initialization Vector]] — public but must never repeat under one key; random vs incremental generation
- [[Message Authentication Code]] — MAC/MIC; CBC residue; no mode gives integrity; separate keys for encryption and authentication
- [[Stream Ciphers]] — OTP with pseudo-random; PRNG, LFSR, RC4; no integrity and catastrophic keystream reuse
- [[Content Scrambling System]] — DVD encryption; self-verifying key block, one player key breaks everything, ~16-bit effective key; DeCSS; AACS
- [[Public Key Cryptography]] — public/private pairs; five applications; trapdoor one-way functions; RSA vs DH vs DSA
- [[Digital Signatures]] — sign with private, verify with public; the reversed key direction; non-repudiation needs asymmetry
- [[Public Key Infrastructure]] — CAs, certificates, chains, CRLs; a compromised CA cannot read the past but owns the future; Comodo
- [[Hash Functions]] — message digest; four properties; weak vs strong collision resistance; why >=128 bits; encryption makes a poor hash
- [[Birthday Attack]] — the paradox (k~23), k = 1.18*sqrt(n), the 2^(m/2) bound; collision resistance is half the output length
- [[Hash Function Applications]] — file/user auth, commitment protocols, C+H encryption, message auth, signatures; key + nonce pattern
- [[User Authentication]] — identification is a search, authentication a comparison; four bases; address- and crypto-based
- [[Password Authentication]] — one-way storage; the 86%-guessable study; three dictionary attacks; salt defeats precomputation only
- [[Biometrics]] — six desired qualities; not revocable; passwords are exact and biometrics statistical; multifactor arithmetic
- [[Authentication Tokens]] — passive (copyable) vs active (crypto onboard); design issues; time-synchronized tokens
- [[Operating System Security]] — boot chain as attack surface; BIOS passwords, hibernation, cold boot attack, TCB, event logging
- [[Access Control Models]] — ACE/ACL; DAC vs MAC; closed vs open policy; deny priority; Linux vs Windows evaluation
- [[Unix File Permissions]] — 10-char notation; directory bits differ; setuid/setgid/sticky; root and sudo; octal; POSIX ACLs
- [[NTFS Permissions]] — cumulative ACEs; explicit beats inherited, deny beats allow; inheritance; move vs copy
- [[Safety Problem]] — the general question; safety vs security; undecidability by reduction from the halting problem
- [[Access Control Matrix]] — `P(S,O,R)`; subjects/objects/rights; ACLs and capabilities as its two compressions; DAC/MAC administration
- [[Security Models]] — what a security model is and why one is adopted; policy types; the four-model taxonomy
- [[Multi-Level Security]] — linear levels; the lattice model; categories; `(L,C)` labels and the dominance relation
- [[Bell-LaPadula Model]] — no read up, no write down; simple security condition, \*-property, Basic Security Theorem
- [[Biba Integrity Model]] — no read down, no write up; integrity vs security labels; low-water mark
- [[Chinese Wall Model]] — conflict-of-interest classes and company datasets; CW-simple and CW-\*-property; sanitization
- [[Role-Based Access Control]] — access by job function; static permissions, transient membership
- [[Buffer Overflow]] — writes past allocated memory; the attack's two halves, placement vs jump strategies, three generations
- [[Stack Smashing]] — overflow a local buffer into the saved return address; attack procedure, address guessing, NOP sled
- [[Shellcode]] — `execve("/bin/sh")` as injectable bytes; `int 0x80`, no null bytes, position-independent
- [[Heap and Pointer Overflows]] — off-by-one frame-pointer hijack, heap overflow, function pointers, path traversal
- [[Format String Vulnerabilities]] — `printf(buf)`; the variadic stack walk and `%n` as an arbitrary write
- [[Unsafe C Functions]] — strcpy/strcat/gets/scanf/printf; strncpy and the Apache `htpasswd` fix that was also wrong
- [[Buffer Overflow Defenses]] — correct code, NX, ASLR, bounds checking, pointer integrity, Libsafe
- [[Stack Canaries]] — StackGuard; random vs terminator canaries, PointGuard, and how canaries are bypassed
- [[GDB]] — the GNU debugger; `bt` and `info frame`, and why its output is a map of the stack-smashing target
- [[Internet Protocol]] — unreliable connectionless datagram delivery; protocol numbers, routing tables, why source addresses are never checked
- [[TCP]] — header format; the three-way handshake as reachability proof and state allocation; retransmission
- [[ICMP]] — echo/unreachable/time-exceeded; how ping and traceroute fall out, and why it is a reconnaissance tool
- [[HTTP]] — methods and response categories; `GET /` over telnet; the end-to-end page-load trace
- [[SMTP]] — the MUA/MTA path and wire transcript; sending mail by hand, and why that is email spoofing
- [[Malware]] — the needs-a-host vs independent taxonomy; trap doors, logic bombs, trojans
- [[Computer Viruses]] — four stages, virus structure, macro viruses, polymorphism, four generations of antivirus
- [[Worms]] — propagation without user action; hit-list and permutation scanning; detection and defense
- [[Notable Worms]] — Morris, Code Red I/v2/II, Nimda, Slammer and Blaster/Welchia, in order
- [[Search Worms]] — finding targets by search query; MyDoom, Santy, and Google's result-side countermeasure
- [[Botnets]] — centralized vs distributed C&C, the IRC life-cycle, Storm, and BotHunter dialog correlation
- [[Stuxnet]] — ICS/PLC target, 4 zero-days, 2 stolen certificates, USB across the air gap
- [[Vulnerability Analysis]] — threat / vulnerability / attack; the five typical steps; attackers and defenders use the same tools; map of the TCP/IP examples
- [[Port Scanning]] — ports and nmap; the SYN "stealth" scan — open answers SYN+ACK, closed answers RST+ACK
- [[OS Fingerprinting]] — active vs passive; the FIN probe; initial TTL clusters (64/128/255); two SYNs compared field by field
- [[IP Spoofing]] — the source address is never checked; router filtering and why it is underused; the handshake makes spoofing blind
- [[SYN Flooding]] — half-open connections fill the queue; 90% of DoS attacks; SYN cookies store the state in the sequence number
- [[TCP Reset Attack]] — a forged RST needs only an in-window sequence number: 2^16 guesses, not 2^32
- [[TCP Session Hijacking]] — SYN-flood A, predict B's sequence numbers, finish B's handshake blind as A
- [[ARP Poisoning]] — a forged ARP reply rewrites a host's cache; static entries, port security, arpwatch, RARP; no universal defence
- [[Smurf Attack]] — ping a broadcast address as the victim; spoofing + reflection + amplification; the DNS variant at about 25x
- [[ICMP Redirect Attack]] — a forged type 5 message makes the attacker the gateway; fix is to disable redirects
- [[Firewalls]] — a device enforcing a policy between networks; DMZ; can and cannot; the four types and the comparison table
- [[Packet Filtering]] — stateless per-packet ACLs; ports above 1024 left open; the four-line FTP example and its hole
- [[Session Filtering]] — stateful inspection; decisions per connection; default deny; FTP in two rules
- [[Proxy Firewalls]] — relays, not filters; application gateways vs circuit-level gateways; SOCKS; why TCP proxies well
- [[FTP]] — command and data channels; active vs passive mode; why a negotiated port breaks stateless filters
- [[Network Address Translation]] — many-to-1 and 1-to-1 mappings; hides unaddressable hosts; a side effect, not a policy
- [[Intrusion Detection Systems]] — identifying and responding; prevent/detect/survive layers; two assumptions; the design space
- [[Misuse and Anomaly Detection]] — signatures can't detect new attacks; anomaly detection has high false positives
- [[IDS Performance Metrics]] — confusion matrix; detection, false positive and Bayesian detection rates; the ROC curve
- [[Base-Rate Fallacy]] — perfect detection and a 10^-5 false alarm rate still give only 66%; why where you deploy matters
- [[Host-Based Intrusion Detection]] — OS auditing, BSM, strace; Forrest's short sequences of system calls as a normal profile
- [[Network Intrusion Detection]] — sensors, the layered event architecture, firewall (fail-close) vs IDS (fail-open), eight requirements
- [[Insertion and Evasion Attacks]] — the IDS and the end host reconstruct different streams; bad checksum, TTL, fragment overlap

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
- [[Backpropagation]] — gradient descent through hidden layers; sigmoid derivative trick; CSCE 421 adds the sensitivity delta and the computational graph
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
- [[Multilayer Perceptron]] — XOR forces hidden layers; tanh for differentiability; forward propagation
- [[Principal Component Analysis]] — max variance = min reconstruction error; Ky Fan; computed via SVD of the centered data

## Algorithms — CSCE 465 (Security)
- [[Feistel Cipher]] — block-cipher template; L_{i+1}=R_i, R_{i+1}=L_i XOR f(R_i,K_i); f never inverted; decrypt = same hardware, keys reversed; note the final swap
- [[DES]] — 64-bit block, 16 rounds, 56-bit key; IP/FP, key schedule, mangler (E, S-boxes, P); S-box worked example; weak and semi-weak keys; sound design, key too short
- [[Triple DES]] — Double DES falls to meet-in-the-middle (2^57); EDE with two keys gives ~112-bit strength at 1/3 DES speed
- [[AES]] — Rijndael; 128-bit block, 128/192/256 key; 4x4 byte state; SubBytes, ShiftRows, MixColumns, AddRoundKey; not Feistel; 2^72 times DES
- [[RSA]] — keygen from p,q,phi,e,d; encrypt/decrypt/sign/verify; correctness via Euler; factoring, probable-message, and timing attacks; blinding
- [[Diffie-Hellman Key Exchange]] — g^(SA*SB) mod p over a public channel; discrete log; MITM and how to authenticate; phone-book mode
- [[MD5]] — 128-bit digest; Merkle-Damgard chaining; passes F/G/H/I; T[i]=floor(2^32|sin i|); broken, colliding X.509 certs
- [[SHA-1]] — 160-bit digest; 80 steps; W0..W15 expanded to W79; broken but not cracked (2^69 vs 2^80)
- [[HMAC]] — defeats the extension attack on H(K|M|pad); digest-inside-a-digest with 0x36/0x5c inner and outer pads
- [[S/Key Protocol]] — Lamport's hash; xn=H(x_{n-1}) chain spent backwards; replay-proof but does not authenticate the server

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
- [[CSCE 420 Midterm Review]] — MIDTERM ONLY: Canvas objectives list, scope (Deck 1 one question, Deck 2, Deck 3 through unification), cheat-sheet rules
- [[CSCE 420 Final Review]] — FINAL ONLY: post-midterm material, not cumulative; SOM and AI Ethics excluded; one FOL theorem-proving question
- [[CSCE 420 Homework 1 — Search]] — Fall 2026 HW1: DFS notebook + written search problems; asks and conventions only, no solutions
- [[CSCE 420 Homework 2 — Game Playing, Logic]] — Fall 2026 HW2: minimax/alpha-beta notebook, resolution-rule truth table; 5 cuts (sheet corrected Sep 17 from 4)
- [[CSCE 420 Homework 3 — FOL, Resolution Prover, Prolog]] — Fall 2026 HW3, no key yet: FOL resolution proof (Snoopy/Garfield), two-pointer prover with set-of-support, Prolog royal family; final scope
- [[CSCE 420 Homework 4 — Probability, Learning, Deep Learning]] — Fall 2026 HW4, live: belief network joint, intercausal inference, information gain, perceptron and XOR, gradient descent, LeNet on MNIST; records errors in the sheet; final scope
- [[CSCE 420 Homework 1 Solutions — Fall 2026]] — instructor's released key: DFS/BFS/IDS traces, admissibility table, greedy 93 vs A* 44
- [[CSCE 420 Homework 2 Solutions — Fall 2026]] — instructor's released key: the five alpha-beta cuts, resolution refutation, skolemization and unification tables
- [[CSCE 420 Fall 2026 — 09-18 minmax.ipynb Walkthrough]] — 4-min in-class walkthrough of the HW2 minimax starter: three-case recursion, node type as parameter, printed call trace (midterm scope)
- [[CSCE 420 Fall 2025 — Midterm Review Recording]] — 50-min Fall 2025 review class: scope, Prolog demo, Wumpus walkthrough (midterm scope)
- [[CSCE 420 Fall 2025 — Whiteboard: Perceptron Decision Line]] — 14-min board derivation: threshold rule → line y = −(w1/w2)x + w0/w2; read output by comparing b to a′ (final scope)
- [[CSCE 420 Demo — Rejection Method Animation]] — 37-s silent animation: uniform samples, accept x < 0.3, bars converge to 0.3/0.7 (Deck 5 background)

## Sources — CSCE 420 Spring 2026 Lecture Recordings
- [[CSCE 420 Spring 2026 — 01-12 Syllabus, What Is Intelligence]] — midterm scope; deck slide01
- [[CSCE 420 Spring 2026 — 01-14 Linguistics, Neuroscience, History of AI]] — midterm scope; deck slide01
- [[CSCE 420 Spring 2026 — 01-16 Modern AI, Limitations, Future]] — midterm scope; deck slide01, slide02
- [[CSCE 420 Spring 2026 — 01-21 Uninformed Search]] — midterm scope; deck slide02
- [[CSCE 420 Spring 2026 — 01-23 DFS, DLS, IDS, Informed Search Intro]] — midterm scope; deck slide02
- [[CSCE 420 Spring 2026 — 01-28 Greedy, A*, Heuristics]] — midterm scope; deck slide02
- [[CSCE 420 Spring 2026 — 01-30 IDA*, Iterative Improvement]] — midterm scope; deck slide02
- [[CSCE 420 Spring 2026 — 02-02 Simulated Annealing, CSP, Game Playing]] — midterm scope; deck slide02
- [[CSCE 420 Spring 2026 — 02-04 Alpha-Beta Pruning]] — midterm scope; deck slide02
- [[CSCE 420 Spring 2026 — 02-06 Chance Games, Game AI History, Logic Intro]] — midterm scope; deck slide02, slide03
- [[CSCE 420 Spring 2026 — 02-09 Knowledge Bases, Propositional Logic]] — midterm scope; deck slide03
- [[CSCE 420 Spring 2026 — 02-11 Normal Forms, Logical Consequence, Resolution]] — midterm scope; deck slide03
- [[CSCE 420 Spring 2026 — 02-13 HW2 Walkthrough, First-Order Logic]] — midterm scope; deck slide03
- [[CSCE 420 Spring 2026 — 02-16 Standard Form, Skolemization]] — midterm scope; deck slide03
- [[CSCE 420 Spring 2026 — 02-18 Composition, Unification, Factors]] — straddles the midterm/final boundary — see page note; deck slide03
- [[CSCE 420 Spring 2026 — 02-20 FOL Resolution, Strategies]] — final scope; deck slide03
- [[CSCE 420 Spring 2026 — 02-23 Cheat Sheet Rules, Prover Demo, Prolog]] — straddles the midterm/final boundary — see page note; deck slide03, slide04
- [[CSCE 420 Spring 2026 — 02-25 Planning]] — final scope; deck slide04
- [[CSCE 420 Spring 2026 — 02-27 Exam Rules, Practice Exam Walkthrough, Frame Problem, Uncertainty]] — straddles the midterm/final boundary — see page note; deck slide04, slide05
- [[CSCE 420 Spring 2026 — 03-02 Probability, Bayes Rule]] — final scope; deck slide05
- [[CSCE 420 Spring 2026 — 03-04 Midterm Review, Bayesian Updating, Belief Networks]] — straddles the midterm/final boundary — see page note; deck slide05
- [[CSCE 420 Spring 2026 — 03-16 Belief Network Inference]] — final scope; deck slide05
- [[CSCE 420 Spring 2026 — 03-18 HW3 Walkthrough, Machine Learning Intro]] — final scope; deck slide05, slide06
- [[CSCE 420 Spring 2026 — 03-20 Supervised, Unsupervised, RL Issues]] — final scope; deck slide06
- [[CSCE 420 Spring 2026 — 03-23 Decision Trees, Entropy]] — final scope; deck slide06
- [[CSCE 420 Spring 2026 — 03-25 Information Gain, Neural Networks Intro]] — final scope; deck slide06
- [[CSCE 420 Spring 2026 — 03-30 Perceptron Recap, Gradient Descent, Backprop I]] — final scope; deck slide06
- [[CSCE 420 Spring 2026 — 03-31 Backprop II, Recorded Lecture]] — final scope; deck slide06
- [[CSCE 420 Spring 2026 — 04-06 Demos, Autoencoders, SRN, Genetic Algorithms]] — final scope; deck slide06
- [[CSCE 420 Spring 2026 — 04-08 HW4 Walkthrough, Genetic Algorithms, Neuroevolution]] — final scope; deck slide06
- [[CSCE 420 Spring 2026 — 04-10 NEAT Demos, Deep Learning Intro]] — final scope; deck slide06, slide07
- [[CSCE 420 Spring 2026 — 04-13 Final Practice Walkthrough, Deep CNNs, AlexNet]] — final scope; deck slide07
- [[CSCE 420 Spring 2026 — 04-15 Final Review Posted, CNN Representations, Deep RL, DQN]] — final scope; deck slide07
- [[CSCE 420 Spring 2026 — 04-17 DQN Finished, Recurrent Networks and LSTM]] — final scope; deck slide07
- [[CSCE 420 Spring 2026 — 04-20 LSTM Applications, Attention, Transformers]] — final scope; deck slide07
- [[CSCE 420 Spring 2026 — 04-22 LLMs, Diffusion, Deep Learning Wrap-Up]] — final scope; deck slide07
- [[CSCE 420 Spring 2026 — 04-24 Self-Organizing Maps (Not on Exam)]] — NOT on either exam; deck slide06
- [[CSCE 420 Spring 2026 — 04-27 SOM Evaluation, AI Ethics (Not on Exam)]] — NOT on either exam; deck slide06, slide08

## Sources — CSCE 421 (Machine Learning)
- [[CSCE 421 T01 — Introduction and Linear Regression]] — what needs learning, perceptron hypothesis set, least squares in closed form; 20 slides
- [[CSCE 421 T02 — Logistic Regression for Binary Classification]] — sigmoid, cross-entropy from MLE, gradient descent and SGD; 30 slides
- [[CSCE 421 T03 — Logistic Regression: From Binary to Multi-Class]] — softmax, shift-invariance, K=2 equivalence to sigmoid; 20 slides
- [[CSCE 421 T03 Notes — Softmax Regression Derivations]] — typed notes; softmax Jacobian and the dL/da = p - y result; 6 pages
- [[CSCE 421 T04 — Overfitting and Regularization]] — polynomial curve fitting, RMS curves, lambda penalty, cross-validation; 14 slides (image-heavy)
- [[CSCE 421 T05 — A Unified View of Loss Functions in Supervised Learning]] — zero-one, perceptron, square, log, hinge, exponential on one axis; convexity; 12 slides
- [[CSCE 421 T05 Notes — A Unified View of Loss Functions]] — typed note with Ji, Lei Cai, Hao Yuan; same six losses plus the comparison figures; 4 pages
- [[CSCE 421 T06 — Multi-Layer Perceptron/Networks]] — XOR, universal approximation, forward propagation, sensitivity and backprop; 24 slides
- [[CSCE 421 T07 — Backpropagation by Examples]] — computational graph, upstream x local, gate patterns; 9 slides (CS231n)
- [[CSCE 421 T08 — Convolution]] — image filtering, box filter, Sobel edges; CNNs train the filter parameters; 13 slides (image-heavy)
- [[CSCE 421 T09 — Convolutional Neural Networks]] — conv/pool arithmetic, ReLU, batch norm, dropout, transfer learning, LeNet->ResNet; 127 slides; 46-48 optional
- [[CSCE 421 T10 — Attention, Transformers, and Large Language Models]] — Q/K/V, multi-head, LayerNorm, GPT/BERT/seq2seq, LoRA, prompting; 41 slides
- [[CSCE 421 HW1 Solutions — Linear Models for Handwritten Digits]] — released key; cross-entropy gradient, sigmoid thresholds, softmax vs sigmoid equivalence; 4 pages
- [[CSCE 421 HW2 Solutions — Loss Functions, Backpropagation, MLP]] — released key; worked LFD 7.8 backprop numbers, 661-parameter count; 3 pages
- [[CSCE 421 T11 — Principal Component Analysis and Autoencoders]] — orthogonal matrices, eigendecomposition, SVD, PCA both ways, PCA as a linear autoencoder; 32 slides
- [[CSCE 421 T11 Notes — Principal Component Analysis and Autoencoders]] — typed note; uncentered-reconstruction derivation, gradient-descent-vs-PCA answer, 2 exercises; 8 pages
- [[SOM Notebook — Self-Organizing Maps (2D Grid)]] — NumPy SOM on an n×n grid; BMU, Gaussian neighborhood, decay schedule; three input distributions

## Sources — CSCE 465 (Computer & Network Security)
- [[CSCE 465 Lecture 1 — Course Introduction]] — logistics, grading, mini-research project; security definition, goals, CIA triad; 39 slides (7–18 image-only)
- [[CSCE 465 Lecture 2 — Security Overview]] — the foundations lecture; attack taxonomy, policy/mechanism/assurance, the ten design principles; 50 slides
- [[CSCE 465 HW1 — Build and Threat-Model an AI Agent]] — assignment brief; 120 pts + 200 bonus; AI agent security and prompt injection; 31 slides
- [[CSCE 465 Lecture 3 — Introduction to Cryptography]] — opens applied cryptography; definitions, cryptanalysis, early ciphers, OTP, primitive taxonomy; 29 slides
- [[CSCE 465 Lecture 3a — Secret Key Cryptography (I)]] — Feistel, DES component by component, Triple DES + meet-in-the-middle, AES, side channels; ~63 slides
- [[CSCE 465 Lecture 3b — Secret Key Cryptography (II): Modes of Operation]] — ECB/CBC/OFB/CFB/CTR, IVs, MACs, stream ciphers, CSS/DeCSS post-mortem; ~37 slides
- [[CSCE 465 Lecture 4 — Hash Functions]] — properties, birthday attack, six applications, MD5, SHA-1, HMAC; ~47 slides
- [[CSCE 465 Lecture 5 — Public Key Cryptography]] — RSA, Diffie-Hellman, digital signatures, PKI and CAs, the Comodo breach; ~59 slides
- [[CSCE 465 Lecture 6a — User Authentication]] — four bases, passwords and salt, S/Key, biometrics, tokens; ~46 slides
- [[CSCE 465 Lecture 7 — Operating System Security]] — boot chain, cold boot, DAC/MAC, Unix permissions, NTFS; ~42 slides
- [[CSCE 465 Lecture 8 — Security Theory: Security Policies and Models]] — safety undecidability, BLP, Biba, Chinese Wall, RBAC; 47 slides
- [[CSCE 465 Lecture 9 — Software Security: Buffer Overflow]] — stack smashing, heap/format-string variants, NX/ASLR/canaries; ~47 slides
- [[CSCE 465 Recitation — gdb Basics]] — gdb commands, `bt` and `info frame`, two worked sessions; 11 slides
- [[CSCE 465 Lecture 10 — Network Basics]] — IP, TCP, ICMP, HTTP, SMTP; telnet by hand; 26 slides
- [[CSCE 465 Lecture 11 — Malware]] — viruses, worms, botnets, Stuxnet; 57 slides
- [[CSCE 465 Lecture 12 — Vulnerability Analysis]] — scanning, spoofing, SYN flood, RST, hijacking, ARP poisoning, smurf, ICMP redirect; 60 slides
- [[CSCE 465 Lecture 13 — Firewall]] — packet and session filters, proxies, the FTP example, comparison table, NAT; 34 slides
- [[CSCE 465 Lecture 14 — Intrusion Detection System]] — misuse vs anomaly, base-rate fallacy, HIDS, NIDS, insertion and evasion; 23 slides

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
