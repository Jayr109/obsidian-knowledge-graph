---
title: "Security Models"
type: concept
tags: [csce465, security, policy, models, blp, biba, chinese-wall, rbac]
sources: [csce465-lecture-08-security-theory-policies-and-models]
course: CSCE 465
updated: 2026-10-20
---

A **security model** is the language you write a [[Security Policy and Mechanism|security policy]] in. [[CSCE 465]] introduces the idea with a question that sounds like syntax and is actually the course's answer to the [[Safety Problem|undecidability of safety]]: *what language should I use to express policy?*

> A **security model** is a model that represents a particular policy or set of policies.
>
> - Abstracts details relevant for analysis
> - Focuses on specific characteristics of policies

## Why a Model Rather Than a Policy

An arbitrary policy over the [[Access Control Matrix|access control matrix]] is expressive enough to be undecidable. A model fixes the *shape* a policy may take — labels and a comparison rule, or roles and a permission map — and in exchange the questions you care about become answerable. The [[Bell-LaPadula Model|Basic Security Theorem]] is the payoff: an inductive guarantee over *all* reachable states, which no free-form policy can offer.

This is the same move as choosing a type system over arbitrary runtime checks. You give up saying some things in order to be able to prove things about everything you can still say.

## Types of Security Policies

The lecture's taxonomy, which cuts along what the policy *protects*:

| Policy type | Primarily protects |
|---|---|
| **Military (governmental)** security policy | [[CIA Triad\|Confidentiality]] |
| **Commercial** security policy | [[CIA Triad\|Integrity]] |
| **Confidentiality** policy | Confidentiality *only* |
| **Integrity** policy | Integrity *only* |

The military/commercial split is the useful one and it is not arbitrary. The lecture's reason for the military side: *extensive redundancy in the military makes integrity and availability less of a problem* — if the document is replicated and the chain of command is duplicated, losing or corrupting a copy is survivable, while disclosing one is not. Commerce inverts the stakes: a bank's balances are not secret from the bank, but they must be right.

## The Four Models in This Lecture

Each specializes in a different characteristic, and the specialization is the point:

| Model | Focus | Rule |
|---|---|---|
| [[Bell-LaPadula Model\|Bell-LaPadula]] | **Secrecy** | No read up, no write down |
| [[Biba Integrity Model\|Biba]] | **Integrity** | No read down, no write up |
| [[Chinese Wall Model\|Chinese Wall]] | **Conflict of interest** | What you have already read restricts what you may read next |
| [[Role-Based Access Control\|RBAC]] | **Jobs** | Access depends on function, not identity |

BLP and Biba are formal duals over a lattice. Chinese Wall is the odd one: it is the only model here whose permissions **change as the subject acts**, and it addresses confidentiality and integrity equally. RBAC is the only one that is primarily an administrative structure rather than an information-flow rule.

> **These are not alternatives you pick between, derived.** A real system runs several at once — SELinux implements BLP-style MLS, the filesystem underneath it is still [[Access Control Models|DAC]], and the organization layered on top is almost certainly RBAC. The models answer different questions, so they compose by stacking rather than competing. The caution from [[Security Policy and Mechanism|Lecture 2]] applies with force here: *when two policies are combined and they conflict, the discrepancies themselves create vulnerabilities.*

## What a Model Does Not Give You

A model is an abstraction of the policy, and [[Safety Problem|safety is not security]]. Proving a policy safe in BLP says nothing about whether the implementation has a buffer overflow, whether the labels were assigned correctly, or whether a [[Side-Channel Attacks|covert channel]] moves information the model cannot see. Models constrain the *authorized* flows; they are silent about flows the model does not model.

## See Also

- [[Safety Problem]]
- [[Access Control Matrix]]
- [[Bell-LaPadula Model]]
- [[Multi-Level Security]]
- [[Biba Integrity Model]]
- [[Chinese Wall Model]]
- [[Role-Based Access Control]]
- [[Access Control Models]]
- [[Security Policy and Mechanism]]
- [[CIA Triad]]
- [[CSCE 465]]
