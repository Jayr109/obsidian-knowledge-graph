---
title: "CSCE 420 Spring 2026 — 02-23 Cheat Sheet Rules, Prover Demo, Prolog"
type: source
tags: [csce420, lecture-recording, spring-2026, midterm-rules, cheat-sheet, theorem-prover-demo, lisp, unit-preference, domain-independence, answer-extraction, prolog, wumpus-world]
sources: []
course: CSCE 420
semester: Spring 2026
date: 2026-02-23
deck: slide03, slide04
exam: midterm / final
updated: 2026-09-17
---

Spring 2026 lecture, 49 min. The midterm cheat-sheet rules, a live demo of his own Lisp resolution prover with step counts, the pros-and-cons argument reduced to one cause, answer extraction, a Prolog demo, and the opening of Planning. Slides 03:133–145 and 04:1–5.

## Midterm Rules (Spring 2026 — confirm yours)

- **One sheet of handwritten notes**, US letter — *"the same paper you put in your printer. Strictly enforced: not A4, not pages ripped from a notebook."* Both sides. He supplies paper on request.
- **No printed text, no photocopies.** One exception: notes handwritten on an iPad/tablet may be **printed**, at reasonable text size, on one sheet — *"you cannot have two pieces and glue them together."*
- **Range: through the unification example**, page 99 of the logic deck. Full scope on [[CSCE 420 Midterm Review]].

## The Theorem-Prover Demo

His own Lisp resolution prover. Clause format: `(number (positive-literals) (negative-literals))` — so ∀x Hound(x) → Howl(x) is Howl in the positive list, Hound in the negative. Two-pointer method with set of support, so you tell it where the goal clause starts.

| Theorem | Method | Result |
|---|---|---|
| Howling Hound | two-pointer | clause 8 → 23: **15 steps** |
| Customs officials | two-pointer | **~40 steps** — vs. his hand proof of 7 |
| Customs officials | unit preference | **11 steps**; clauses mostly 1–2 literals |
| Howling Hound (one encoding) | unit preference | **failed** — *"it's not exact; when it works it works"*; a second encoding succeeded |

Two lessons he drew: the machine's proof is far longer than a human's because it explores blindly; and unit preference *"can be a little bit unreliable."* Even printed legibly, *"it might be difficult to keep track of what's really the reasoning process."*

## Pros and Cons — One Root Cause

The advantage: universally applicable and **domain-independent** — one prover for every domain.

The disadvantage, traced back: resolution is inefficient *"because it's basically a search algorithm — a breadth-first approach."* Could we make it informed? *"This requires domain knowledge. The reason we cannot use any informed search method is because resolution is **purely syntactic**. It doesn't consider what the predicates mean. A domain-dependent heuristic is impossible."*

**"So it's funny that both the advantage and the disadvantage come from the domain independence."** That sentence is the whole pros-and-cons slide. Plus: contradictions in the axioms prove anything, and proofs are hard for humans to follow.

Aside: the theorem-proving group at UT Austin used provers to **verify CPU floating-point units**.

## Answer Extraction

Yes/no is *"of very limited usage."* For *who is a grandparent of Harmonia?*: the negated goal ¬Grandparent(x, Harmonia) only cancels when x gets bound, so **the binding is the answer** — track the unifier. Mechanically: append **Answer(x)** to the negated goal; it never resolves, rides along collecting bindings, and a clause of only Answer(...) counts as False. Result: Answer(Hera).

**Zeus is also a grandparent.** Zeus fathered Ares, Hera mothered Ares, Ares fathered Harmonia. *"If you run this in Prolog it'll produce all the answers — Hera and also Zeus."* Resolution stops at the first False. See [[Answer Extraction]].

## Prolog

Based on **Horn clauses** — P ∧ Q → R written `r :- p, q.` — *"a little bit limited, but everything is positive and this translates directly."*

**GProlog session**: `[user].` enters data-entry mode (queries alone won't define anything); every clause ends with a **period**; **facts at the top, rules below**; Ctrl-D exits entry; `[dating].` loads a file; `;` retrieves further answers. Lowercase = predicates/constants; **Uppercase = variables**. `write` produces side effects.

**Unification at the prompt**, with the mistake he flagged as common:
- `p(X) = p(john).` → `X = john`.
- `p(X,Y) = p(g(Z),Z).` → first {x/g(z)}, then {z/y} — *"you have to apply this to the term part, so g(z) becomes g(y)."* Result **X = g(Y), Z = Y**. Writing {x/g(z), z/y} without composing is the error. (Prolog may equally answer with y/z; both are valid unifiers.)
- `p(X) = p(f(X)).` → *"cannot display cyclic term"* — the occurs check; the algorithm requires a variable that does not occur in its term.

**SWI-Prolog online (swish)**: fine for testing, *"but it doesn't save any of the programs, so don't use it to do your homework."* HW3 was previewed: a Prolog family-tree problem. See [[Prolog]].

## Planning — First Slides

*"You have a goal; you come up with a series of actions to achieve it. That's planning in one sentence."* Search-based, logic-based, and nowadays neural approaches. The [[Wumpus World]] introduced: percepts (breeze, stench, glitter, bump, scream), penalties, the arrow. Continued next lecture; see [[CSCE 420 Lecture 4 — Planning]].

## See Also

- [[CSCE 420 Spring 2026 — 02-20 FOL Resolution, Strategies]]
- [[CSCE 420 Spring 2026 — 02-25 Planning]]
- [[CSCE 420 Fall 2025 — Midterm Review Recording]]
- [[Prolog]]
- [[CSCE 420 Midterm Review]]
- [[CSCE 420]]
