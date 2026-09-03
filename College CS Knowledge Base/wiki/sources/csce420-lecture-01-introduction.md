---
title: "CSCE 420 Lecture 1 — Introduction to AI"
type: source
tags: [csce420, introduction, philosophy, history, foundations, deep-learning]
sources: []
course: CSCE 420
updated: 2026-08-25
---

Lecture 1 of [[CSCE 420]] (`raw/CSCE420_slide01_Introduction.pdf`, 60 pages / 42 logical slides, instructor [[Yoonsuck Choe]]) is the course's framing lecture. It has four sections — Introduction, Related Disciplines, History, and Summary — and covers what AI is, which disciplines it draws on, how the field got here, and where it is going. No algorithms appear; this is the conceptual scaffolding the rest of the course hangs on.

## Section 1 — Introduction (slides 1–16)

Logistics, then the definitional problem. R&N's four textbook definitions (thinking/acting × humanly/rationally) and the agent-based definition the book commits to. The professor-vs-kid-vs-Mathematica comparison showing that task competence is not intelligence. The list of AI subfields per AAAI. The [[Strong AI and Weak AI]] distinction with its three-point characterization of each and the problems with both. The "why not engineer AI like airplanes" argument and its rebuttal via insect flight (Ellington et al., *Nature* 384(6610), 626–630, 1996).

→ [[Artificial Intelligence]], [[Strong AI and Weak AI]], [[Yoonsuck Choe]]

## Section 2 — Related Disciplines (slides 17–25)

The six [[Foundations of AI]]: philosophy (mind-body problem, Chinese room, AI ethics), mathematics (al-Khowarazmi, Boolean logic, Hilbert, Gödel, Turing), psychology (behaviorism, functionalism, perceptual, cognitive), cognitive science, linguistics (machine translation through to LLMs), and neuroscience (Golgi staining through to TMS).

→ [[Foundations of AI]], [[Philosophy of Mind]], [[Chinese Room]], [[Turing Test]]

## Section 3 — History (slides 26–32)

Six-part timeline from the 1943 McCulloch-Pitts neuron and the 1956 Dartmouth workshop through to ChatGPT, plus the AI@50 assessment (Rodney Brooks's "social sophistication of a 10-year-old, manual dexterity of a 6-year-old, language ability of a 4-year-old, visual object recognition of a 2-year-old") and a list of major achievements from Deep Blue to AlphaFold.

→ [[History of AI]]

## Section 4 — Summary and Outlook (slides 33–42)

Figure-heavy synthesis of three eras. The [[Symbolic AI]] slide includes a worked train/taxi clause example. The machine learning slide notes probability-based learning from data and the decline of logic-based AI. The machine learning primer defines supervised learning as learning from $(x=\text{PATTERN}, y=\text{LABEL})$ pairs to recognize novel input. The [[Deep Learning]] slides cover the CNN feature hierarchy (pixels → edges → object parts → objects), the three fuels of the revolution (algorithms, big data, GPU compute), superhuman results in vision/speech/NLP, and deep RL for control. The limitations slide lists four failure modes with illustrations (panda→gibbon perturbation, altered stop signs, the fire-rescue common-sense gap, the husky-vs-snow spurious feature). The closing slide lists four future directions.

→ [[Symbolic AI]], [[Machine Learning Paradigms]], [[Deep Learning]], [[Neurosymbolic AI]]

## Extraction Notes

- 42 logical slides span 60 PDF pages because of beamer incremental builds.
- Slides 33–42 (the entire Summary section) are **title plus embedded image** — they carry no extractable text and were read by rendering the pages. Their content is transcribed above and on the linked concept pages.
- "Suppl:" slides interspersed throughout are screenshot-only pointers to external material (Turing's 1950 paper, the Turing Test, AI pioneers, a LISP DFS example at `github.tamu.edu/choe/lisp`, ELIZA, IBM Watson, Mechanical Turk, deep RL, `github.com/yschoe/chatgpt-fun`, DALL-E, Golgi stain, Hubel and Wiesel, TMS, direct current stimulation). They contribute references, not content.

## See Also

- [[CSCE 420]]
- [[Artificial Intelligence]]
- [[History of AI]]
- [[Foundations of AI]]
- [[Yoonsuck Choe]]
