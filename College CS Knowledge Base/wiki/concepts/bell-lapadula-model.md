---
title: "Bell-LaPadula Model"
type: concept
tags: [csce465, security, blp, confidentiality, mls, information-flow]
sources: [csce465-lecture-08-security-theory-policies-and-models]
course: CSCE 465
updated: 2026-10-20
---

**Bell-LaPadula (BLP)** is the canonical confidentiality model: the basis for most [[Multi-Level Security|multi-level security]] systems and the one SELinux MLS implements. [[CSCE 465]] presents it as two access rules plus a theorem, built on top of the lattice of labels. Its slogan is **"no read up, no write down."**

## The Goal

> **Confidentiality policy** — prevent the unauthorized disclosure of information.
>
> - Deals with **information flow**
> - Extensive redundancy in the military makes integrity and availability less of a problem

"Deals with information flow" is the key phrase and the reason BLP needs *two* rules rather than one. Stopping a subject from reading a secret is the obvious half; stopping a cleared subject from *copying* that secret somewhere a lower subject can read is the half people forget.

## Labels

From [[Multi-Level Security|MLS]]: subjects have a security clearance `L(s)`, objects a security classification `L(o)`, and in the lattice model each is a pair `(L, C)` with a category set. **(L, C)** dominates **(L′, C′)** when `L′ ≤ L` and `C′ ⊆ C`.

## Rule 1 — The Simple Security Condition

> **Information flows up, not down.** "Reads up" disallowed, "reads down" allowed.
>
> **Simple Security Condition:** subject *s* can read object *o* iff `L(o) ≤ L(s)` and `C(o) ⊆ C(s)`, and *s* has permission to read *o*.
>
> Sometimes called the **"no reads up"** rule.

Restated: *s* may read *o* only if *s*'s label **dominates** *o*'s. The trailing clause — *and s has permission to read o* — is easy to skip and matters: BLP is a **restriction layered on top of** ordinary [[Access Control Models|discretionary permissions]], not a replacement for them. Dominance is necessary, not sufficient.

## Rule 2 — The *-Property

> **Information flows up, not down.** "Writes up" allowed, "writes down" disallowed.
>
> **\*-Property:** subject *s* can write object *o* iff `L(s) ≤ L(o)` and `C(s) ⊆ C(o)`, and *s* has permission to write *o*.
>
> Sometimes called the **"no writes down"** rule.

> **Why write-up is allowed at all, derived.** It looks wrong — a Confidential user appending to a Top Secret file cannot verify what they wrote and cannot read it back. But the model is protecting *secrecy*, not accuracy, and writing up leaks nothing: information moves from a low compartment into a high one, which is the safe direction. The cost is that BLP permits a low-clearance subject to **corrupt** a high-clearance file, a blind write with no read-back. That is precisely the hole [[Biba Integrity Model|Biba]] exists to close, and precisely why the two models are duals rather than the same model twice.

## The Basic Security Theorem

> If a system is **initially in a secure state**, and **every transition** of the system satisfies the simple security condition and the \*-property, then **every state** of the system is secure.

This is an induction over reachable states, and it is the payoff for adopting a [[Security Models|model]] instead of a free-form policy. The [[Safety Problem|general safety question is undecidable]]; inside BLP it is a two-line proof. The model earns that by being too weak to encode a Turing machine — the price of the guarantee.

## Worked Example — Can DocC Leak to Bob?

The lecture poses this against its lattice (slide 28) and leaves it as an in-class question:

| Subject | Label | | Object | Label |
|---|---|---|---|---|
| Bob | (CONFIDENTIAL, {INTEL}) | | DocA | (CONFIDENTIAL, {INTEL}) |
| Alice | (SECRET, {CRYPTO, NUC}) | | DocB | (SECRET, {CRYPTO}) |
| Charlie | (TOP SECRET, {CRYPTO, NUC, INTEL}) | | DocC | (UNCLASSIFIED, {NUC}) |

Who may read what, by dominance:

| | DocA (CONF, {INTEL}) | DocB (SEC, {CRYPTO}) | DocC (UNCL, {NUC}) |
|---|---|---|---|
| **Bob** (CONF, {INTEL}) | yes | no — clearance too low | **no** — NUC not in {INTEL} |
| **Alice** (SEC, {CRYPTO, NUC}) | no — INTEL missing | yes | yes |
| **Charlie** (TS, all three) | yes | yes | yes |

> **Answer, derived — no legitimate flow exists.** Bob cannot read DocC directly: DocC's category NUC is not in Bob's `{INTEL}`, so Bob's label does not dominate it despite DocC being UNCLASSIFIED. The only route left is a reader of DocC writing it somewhere Bob can reach, meaning DocA — the one object Bob can read.
>
> - **Charlie** can read DocC, but writing to DocA needs `L(Charlie) ≤ L(DocA)`: TOP SECRET ≤ CONFIDENTIAL is false. Blocked by the \*-property.
> - **Alice** can read DocC, but writing to DocA needs SECRET ≤ CONFIDENTIAL (false) and `{CRYPTO, NUC} ⊆ {INTEL}` (false). Blocked twice over.
>
> So under BLP the answer is **no**. The caveat worth attaching: this is a statement about the *model*. A [[Side-Channel Attacks|covert channel]] — Charlie modulating a resource Bob can observe — moves information the model does not represent, and BLP says nothing about it. [[Safety Problem|Safety is not security]].

## Where It Runs

**SELinux MLS** implements BLP to control information flow using strict confidentiality and sensitivity labels. That is the mainstream deployment; BLP also underlies the evaluation criteria that classified military systems are built against.

## See Also

- [[Multi-Level Security]]
- [[Biba Integrity Model]]
- [[Security Models]]
- [[Chinese Wall Model]]
- [[Safety Problem]]
- [[Access Control Matrix]]
- [[Access Control Models]]
- [[CIA Triad]]
- [[CSCE 465]]
