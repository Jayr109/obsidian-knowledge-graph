---
title: "Foundations of AI"
type: concept
tags: [csce420, philosophy, mathematics, psychology, linguistics, neuroscience, cognitive-science]
sources: [csce420-lecture-01-introduction]
course: CSCE 420
updated: 2026-08-25
---

AI draws on six academic disciplines, each contributing a distinct question and a distinct method. Lecture 1 walks through all six as the intellectual background of the field. Course reference: B&S pp. 13–20.

## Philosophy

Supplies the mind-body problem and the question of whether machine thought is coherent at all. See [[Philosophy of Mind]] for dualism/monism/epiphenomenalism, and [[Chinese Room]] for the syntax-vs-semantics argument. Contributes AI ethics: safety, fairness, privacy, promoting collaboration, transparency, limiting harmful use.

## Mathematics

- **Algorithm** — from al-Khowarazmi
- **Boolean logic**
- **Hilbert** — are the axioms of arithmetic complete?
- **Gödel** — incompleteness theorem
- **Turing** — halting problem; *Computing Machinery and Intelligence* and the [[Turing Test]]

The takeaway phrase from this slide is the **computer/software metaphor**: representation/interpretation and symbol/computing as a model of mind. This is the intellectual license for [[Symbolic AI]].

## Psychology

- **Behaviorism** — stimulus-response and conditioning
- **Functionalism** — internal representations and processes; *implementation independent*
- **Perceptual psychology** — vision, audition, etc.
- **Cognitive psychology** — cognition as information processing

Functionalism's implementation independence is the assumption that lets you claim a program on silicon could realize the same mental states as a brain.

## Cognitive Science

An interdisciplinary field studying human perception and cognition, spanning neuroscience, behavioral science, social science, psychology, computational science, information theory, and cultural studies.

## Linguistics

- WWII machine translation
- Phonetics, syntactic theory, semantics, discourse
- Innate vs. learned? — Chomsky
- Syntax: finite automata, context-free grammar
- Semantics: semantic nets
- Sub-symbolic: [[Self-Organizing Map|self-organizing maps]], episodic memory, recurrent neural nets
- [[Deep Learning]]: RNNs, transformers, large language models

Linguistics is where the course's symbolic and sub-symbolic threads visibly meet — the same problem (language) has been attacked by grammars and by neural nets.

## Neuroscience

Methods, roughly in historical order of what they let you see:

| Method | What it reveals |
|--------|-----------------|
| Staining (Golgi, Nissl) | Neurons and connections |
| Hubel and Wiesel | Neural activation induced by visual stimulus |
| PET and CAT scans | Localizing functional modules |
| fMRI imaging | Whole-brain activation during task |
| Optical imaging | Mapping cortical activations |
| TMS | Non-invasive stimulation ("zap your brain") |
| Direct current stimulation | Non-invasive stimulation |

Hubel and Wiesel's receptive-field work is the direct ancestor of convolutional architectures in [[Deep Learning]].

## See Also

- [[Artificial Intelligence]]
- [[History of AI]]
- [[Yoonsuck Choe]]
- [[Neurosymbolic AI]]
