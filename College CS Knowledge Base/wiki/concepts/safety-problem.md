---
title: "Safety Problem"
type: concept
tags: [csce465, security, safety, undecidability, protection-systems, theory]
sources: [csce465-lecture-08-security-theory-policies-and-models]
course: CSCE 465
updated: 2026-10-20
---

[[CSCE 465]] opens its security-theory unit with the most ambitious question the field can ask: **given a computer system, is there a generic algorithm that determines whether it is secure?** The answer is no, and the proof is a reduction from the [[Halting Problem|halting problem]]. Everything downstream — [[Bell-LaPadula Model|BLP]], [[Biba Integrity Model|Biba]], [[Chinese Wall Model|Chinese Wall]], [[Role-Based Access Control|RBAC]] — exists because the general question is closed and the only remaining move is to restrict scope.

## What "Secure" Has to Mean First

The question is unanswerable until "secure" is defined, and the definition is the state-machine one already established in [[Security Policy and Mechanism|policy and mechanism]]:

> A secure system
> - Starts in an authorized state
> - Never enters an unauthorized state
>
> A **breach of security** occurs when a system enters an unauthorized state.

So security is not a property of a snapshot. It is a property of every reachable state — which is exactly the shape of problem that tends to be undecidable.

## Safety vs. Security

The lecture draws a distinction that is easy to slide past and worth pinning down:

| Term | Refers to |
|---|---|
| **Safety** | The abstract **model** |
| **Security** | The actual **implementation** |

And the implication runs **one way only**:

- A secure system corresponds to a model safe with respect to all rights.
- A model safe with respect to all rights **does not ensure** a secure system.

> **Why the implication is one-way, derived.** The model is an abstraction, and an abstraction omits things. A safety proof covers the rights the model names; the implementation also has buffer overflows, [[Side-Channel Attacks|side channels]], misconfigured defaults, and a boot chain that runs before any of the model's rules do. Proving the model safe eliminates one class of failure — *policy that permits what it should not* — and says nothing about the other class, *implementation that permits what the policy does not*. This is the same gap [[Security Assurance|assurance]] exists to close, stated formally.

## The Safety Question

> Does there exist an algorithm for determining whether a protection system **S** with initial state **s₀** is safe with respect to a generic right **r**?

Here "safe" means "secure" for an abstract model. Concretely: can right `r` ever leak to a subject that does not currently hold it, through any sequence of legal operations?

## The Theorem

> **Theorem.** It is **undecidable** whether a given state of a given protection system is safe for a given generic right.

**Proof sketch, as the lecture gives it:** an arbitrary [[Turing Machines|Turing machine]] can be reduced to the safety problem, with the Turing machine entering a final state corresponding to the **leaking of a given generic right**. If the safety problem were decidable, we could decide when the Turing machine halts. The [[Halting Problem|halting problem]] is already known undecidable, so the safety problem cannot be decidable either.

Details are in Matt Bishop, *Introduction to Computer Security* — the lecture cites it rather than reproducing the construction. The result is due to Harrison, Ruzzo and Ullman and the protection system it concerns is the HRU model built on the [[Access Control Matrix|access control matrix]].

> **What the reduction actually encodes, derived.** The access control matrix is general enough to simulate a tape: subjects and objects stand in for cells, and the matrix-modifying commands (`enter`, `create subject`, `create object`, `destroy`, `delete`) play the part of transitions. "Right `r` has leaked" is arranged to mean "the machine reached its final state." The undecidability is therefore not a statement about security being mysterious — it is a statement that a sufficiently expressive protection system is **Turing-complete**, and expressiveness is the thing that costs you decidability. See [[Decidability and Undecidability]].

## Key Points

- **The safety problem is undecidable.**
- **Limiting the scope of systems can make the problem decidable.**

The second point is the whole rest of the lecture. Restricted protection systems — mono-operational commands, take–grant systems, and in practice the fixed-shape lattice models — trade expressive power for an answerable question. A [[Security Models|security model]] is precisely such a restriction: a language deliberately too weak to encode a Turing machine, chosen so that the safety of policies written in it can be argued.

## See Also

- [[Security Models]]
- [[Access Control Matrix]]
- [[Security Policy and Mechanism]]
- [[Security Assurance]]
- [[Bell-LaPadula Model]]
- [[Halting Problem]]
- [[Decidability and Undecidability]]
- [[Turing Machines]]
- [[Computer Security]]
- [[CSCE 465]]
