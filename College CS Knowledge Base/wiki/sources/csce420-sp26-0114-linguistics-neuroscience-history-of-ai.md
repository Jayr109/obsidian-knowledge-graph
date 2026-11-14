---
title: "CSCE 420 Spring 2026 — 01-14 Linguistics, Neuroscience, History of AI"
type: source
tags: [csce420, lecture-recording, spring-2026, linguistics, chomsky, semantics, ambiguity, cognitive-science, neuroscience, hubel-wiesel, fmri, tms, history-of-ai, dartmouth, perceptron, ai-winter, eliza, mechanical-turk, watson, dqn]
sources: []
course: CSCE 420
semester: Spring 2026
date: 2026-01-14
deck: slide01
exam: midterm
updated: 2026-09-30
---

Spring 2026 lecture, 50 min. The remaining related disciplines — linguistics, cognitive science, neuroscience — then the full history of AI from McCulloch & Pitts to deep RL. Slides 01:30–38. Archived at `raw/CSCE420_Spring2026_lecture_transcripts/GMT20260114-*.vtt`.

> **Exam scope, stated outright.** A student asked whether the discipline material would be on the exam: *"The answer is no. This is just for fun — except for core concepts like strong AI, weak AI."* And: *"There'll be typically just one question from the introductory slide, slide01."* The sample midterm's slide01 question shows an image and asks **strong AI or weak AI**. See [[CSCE 420 Midterm Review]].

## Linguistics

Machine translation was first attempted in **World War II** (German ↔ English). Subfields: **phonetics** (sound), **syntax** (grammar), **semantics** (meaning), **discourse** (ongoing conversation).

**Chomsky**: language ability is **innate** — not a specific language, but *"a general language ability."* His formal grammars (regular, context-free, phrase-structure) and the matching machines (finite automata, pushdown automata) came out of the attempt to pin syntax down.

**Semantics and ambiguity** — he polled the room on the word *bat*, and the split was about half animal, half baseball. Then in context: *"I was hit by a bat"* in Antarctica means the baseball bat; at a baseball game, same sentence, also the bat — *"it all depends on the context."*

**Symbolic → subsymbolic**: everything above is symbolic, but LLM internal representations are **embedding vectors** that *"can be broken down — it's not atomic."* His PhD advisor **Risto Miikkulainen** did early work in subsymbolic NLP.

A caution: language is often called uniquely human, but whales and dolphins vocalize to communicate — *"we just don't understand what they're saying."*

## Cognitive Science

*"Perhaps the most similar to AI"* — interdisciplinary, computation-based, studying human perception and cognition from the brain up through social interaction and cultural studies.

## Neuroscience

**Structure first.** Brain tissue is semi-transparent, so neurons need **chemical stains** to be visible. He opened his own lab's mouse-brain atlas (**Golgi stain**), overlaying 20 slices at 5-image intervals to resolve **cell bodies**, **dendrites**, and **axons**.

**Then function.** **Hubel and Wiesel** (Nobel Prize) poked an electrode into cat visual cortex. Cat photos and object images produced nothing reliable; **by accident** they found **moving edges** drive strong responses, with each neuron tuned to a **specific orientation** — *"if the orientation is way off, there will be no response."* He showed a 2004 conference photo of himself with both, and his signed copy of *Brain and Visual Perception*.

**Non-invasive imaging**: **PET**; **CAT** (*"a glorified X-ray"* — multiple sections into a 3-D volume), low resolution but enough to localise lesions in patients with language loss, which mapped speech production vs. comprehension; **fMRI**, measuring **oxygen depletion** ~1 frame/sec as the signature of activity; optical imaging.

**Stimulation, not just recording** — *"it's not enough to just record from the brain; you have to activate it and see what happens."*
- **TMS**: two tightly wound coils carry strong current → magnetic fields that **interfere and amplify** in the middle → placed on the skull, the field **induces current on the brain surface**. At UT Houston they targeted his **motor cortex** (just anterior to somatosensory, with the same body map): his hand twitched with no intention, and a slight move down isolated his **index finger**. On visual cortex it produces **phosphenes**.
- **Transcranial direct current stimulation**: weak current across the head in a specific direction — marketed to gamers; *"I'm not sure whether this was very effective. I'm not seeing these anymore."*

## History of AI

