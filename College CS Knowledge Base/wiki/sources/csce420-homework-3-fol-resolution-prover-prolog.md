---
title: "CSCE 420 Homework 3 — FOL, Resolution Prover, Prolog"
type: source
tags: [csce420, homework, hw3, first-order-logic, resolution, set-of-support, level-saturation, prolog, unicorn, fall-2026]
sources: []
course: CSCE 420
semester: Fall 2026
exam: final
updated: 2026-11-04
---

Homework 3 of the user's **Fall 2026** section. 100 points, 3 problems — one written FOL resolution proof, one Python prover, one Prolog knowledge base. Archived as `raw/CSCE420_HW3_Fall2026.pdf` with the starter notebook `raw/CSCE420_HW3_Fall2026_resolution.ipynb` and its later replacement `raw/CSCE420_HW3_Fall2026_resolution-fixed.ipynb`.

> **No key had been released as of the 2026-11-04 export, so this is treated as live.** The sheet gives no due date; check Canvas. This page records what is *asked* and the conventions the sheet fixes. It does not contain solutions — that is the student's own work. HW1 and HW2 are past due and their released keys are at [[CSCE 420 Homework 1 Solutions — Fall 2026]] and [[CSCE 420 Homework 2 Solutions — Fall 2026]].

> **Exam scope: `final`, not midterm.** The midterm stops at **unification**, Deck 3 slide 99 — see [[CSCE 420 Midterm Review]]. Everything here (FOL resolution proofs, the prover, Prolog) sits past that cutoff, and the final guarantees **one FOL theorem-proving question**. In Spring 2026 this assignment was walked through on 03-18, after that semester's midterm — see [[CSCE 420 Spring 2026 — 03-18 HW3 Walkthrough, Machine Learning Intro]].

## Submission Requirements

- **`resolution.ipynb`** plus **at least 3 revision screenshots** showing major revisions.
- **`family.pl`** plus **`family-results.txt`** (queries and their output). **No revision screenshots needed for the Prolog part.**

## Problem 1 — FOL Resolution Proof (Written, 30 pts)

Three steps, all required: **(1) translate to FOL, (2) convert to canonical form, (3) prove by resolution.**

Premises:
1. Every kid likes Snoopy.
2. Everyone who likes Snoopy likes all beagles.
3. Underdog is a beagle, and Underdog is a superhero.
4. Every superhero can fly or time travel.
5. No beagle can time travel.
6. Garfield does not like all things that can fly.

Conclusion to derive: **Garfield is not a kid.**

**Fixed predicate set** (shorthand in parentheses): `Kid(x)` (K), `Likes(x,y)` (L), `Beagle(x)` (B), `Super(x)` (S), `Fly(x)` (F), `Time(x)` (T); constants **Snoopy**, **Underdog**. Garfield is a constant too.

Two translation patterns the sheet hands you:
- *"Every cat loves all catnips"* → `∀x(Cat(x) → (∀y(Catnip(y) → Loves(x,y))))` — the nested-implication shape, which premises 1 and 2 both need.
- *"There does not exist a black swan"* ≡ *"All swans are not black"*: `¬∃x(Swan(x) ∧ Black(x))` ≡ `∀x(Swan(x) → ¬Black(x))` — the pattern for premise 5, and for reading premise 6 correctly.

Premise 6 is the one to read slowly: *does not like **all** things that can fly* negates a universal, so it yields an **existential** — something that flies which Garfield does not like — and skolemizes to a constant. Reference link given for general story→FOL translation: `cs.utexas.edu/users/novak/reso.html`.

## Problem 2 — Resolution Theorem Prover (Programming, 40 pts)

Propositional logic only. `resolve()`, `null_p()`, `mk_unique()` and the clause representation are **provided**; *"the only part you need to implement is the `prover()` function."*

Clause representation (unchanged from the Spring walkthrough): `[<positive-list>, <negative-list>]`, so `P ∨ Q ∨ ¬R` is `[['p','q'], ['r']]`. **Propositions are case sensitive.** A theorem is a list of `[<index>, <clause>]` pairs.

### The algorithm — two-pointer / level saturation with set of support

1. **Initialize** so you get the **set-of-support strategy**: inner pointer at the **front of the clause list**; outer pointer at the **first clause coming from the negated conclusion**.
2. **Resolve** the two pointed-at clauses:
   - produce the resolvent, append it to the clause list, print it;
   - **before appending, check whether the same clause is already in the list — if so, do not add it**, *"since doing so can lead to an infinite loop"*;
   - if the resolvent is the **empty clause**, stop and return **"success"**.
