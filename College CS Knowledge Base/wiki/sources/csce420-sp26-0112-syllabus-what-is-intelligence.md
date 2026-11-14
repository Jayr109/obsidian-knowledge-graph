---
title: "CSCE 420 Spring 2026 — 01-12 Syllabus, What Is Intelligence"
type: source
tags: [csce420, lecture-recording, spring-2026, syllabus, grading, exam-rules, strong-ai, weak-ai, agi, turing-test, chinese-room, philosophy-of-mind, behaviorism, functionalism]
sources: []
course: CSCE 420
semester: Spring 2026
date: 2026-01-12
deck: slide01
exam: midterm
updated: 2026-09-30
---

Spring 2026, **first class of the semester**, 50 min. Syllabus walkthrough, then slide01 from the start: what intelligence is, strong vs. weak AI, and the first related disciplines (philosophy, mathematics, psychology). Slides 01:1–30. Archived at `raw/CSCE420_Spring2026_lecture_transcripts/GMT20260112-*.vtt`.

> Spring 2026 offering — dates and deadlines are that semester's. The **course rules** below were restated in Fall 2026, but verify any number against your own syllabus.

## Course Structure (Spring 2026)

| Component | Weight |
|---|---|
| Midterm | 25% |
| Final | 30% |
| 4 homeworks | 10% each |
| Attendance | 5% |

Midterm is deliberately the lighter of the two *"so that you can make up if you don't do too well during the midterm."* **No curving.** Late penalty **1 point per hour**. Attendance submitted by UIN at a web link; not taken during week 1 because of add/drop churn.

**Exam rule**: *"You may bring one sheet of handwritten notes."* US letter, both sides. The only permitted printed version is notes you **handwrote on a tablet** and then printed — *"in case you don't like to harm the environment."*

**Homework rules**: no collaboration or discussion; **you are required to use the provided data structures and starter code** — *"you cannot use something entirely different"*; AI tools allowed **only** where the sheet explicitly says so, which in Spring was the final deep-learning assignment alone.

Spring dates: midterm **Friday March 6** (right before spring break, *"not negotiable"*); final **Tuesday May 5, 10:30–12:30**, the university-designated slot.

## The Textbook Cover as a Syllabus

He walked the 4th-edition cover and had the class name each element: a **chessboard** with **Garry Kasparov**, first grandmaster beaten by AI (IBM **Deep Blue**, 1997); **Alan Turing**; **Aristotle**, who wrote *De Anima* on the mind; **Ada Lovelace**, the first programmer; NASA's **Mars rover**; Boston Dynamics' **Atlas**; autonomous driving; and the Bay Area skyline (Golden Gate, Sonoma, the UC Berkeley tower) where Russell and Norvig live. The 3rd-edition cover had Honda's **ASIMO**, **Thomas Bayes**, a recursive image of the book itself, and **Go** — unbeaten when the 3rd edition shipped, beaten by **AlphaGo** by the 4th. Also **Shakey** (SRI, late 1960s–70s): camera plus sonar, scene analysis, wheeled navigation.

Optional second text: Brighton & Selina, *Introducing Artificial Intelligence* — reissued as *Artificial Intelligence: A Graphic Guide*; *"these two are the same books."*

## What Is Intelligence — the Four Definitions

R&N's grid, each knocked down in turn:

| Definition | His objection |
|---|---|
| **Thinking like humans** | *"Do people always do smart things? No."* Plus the **pet-rock problem** — a USB pet rock *"could be intelligent, doing smart things, but there's no expressed behavior,"* and you can never tell |
| **Acting like humans** | same human-stupidity problem |
| **Thinking rationally** | same pet-rock problem — no behavior to observe |
| **Acting rationally** | the working definition: rational **and** expressed in behavior |

R&N's final form: *"AI is the study of agents that receive percepts from the environment and perform actions"* — which he called *"a little bit too relaxed"*; insert **rationally** and it matches.

### Why "more knowledge = more intelligent" breaks

Three subjects: a math professor (**Terence Tao**, Fields medallist, who *"has recently been using AI to explore unsolved problems"*), a kid, and **Wolfram Alpha**. The professor beats the kid — on mathematical knowledge. But *"I would say the kid is more intelligent than Wolfram Alpha"* — which **contradicts** the knowledge criterion, since Wolfram Alpha knows far more math. The mathematicians' joke on Tao: *"How do you solve a really tough problem? Make him get interested in it."*

