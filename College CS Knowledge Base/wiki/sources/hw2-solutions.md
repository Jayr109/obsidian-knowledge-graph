---
title: "Homework 2 Solutions — Spring 2026"
type: source
tags: [csce411, homework, solutions, decidability, turing-machines]
sources: []
course: CSCE 411
updated: 2026-04-09
---

# Homework 2 Solutions — Spring 2026

**Source file:** `raw/CSCE_411_HW2_Sp26_Solutions (2).pdf`
**Course:** CSCE 411, Spring 2026
**Due:** Monday, February 9, 2026
**Topic:** Decidability

## Problem 1: Decidability Closure Properties

### Part (a): Union of Two Decidable Languages
**Claim:** If L₁ and L₂ are decidable, then L₁ ∪ L₂ is decidable.
**Construction:** Build a new TM M that, on input w:
1. Run M₁ (decider for L₁) on w
2. Run M₂ (decider for L₂) on w
3. Accept if either M₁ or M₂ accepts; reject otherwise

Since both M₁ and M₂ always halt, M always halts — M is a valid decider.

### Part (b): Two Undecidable Languages with Decidable Union
**Example:** Let L₁ be any undecidable language, and let L₂ = Σ* \ L₁ (the complement of L₁).
- L₁ is undecidable by assumption
- L₂ is undecidable (if L₂ were decidable, L₁ would be too by complement closure of decidability)
- L₁ ∪ L₂ = Σ* — trivially decidable (always accept)

This shows undecidability is not preserved under union.

## Problem 2: Semi-Decidable to Decidable

**Claim:** If L and Σ* \ L are both semi-decidable (recognizable), then L is decidable.

**Proof:** Let M₁ semi-decide L and M₂ semi-decide Σ* \ L. Build a decider M for L:
- Simulate M₁ and M₂ in **interleaved** steps on input w
- If M₁ accepts: accept (w ∈ L)
- If M₂ accepts: reject (w ∉ L, since w ∈ Σ* \ L)

**Key insight:** Every string w is in exactly one of L or Σ* \ L, so one of M₁, M₂ must eventually accept w. M always terminates.

**Why interleaving is necessary:** You cannot run M₁ fully first — if w ∉ L, M₁ might loop forever, and M would never reach M₂.

## Problem 3: Surprisingly Decidable

**Language:** SmallHalts = {⟨M⟩ : M has ≤ 411 states, tape alphabet {0,1,⊔}, input alphabet {0,1}, and M(ε) halts}

**Claim:** SmallHalts is decidable.

**Proof:** There are only finitely many TMs satisfying the size constraint (bounded number of states × bounded alphabet × bounded transition function). A decider can:
1. Enumerate all TMs with ≤ 411 states over {0,1,⊔}
2. For each such TM, simulate it on ε for a sufficiently bounded number of steps
3. Determine whether each halts

Since the set of "pretty small" TMs is finite, we can hard-code the answer for each one — or simulate with a known time bound (the busy beaver bound for ≤411-state TMs).

**General principle:** Any language defined by a finite structural property of TM descriptions is decidable.

## See Also

- [[Decidability and Undecidability]]
- [[Turing Reductions]]
- [[CSCE 411]]