3. **Advance**: inner pointer forward one. If the **outer** pointer runs past the last clause, stop and return **"failure"**. If inner has not caught up to outer, go resolve. Otherwise reset inner to the front, advance outer by one, and go resolve.

See [[Resolution Strategies]] for why set-of-support keeps the search goal-directed, and [[Resolution]] for the rule itself.

### Testing requirement

1. The **default theorem** in the skeleton.
2. The **Unicorn theorem** from `slide03-logic.pdf`, entered as a new theorem, with premises `M → I`, `¬M → (¬I ∧ L)`, `(I ∨ L) → H`, `H → G`. **Test all three possible conclusions — M, G, H — one at a time**, remembering to negate each. A conclusion that cannot be proved returns **failure**, which is a valid result to report. Convert to CNF first.
3. For **every** case, report **how many new clauses were generated** before deriving the empty clause or failing.

## Problem 3 — Prolog Family Knowledge Base (Programming, 30 pts)

British royal family tree. Three access routes offered: `sun.cs.tamu.edu` with `gprolog`; the `tau-prolog.org/sandbox/` web sandbox (*"does not save your code when you close the browser"* — type it locally first); or a local GNU Prolog install. Workflow: save `family.pl`, run `gprolog`, enter `[family].` — *"don't forget that '.' at the end"* — then query.

**Syntax rule stated in bold**: variables are **upper case**; predicates, functions and constants are **lower case**.

**The family tree** (from the sheet's figure, using the sheet's spelling of *Camila*):

| Relation | People |
|---|---|
| Married | Charles and Camila; William and Catherine; Harry and Meghan |
| Divorced | Charles and Diana |
| Children of Charles and Diana | Prince William, Prince Harry |
| Children of William and Catherine | Prince George, Princess Charlotte, Prince Louis |
| Child of Harry and Meghan | Archie Harrison |

The sheet's tree prints Charles as Prince of Wales, struck through with "King" handwritten beside it.

**Task 1 — facts only**: `male()`, `female()`, `spouse()`, `parent()`, taken straight from the tree, using the **black bold text (first line)** of each tree node as the constant.

| Domain rule | Effect |
|---|---|
| `parent()` is **biological only** | Camilla is not a parent of William |
| `spouse()` includes **current and divorced** | both Diana and Camilla are spouses of Charles |
| `grandparent()` tracks **biological ancestry only** | step-relations do not propagate |
| **Do not** define helper predicates such as `divorced` | — |
| Only basic constructs — **no `dynamic`, `assertz`, `retract`** | — |

**Task 2 — twelve rules**, in the sheet's order, where `relation(X,Y)` means *X is a `relation` of Y*: `mother`, `father`, `brother`, `sister`, `sibling`, `nephew`, `niece`, `grandparent`, `stepmother`, `cousin`, `uncle`, `aunt`. Two hints given: **`X \== Y`** is needed in some rules (without it `brother(X,Y)` makes everyone their own brother — the trap called out in the Spring walkthrough), and *"as you go along, use rules defined above it as much as possible."*

**Task 3 — nine queries**, answered **only with predicates defined in the KB**, with results saved to `family-results.txt`:

1. Grandchildren of Charles. 2. Who is married to Prince William's brother. 3. Uncle of Princess Charlotte. 4. Aunt of Archie Harrison. 5. Nephews of Prince Harry. 6. Stepmother of Prince William. 7. Who has siblings. 8. Who has a female cousin. 9. Who has a niece.

**Check the operator when you run it:** the sheet prints the not-identical test as `X \\== Y`, but standard Prolog's operator is `\==`. The double backslash looks like a typesetting artifact.

See [[Prolog]].

## The Fixed Notebook

A later export replaced `resolution.ipynb` with `resolution-fixed.ipynb`, although the sheet still uses the old name. The diff is four lines, and **no logic changed**: the docstrings and the `\/` strings in the clause printer became raw strings, which silences Python's invalid-escape warning. Code started on the old notebook does not need redoing.

## See Also

- [[CSCE 420 Homework 2 — Game Playing, Logic]]
- [[CSCE 420 Spring 2026 — 03-18 HW3 Walkthrough, Machine Learning Intro]]
- [[CSCE 420 Final Review]]
- [[Resolution]]
- [[Resolution Strategies]]
- [[Prolog]]
- [[CSCE 420]]