**Gestation — two camps from the start.** **Symbolic** (search, theorem proving, representation; Newell & Simon's **physical symbol system hypothesis**) vs. **connectionist**. The connectionist side came **first**: **McCulloch & Pitts** gave a mathematical description of neurons and synapses, but *"they didn't have any facility to train these networks"* — descriptive, not functional.

**1956 Dartmouth workshop** — the term *artificial intelligence* is coined; **exactly 70 years ago as of this semester**. He browsed the **AI@50** Wikipedia page (2006, *"The Dartmouth Artificial Intelligence Conference: The Next 50 Years"*): Minsky and McCarthy since deceased; speakers included **Geoffrey Hinton**, **Peter Norvig** (textbook co-author), **Rodney Brooks** (behavioral robotics at MIT, founded **iRobot** / Roomba), and **Ray Kurzweil** (technological **singularity**).

**1950s–60s successes**: the **General Problem Solver**; McCarthy's **Lisp** (he showed his own DFS implementation — *"a lot of these parentheses"*); **Rosenblatt's perceptron** (1958), *"the first neural network model that has a learning rule"*, step activation; **Widrow & Hoff** extending it to continuous outputs; toy domains like **ANALOGY** and **STUDENT**. Then **Minsky & Papert (1969)** *"proved that Rosenblatt's perceptron is not good"* → the neural-network **winter**. *"We'll learn what that limitation was and how the neural network people overcame it."*

**1960s–70s**: hard-coded AI and **ELIZA**, a pattern-matching chatbot that was *"surprisingly impactful — ordinary people thought there was a human behind the terminal."* He found a live mirror and demoed it: *"How are you feeling today?"* → *"Would you prefer if I were not feeling today?"* — *"Very sarcastic."* Knowledge-based systems spawned companies, *"but they claimed too much and got too much investment without real impact — hence the AI winter."*

**1980s–90s**: 1980s = personal computers; **1990s = the internet** (he first used it in 1993, on **NCSA Mosaic**), which meant **data started accumulating**. Non-symbolic methods rose: **Bayesian networks**, **hidden Markov models**, **SVMs** with theoretical guarantees, statistical NLP displacing hand-built syntactic parsing. *"This is the decade when machine learning came to the central stage."*

**2000s–early 2010s**: big data, web, information retrieval; **IBM Watson** beating the Jeopardy! champions; **human-based computation** — **reCAPTCHA**, which repurposed the bot test into **labelling scanned text** (*"ask 100 people what letter this is and on average they get it right"*), and **Amazon Mechanical Turk**, named for the 18th-century chess automaton that **hid a human inside the cabinet**. Over 500,000 registered Turk workers globally, paid fractions of a cent per click, with the system resolving the true label from multiple responses.

**Rod Brooks' 2006 wish-list**, and his scorecard on it today:

| Target | Status |
|---|---|
| visual object recognition of a 3-year-old | done |
| language ability of a 4-year-old | *"way beyond"* |
| manual dexterity of a 6-year-old | **hard** — *"none of these humanoid robots have a very delicate hand like us"*; mechanical and electrical, not just control |
| social sophistication of a 10-year-old | *"I don't know whether we want this — you don't want them to manipulate you"* |

**Mid-2010s to now**: deep learning across vision, speech, NLP, RL; generative AI; bordering on AGI, with reasoning and common sense as the gaps, and **neuro-symbolic AI** proposed by those who think networks alone will not get there. See [[History of AI]].

## Deep RL Demo

Reinforcement learning framed as state → action → resulting state + reward, maximizing accumulated reward; a video game maps onto it directly (screen = state, paddle control = action, score = reward). He ran the Atari **Breakout** DQN: useless at 100 steps; by **620 episodes** it has learned the human trick of **punching a hole up the side** so the ball bounces along the top. Also Space Invaders.

**The architecture**: several video frames → convolutional layers → fully connected → output units, where *"these output values are the **Q function** — given this state, how valuable is this action?"* Pick the highest and move the paddle. *"You don't need to tell it the rules of the game, even."* Full treatment in [[Deep Q-Network]].

## See Also

- [[CSCE 420 Spring 2026 — 01-12 Syllabus, What Is Intelligence]]
- [[CSCE 420 Spring 2026 — 01-16 Modern AI, Limitations, Future]]
- [[CSCE 420 Lecture 1 — Introduction to AI]]
- [[History of AI]]
- [[Foundations of AI]]
- [[CSCE 420]]