## Strong AI vs. Weak AI

| | Strong AI | Weak AI |
|---|---|---|
| Goal | a machine with thought, consciousness, emotion **equal to humans** | theories of human/animal intelligence, **tested by building working models** |
| Assumption | *"humans are no more than elaborate computers"*; the model **is** the mind | the model is a **tool for understanding**, not the mind |
| Problem | consciousness is **subjective** — *"I'm not sure whether any of you are really conscious. I can only say that I am"* (the **other minds problem**) | utility is capped by the stated goal; hard to reach general usefulness |

**AGI** came out of this ~20 years ago and is now the stated goal of OpenAI and DeepMind, with open debate over whether LLMs have reached it. His own note: the weak-AI complaint about narrowness is *"partly no longer the case"* — modern models are broad. See [[Strong AI and Weak AI]].

### The flight analogy, and where it fails

Defining **flight** is tractable: the class converged on **off the ground + controlled + own propulsion** (a bullet fails control; a glider fails propulsion). Intelligence is not: a chess machine beats humans at chess and nobody calls it intelligent, and *"every time someone finds a case where the system fails, you can say it's not truly intelligent — it's a moving target."* His framing: *"There can be only a small number of ways to simultaneously meet a huge number of unclearly defined goals."*

And aerospace theory alone would have mispredicted real flight — modelling **flies** showed flapping cannot generate the needed lift; they **gyrate** their wings, creating leading-edge and tip **vortices**.

### His own perspective

Study the **brain**, the only known implementer of intelligence; study the brain **in its environment**, since it is not isolated in a vat; and take **tools seriously** — *"intelligence is extended into the environment."* Tool use is the standard criterion for animal intelligence (chimpanzees and termite sticks); humans build spoons, smartphones, telescopes, microscopes.

## Related Disciplines — Philosophy, Mathematics, Psychology

**Philosophy of mind**: the **mind–body problem**; **dualism** (two kinds of stuff — but how do they interact?); **idealism** and **materialism** as the two monist extremes; **epiphenomenalism**, where mental phenomena are side effects of physical change with no causal power. Searle's **Chinese Room** (1980): an English speaker inside follows a rulebook over *"squiggle-squoggle"* symbols; the outside Chinese speakers conclude someone in there understands Chinese. *"You wouldn't say the book has understanding, the baskets have understanding; clearly the English speaker doesn't. So the room as a whole does not."* — *"just replace this with ChatGPT and you have the same scene."* See [[Chinese Room]]. Philosophy also now supplies [[AI Ethics]].

**Mathematics**: algorithms; **Boolean logic** under digital computers; **Hilbert's** completeness program; **Gödel's incompleteness**; **Turing's halting problem** — these *"lay out the boundary for what is doable using the computational framework."* Trivia he enjoyed: **Geoffrey Hinton is George Boole's great-great-grandson**.

**Turing**: *Computing Machinery and Intelligence* (journal *Mind*). He read the opening aloud — Turing rejects defining "machine" and "think" by common usage because the answer would then come from *"a statistical survey such as a Gallup poll. But this is absurd"* — and substitutes the **imitation game**. Asked whether the class could spot ChatGPT behind a teletype, answers came back: formatting and em-dashes, **vocabulary**, and **typos** — *"humans would make typos; ChatGPT wouldn't. But you can always instruct it to make typos."* See [[Turing Test]].

**Psychology**: **behaviorism** — study only stimulus and response, since the mind is subjective; **Pavlov's dog** worked step by step (food → salivate; food + bell during conditioning; bell alone → salivate afterwards), with the joke that a cat would do nothing. The extreme behaviorists denied any internal state at all. **Functionalism** reacted, taking its cue from computers: internal representations and processes exist and matter, which yields **implementation (substrate) independence** — *"it doesn't matter whether it's made up of proteins and fat or implemented in silicon, as long as they have the same representations and processes."*

Ran out of time mid-functionalism. See [[Foundations of AI]].

## See Also

- [[CSCE 420 Spring 2026 — 01-14 Linguistics, Neuroscience, History of AI]]
- [[CSCE 420 Lecture 1 — Introduction to AI]]
- [[Strong AI and Weak AI]]
- [[Chinese Room]]
- [[Turing Test]]
- [[CSCE 420]]
