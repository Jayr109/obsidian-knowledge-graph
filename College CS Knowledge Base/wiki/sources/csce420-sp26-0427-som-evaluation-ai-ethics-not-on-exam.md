---
title: "CSCE 420 Spring 2026 — 04-27 SOM Evaluation, AI Ethics (Not on Exam)"
type: source
tags: [csce420, lecture-recording, spring-2026, self-organizing-maps, quantization-error, topographic-error, semantic-map, animal-map, mnist-som, ai-ethics, moral-agency, bias-fairness, transparency, explainability, privacy, training-data-extraction, future-of-work, turing-trap, augmentation, ai-regulation, ai-bill-of-rights, eu-ai-act, pause-letter]
sources: []
course: CSCE 420
semester: Spring 2026
date: 2026-04-27
deck: slide06, slide08
exam: excluded
updated: 2026-09-17
---

Spring 2026 lecture, 50 min, last regular Monday. SOM evaluation metrics and the semantic-map examples, then the **AI Ethics** deck (08) nearly to the end. The final class (Tuesday 04-28, Redefined Friday) was a research talk and is not in the export.

> **NOT ON THE FINAL.** Both halves — Self-Organizing Maps and AI Ethics — were explicitly excluded from the final exam. Filed for completeness only. See [[CSCE 420 Final Review]].

## Evaluating a SOM

No supervised error exists, but two input-only measures do:

- **Quantization error** = (1/N) Σ over inputs ‖x − w_BMU(x)‖ — how far each input sits from its best-matching unit's weight vector. High when units are far from the data.
- **Topographic error** = (1/N) Σ u(x), where **u(x) = 1 if the first- and second-best matching units are not grid-adjacent**, else 0 — measures whether nearby units represent similar inputs.

**Predicting the learned grid from the input distribution**: uniform square → evenly spread grid; Gaussian blob → **more units in the middle**, periphery stretched by occasional outer samples; a shape with a hole → no units pulled into the empty region.

## Semantic Maps

**Animal dataset**: 16 animals × **13 binary features** (small/medium/big; 2 legs, 4 legs, hair, hooves, mane, feathers; hunts, runs, flies, swims). Impossible to eyeball in 13-D. A **10×10 SOM** puts dog, fox, wolf together; the cats (cat, lion, tiger) together; birds of prey; fowl; herbivores (horse, zebra, cow) — *"we didn't explicitly tell it there are these five major groups."*

**Labelling the in-between units**: present all 16 animals to each unit and label it with the best match → coherent regions (dog region, fox region, wolf region) and a higher-level layout: predators / birds / herbivores.

**His 1995 MS thesis**: 20×20 SOM on 32×32 (1024-d) MNIST digits. Regions of 1s at different angles and thicknesses; 7 transitioning into 9; **regional 7s** (US vs. European vs. Asian styles); thin/fat 4s; tilted/flat/fat 0s. Using the 20×20 **similarity response map** as features gave **better generalization** than training directly on pixels.

## AI Ethics (Deck 08)

**Ethics**: Britannica's definition is circular (*"concerned with what is morally good and bad"*); ChatGPT's — principles of right and wrong conduct and the obligations that guide behaviour — *"a pretty good summary."* Thinkers on the slide: Bentham, Mill, Kant, Dewey; and **Timnit Gebru**, fired from Google's AI-ethics lead in 2020 after raising harms including the environmental cost of large models.

**Moral agency**: an exploding rice cooker or a lawnmower robot that flattens the neighbour's flowerbed is not ethically blameable — it followed its algorithm. Agency = the capacity to make moral decisions and therefore be **accountable**.

**Why now**: *"This year has been really alarming — from January, agentic AI just exploded in capability, so people are not sure any longer whether we can control it."* Harms: physical (autopilot), societal disruption (jobs, roles). Roots: we don't fully understand why it works; data and human misuse.

### Topics, with his examples

- **Accountability in decisions**: financial, judicial, law-enforcement software — parole-screening tools found biased.
- **Transparency and explainability**: OECD guideline ("meaningful information appropriate to the context"); DARPA XAI.
- **Privacy**: *Extracting Training Data from LLMs* — a multimodal model reproduced a near-replica of a training image ("Living in the Light with Anne Graham Lotz") from its caption; the **"repeat 'poem' forever"** attack that eventually spat out someone's personal information — *"I was really amazed… how did people even come up with this prompt?"* Earlier USENIX work inferred training data from online ML services.
- **Bias and fairness**: race, age, wealth, status; symptoms in speech recognition, face recognition, job screening. TAMU System non-discrimination policy read aloud.
- **Future of work**: two-thirds of jobs affected to some degree; OpenAI study — 80% of US jobs have ≥10% of tasks affected, 1 in 5 has half; Goldman Sachs — ≥50% exposure ≈ replaceable; most exposed: legal services, securities, telemarketing, post-secondary teaching of languages and history. Harari: the unretrained become *"not just unemployed but unemployable."* Historical offset by new occupations — *"but AI is a different beast."*
- **The Turing Trap** (Brynjolfsson): **automation** mimics humans inside the human task space; **augmentation** reaches tasks *"previously not reachable by us"* and *"generates far more value."*
- **Misuse**: hacking, phishing, DoS, disinformation, deepfakes, autonomous weapons.
- **Regulation**: OECD AI Principles; the US **Blueprint for an AI Bill of Rights** — now a 404 on whitehouse.gov, retrieved via the **Wayback Machine** (safe systems, algorithmic-discrimination protection, data privacy, notice and explanation, human alternatives); the **EU AI Act**; **Partnership on AI**; the 2023 **"pause giant AI experiments"** letter (33,000 signatories, 6-month pause beyond GPT-4) — *"it seems like they failed."*

Left for the last class: research ethics, conscious AI, developers' responsibilities. See [[AI Ethics]].

## See Also

- [[CSCE 420 Spring 2026 — 04-24 Self-Organizing Maps (Not on Exam)]]
- [[CSCE 420 Spring 2026 — 01-21 Uninformed Search]]
- [[AI Ethics]]
- [[CSCE 420 Lecture 8 — AI Ethics]]
- [[CSCE 420 Lecture 6 — Machine Learning]]
- [[CSCE 420]]
