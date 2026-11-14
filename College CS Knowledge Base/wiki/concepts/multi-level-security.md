---
title: "Multi-Level Security"
type: concept
tags: [csce465, security, mls, lattice, clearance, categories, dominance]
sources: [csce465-lecture-08-security-theory-policies-and-models]
course: CSCE 465
updated: 2026-10-20
---

**Multi-level security (MLS)** is the labelling scheme underneath [[Bell-LaPadula Model|BLP]] and [[Biba Integrity Model|Biba]]: every subject and every object carries a label, and the decision to allow an access is *computed* by comparing two labels rather than looked up in a table. [[CSCE 465]] presents it in two stages — a linear ordering of clearances first, then the **lattice model** that adds categories.

## Stage One: Linear Levels

Security levels arranged in a linear ordering, as used for physical documents by governments as well as by computers:

```
Top Secret
    ^
  Secret
    ^
Confidential
    ^
Unclassified
```

- **Subjects** have a *security clearance* `L(s)`
- **Objects** have a *security classification* `L(o)`

The lecture's example table:

| Security level | Subject | Object |
|---|---|---|
| Top Secret | Tamara | Personnel Files |
| Secret | Samuel | E-Mail Files |
| Confidential | Claire | Activity Logs |
| Unclassified | Ulaley | Telephone Lists |

- Tamara can read all files
- Claire cannot read Personnel or E-Mail Files
- Ulaley can only read Telephone Lists

## Stage Two: The Lattice Model

> Used by the US military (and many others), the **Lattice model** uses MLS to define policy.

A linear ordering is too coarse: a Top Secret clearance in one specialty should not confer access to an unrelated Top Secret program. So the notion of a security level expands to include **categories** — an unbounded set, of which the lecture uses three:

- **NUC**(lear)
- **INTEL**(ligence)
- **CRYPTO**(graphy)

A security level is then a pair `(clearance, category set)`, written formally **(L, C)** where `L` is the clearance level and `C` is the set of categories. The lecture's running cast:

| Entity | Label |
|---|---|
| Alice | (SECRET, {CRYPTO, NUC}) |
| Bob | (CONFIDENTIAL, {INTEL}) |
| Charlie | (TOP SECRET, {CRYPTO, NUC, INTEL}) |
| DocA | (CONFIDENTIAL, {INTEL}) |
| DocB | (SECRET, {CRYPTO}) |
| DocC | (UNCLASSIFIED, {NUC}) |

## Dominance

The comparison that replaces the table lookup:

> The security level **(L, C)** *dominates* the security level **(L′, C′)** if **L′ ≤ L** and **C′ ⊆ C**.

Two conditions, both required: the clearance must be at least as high **and** the category set must be a superset. This is what makes the structure a **lattice** rather than a chain — labels are only **partially** ordered, because two levels can be incomparable in both directions.

> **Incomparability is the feature, derived.** Alice (SECRET, {CRYPTO, NUC}) and Bob (CONFIDENTIAL, {INTEL}) do not dominate each other: Alice outranks Bob on clearance but lacks INTEL, and Bob holds INTEL but is lower-cleared. Neither can read the other's documents. A linear ordering cannot express that — it would force Alice, as the higher clearance, to see everything Bob sees. **Categories are how "need to know" gets encoded**, and they are why the structure must be a lattice. Worked against the lecture's own labels: Alice vs DocA (CONFIDENTIAL, {INTEL}) — CONFIDENTIAL ≤ SECRET holds, but {INTEL} is not a subset of {CRYPTO, NUC}, so Alice does **not** dominate DocA and cannot read it even though she outranks it on clearance alone.

Charlie, holding (TOP SECRET, {CRYPTO, NUC, INTEL}), dominates every label in the table — he is the top element of this lattice, and the only subject who can read all three documents.

## Why the Labels Matter More Than the Rules

The access rules BLP and Biba build on this are two lines each. The labelling is the hard part in practice: every object must be classified, every subject cleared, and a mislabelled document is invisible to the model — the rules will enforce the wrong thing perfectly. This is the gap between [[Safety Problem|safety and security]] appearing in its most ordinary form, as data-entry error.

## See Also

- [[Bell-LaPadula Model]]
- [[Biba Integrity Model]]
- [[Security Models]]
- [[Access Control Matrix]]
- [[Access Control Models]]
- [[Safety Problem]]
- [[CIA Triad]]
- [[CSCE 465]]
