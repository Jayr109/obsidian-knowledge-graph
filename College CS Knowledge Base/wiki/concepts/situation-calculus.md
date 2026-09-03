---
title: "Situation Calculus"
type: concept
tags: [csce420, planning, logic, actions, frame-problem]
sources: [csce420-final-practice, csce420-lecture-04-planning]
course: CSCE 420
updated: 2026-09-01
---

Situation calculus is a first-order formalism for reasoning about **actions and change**. Ordinary [[First-Order Logic]] describes a static world; situation calculus adds a *situation* argument to every changeable predicate so the same fact can be true at one point in time and false at another.

## Vocabulary

- **Situation** $s$ — a snapshot of the world; a term, not a time index.
- $Result(a, s)$ — the situation resulting from performing action $a$ in situation $s$.
- $Poss(a, s)$ — it is possible to execute action $a$ in situation $s$.
- **Fluent** — a predicate whose truth depends on the situation, e.g. $At(Agent, x, s)$.

## The Two Basic Axiom Types

| Axiom type | Shape | Answers |
|---|---|---|
| **Possibility axiom** | *preconditions* $\Rightarrow Poss(a,s)$ | When *can* the action be done? |
| **Effect axiom** | $Poss(a,s) \Rightarrow$ *what changes in* $Result(a,s)$ | What *happens* if it is done? |

The reliable test is where $Poss$ sits. If $Poss$ is on the **right** of the implication, preconditions are being established, so it is a possibility axiom. If $Poss$ is on the **left**, possibility is assumed and consequences follow, so it is an effect axiom. Effect axioms are also identifiable by containing a $Result(\cdot,\cdot)$ term.

## Worked Example (Final Practice, Problem 2)

$x$ and $y$ are locations.

**1.** $Poss(Go(x,y), s) \Rightarrow At(Agent, y, Result(Go(x,y), s))$

$Poss$ is the antecedent and the consequent describes the state after $Result(\cdot)$ — "if going is possible, then afterwards the agent is at $y$." → **Effect axiom**

**2.** $At(Agent, x, s) \land Adjacent(x,y) \Rightarrow Poss(Go(x,y), s)$

The antecedent lists preconditions (agent is at $x$, and $y$ is adjacent to $x$) and the consequent is $Poss$. → **Possibility axiom**

The problem awards no partial credit, so the $Poss$-position test is worth internalizing.

> Worked here from the problem statement; the practice exam ships without an answer key.

## The Frame Problem

The two axiom types state what changes. What they do not state is everything that *stays the same* — the agent's color does not change when it walks. Writing an explicit frame axiom for every (fluent, action) pair is quadratically many axioms and is the classic **frame problem**. The standard repair is the successor-state axiom, which combines effect and frame information into one biconditional per fluent: a fluent is true after an action iff the action made it true, or it was already true and the action did not undo it.

## From the Lecture

### Purpose

Situation calculus exists to **make a propositional-logic-based planner scalable**. The propositional agent in [[Wumpus World]] needs a separate proposition per location ($Breeze_{x,y}$, $Stench_{x,y}$) and can pursue only a single hard-wired goal. Situation calculus adds objects and relations so that an **arbitrary goal** can be stated and a plan derived.

### The Two Constructs

- **Situations** — logical *terms* denoting a state. Taking action $a$ in situation $S_0$ yields $S_1 = Result(a, S_0)$.
- **Fluents** — functions and predicates that **vary from one situation to the next**: $\neg Holding(Gold_1, S_0)$.

Supporting machinery: atemporal (eternal) predicates such as $Gold(Gold_1)$; the empty action $Result([\,], s) = s$; and action sequences $Result([a|seq], s) = Result(seq, Result(a, s))$.

The recursive definition of sequences is what lets a *plan* be a single logical term.

### Two Tasks

| Task | Definition |
|---|---|
| **Projection** | Deduce the outcome of a **given** sequence of actions |
| **Planning** | **Find** a sequence of actions achieving a desired effect |

Planning stated in Wumpus World:

- Initial: $At(Agent,[1,1],S_0) \land At(G_1,[1,2],S_0) \dots$
- Goal: $\exists seq\; At(G_1,[1,1],Result(seq, S_0))$

The goal is an **existential over action sequences** — so planning becomes theorem proving, and the witness recovered by [[Answer Extraction]] *is* the plan.

### Describing Actions: Two Axiom Types

| Axiom | Form | Says |
|---|---|---|
| **Possibility** | $\text{Preconditions} \rightarrow Poss(a,s)$ | When an action *can* be executed |
| **Effect** | $Poss(a,s) \rightarrow \text{changes that result}$ | What happens when it is |

Wumpus World possibility axioms:

$$At(Agent,x,s) \land Adjacent(x,y) \rightarrow Poss(Go(x,y),s)$$
$$Gold(g) \land At(Agent,x,s) \land At(g,x,s) \rightarrow Poss(Grab(g),s)$$
$$Holding(g,s) \rightarrow Poss(Release(g),s)$$

Effect axioms:

$$Poss(Go(x,y),s) \rightarrow At(Agent,y,Result(Go(x,y),s))$$
$$Poss(Grab(g),s) \rightarrow Holding(g,Result(Grab(g),s))$$
$$Poss(Release(g),s) \rightarrow \neg Holding(g,Result(Release(g),s))$$

### The Catch

These axioms are **not sufficient**. They say what changes but never what stays the same, so the agent cannot prove the gold remained where it was left. That is the [[Frame Problem]], and solving it — via successor-state axioms — is the bulk of the planning lecture.

Reference: Russell & Norvig 10.4.2 (3rd ed.) / chapter 11 (4th ed.).

## See Also

- [[First-Order Logic]]
- [[Logical Inference]]
- [[Symbolic AI]]
- [[CSCE 420]]
