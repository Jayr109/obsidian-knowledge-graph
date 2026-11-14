---
title: "CSCE 420 Spring 2026 — 03-04 Midterm Review, Bayesian Updating, Belief Networks"
type: source
tags: [csce420, lecture-recording, spring-2026, midterm-review, causal-diagnostic, perception-illusions, bayesian-updating, conditional-independence, belief-networks, burglary-alarm]
sources: []
course: CSCE 420
semester: Spring 2026
date: 2026-03-04
deck: slide05
exam: midterm / final
updated: 2026-09-17
---

Spring 2026 lecture, 50 min. Two minutes of midterm review, then the Bayesian core of the probability deck: the ratio form of Bayes rule, perception as inference (hexagon/cube, the dragon illusion), Bayesian updating with multiple evidence, conditional independence, and the belief-network definition through the burglary example. Slides 05:30–48. Two days before the midterm.

## The Midterm Review Portion (0:00–2:20)

He opened the Canvas Midterm Review page — the same page captured frame-by-frame on [[CSCE 420 Midterm Review]]. Spoken summary: slide 1, don't spend time, see the practice exam; slide 2 — uninformed, informed, iterative improvement, CSP, game playing and pruning, probabilistic games — *"all potential topics"*; slide 3 — propositional logic and theorem proving, CNF especially, *"apply the resolution algorithm, that's included"*; FOL partly, but *"the not-covered part is resolution-based theorem proving in first-order logic."* *"Review your homework questions"* — HW2 solutions released that day; he had walked through them on 02-27 and *"almost gave out the answers."*

## Bayes Rule as a Ratio

To decide between causes C₁ and C₂ for an effect E, you never need P(E): *"divide this by this and these two cancel out because they're the same for the same effect."* P(C₁|E)/P(C₂|E) = P(E|C₁)P(C₁) / P(E|C₂)P(C₂) — compare to 1. *"So you just need the likelihood and the prior — these two are very easy to compute."*

## Perception as Bayesian Inference

**Hexagon or wireframe cube?** A flat hexagon and a 3D wire cube viewed from exactly the right angle project to the same image. P(hexagon|image) vs P(cube|image) reduces to comparing P(image|hexagon)·P(hexagon) with P(image|cube)·P(cube). The **likelihood** favors the hexagon overwhelmingly — a hexagon produces that image from *many* viewing angles, the cube from only **8**. So unless cubes vastly outnumber hexagons in your world, you see a hexagon. *"If cubes occurred a lot in our environment, you'd most likely say it's a cube."*

**The dragon illusion**: a folded paper dragon that appears to follow your gaze and protrude toward you, but is actually **concave**. *"Even though you know it's concave, whenever you move it looks like this."* The prior on convexity is so strong — *"we are so used to objects protruding toward you"* — that it overrides the geometry. Illumination illusions work the same way.

**Why P(image|object) is the tractable direction**: object → image is **one-to-one**, the causal mechanics. Image → object is **one-to-many — actually one-to-infinite**: he drew wires hung in 3D space that project to the same hexagon from one viewpoint, of which there are infinitely many arrangements. Diagnosis runs against the causal grain; that is why it needs Bayes rule.

## Bayesian Updating

Evidence arrives sequentially — rain given umbrella, then given a second observation. Naively, P(cavity | toothache ∧ catch) by Bayes rule needs P(toothache ∧ catch | cavity), *"entirely not obvious how you'd compute that."* (A **catch** is the dental probe snagging on a cavity.) The individual likelihoods P(toothache|cavity), P(catch|cavity) are easy; the joint is not.

Applying Bayes twice yields a factor **P(catch | toothache ∧ cavity)** — effect₁ given effect₂ and cause. *"Can you arbitrarily drop toothache to get P(catch|cavity)?"*

## Conditional Independence

**Yes — if catch and toothache are conditionally independent given cavity**: P(catch | toothache, cavity) = P(catch | cavity), written Catch ⊥ Toothache | Cavity. Justification: *"cavity is the common cause of both. Cavity is a very strong indicator of catch; toothache does not add much information."*

**Not independent without the condition.** Definition of plain independence: P(X∧Y) = P(X)P(Y), equivalently P(X|Y) = P(X). His test: *"What's the probability the probe will catch? You hope very low. Now you feel toothache — would you revise it? It goes up."* So catch and toothache are dependent — until cavity is known, when *"they will actually become independent."*

**The payoff**: P(cavity | toothache, catch) = α · P(cavity) · P(toothache|cavity) · P(catch|cavity), and each further symptom — bad breath — multiplies in one more easy factor. The normalizer α = 1/P(toothache ∧ catch ∧ …) *"you don't need to compute at all if you're comparing cavity true vs. false — it cancels."* General form: P(Z | E₁, E₂, …) ∝ P(Z) Π P(Eᵢ | Z).

## Belief Networks — Definition

Probabilistic reasoning here means *"determining the exact probability of a specific conditional or joint probability."* A **belief network** represents dependencies between random variables as a **directed acyclic graph**: nodes are variables, directed edges encode conditional (in)dependence, and each node carries a **conditional probability table**. A missing edge is an independence assertion: with A → B and A → C but no B–C edge, P(B | A, C) = P(B | A).

**The alarm network**: Burglary, Earthquake → Alarm → JohnCalls, MaryCalls — neighbors who call you at work if they hear it (*"prior to any internet-connected alarm systems"*). The structure says **P(JohnCalls | Burglary, Earthquake, Alarm, MaryCalls) = P(JohnCalls | Alarm)** — the alarm is his most immediate cause. First query posed: both John and Mary call, but no burglary and no earthquake — the false-alarm joint. Five Boolean variables → 2⁵ = 32 combinations. Continues after spring break. See [[Bayesian Networks]].

## See Also

- [[CSCE 420 Spring 2026 — 03-02 Probability, Bayes Rule]]
- [[CSCE 420 Spring 2026 — 03-16 Belief Network Inference]]
- [[CSCE 420 Midterm Review]]
- [[Bayesian Networks]]
- [[CSCE 420]]
