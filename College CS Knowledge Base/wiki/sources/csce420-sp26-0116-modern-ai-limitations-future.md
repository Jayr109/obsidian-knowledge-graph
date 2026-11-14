---
title: "CSCE 420 Spring 2026 — 01-16 Modern AI, Limitations, Future"
type: source
tags: [csce420, lecture-recording, spring-2026, chatgpt, rlhf, dall-e, gpt-3, milestones, symbolic-ai, resolution-preview, machine-learning, deep-learning, alexnet, vgg, inception, object-detection, vqa, adversarial-inputs, spurious-features, neuro-symbolic, hw1]
sources: []
course: CSCE 420
semester: Spring 2026
date: 2026-01-16
deck: slide01, slide02
exam: midterm
updated: 2026-09-30
---

Spring 2026 lecture, 50 min, last day of slide01. Modern generative AI, the achievement timeline, the three-era summary of AI, the CNN scaling story, deep learning's limitations, the future, then HW1 and a peek at slide02. Slides 01:38–end, 02:1–3. Archived at `raw/CSCE420_Spring2026_lecture_transcripts/GMT20260116-*.vtt`.

> MLK Day fell on the following Monday — **no class 01-19**; the next lecture is [[CSCE 420 Spring 2026 — 01-21 Uninformed Search]]. (His battery died mid-lecture and he swapped it on camera.)

## Generative AI, Briefly

The **ChatGPT three-step diagram** got a preview — label-written demonstrations, then humans **ranking** candidate responses, then optimization — *"we'll learn a little more about that near the end of this semester."* Full treatment in [[CSCE 420 Spring 2026 — 04-22 LLMs, Diffusion, Deep Learning Wrap-Up]]. Then **DALL·E**: *"knitted out of wool," "spray-painted on a wall," "made out of plasticine"* — multiple realistic variants per prompt. *"This is so routine nowadays it's not even surprising."*

## Milestones

Game AI in the 1980s (*"stereotypical behavior"*); **Deep Blue** beats Kasparov, 1997; **Watson** wins Jeopardy!, 2011; **AlphaGo** beats the Go master, 2016; **AlphaStar** beats top StarCraft players 10–1, 2019; **Hinton, LeCun, Bengio** win the **2018 ACM Turing Award**. His Waymo-instead-of-Uber ride in Atlanta got its first mention here (shown in full on 04-06). **GPT** from 2020; **AlphaFold**; **DALL·E/DALL·E 2** (2021); **GitHub Copilot**; **ChatGPT** (2022).

### The philosopherai.com demo

Built on the **GPT-3 API before it became paid** — *"there was no user-facing interface, so someone built a website."* He read his saved sessions: *"What is the fundamental truth?"* → a unified field underlying reality, never discoverable because knowledge comes through the senses. *"Is the universe fundamentally computational?"* → yes, resting on two claims, that everything follows rules and everything can be simulated. *"Pretty profound."* Revisited on 04-22.

## The Three Eras — One Table

| Era | Approach | Breaks on |
|---|---|---|
| **→ mid-1980s** | symbolic, logic, rule-based, theorem proving, expert systems | **vague concepts**; cannot **learn from data** |
| **mid-1980s → mid-2010s** | machine learning — learn from data, handle **unstructured** data; SVMs, decision trees; vision, speech, language | symbolic AI declines |
| **mid-2010s → now** | deep learning; CNNs, deep RL, generative AI | data hunger, reasoning, interpretability |

### The symbolic example — a resolution preview

*"If the train is late and there is no taxi at the station, John will be late for the meeting."* Given the train **was** late and John was **not** late, what follows? The class got it: **there was a taxi.** He then propositionalized it — T (train late), X (taxi at station), L (John late) — wrote the clause form **¬T ∨ X ∨ L**, and showed that eliminating **complementary pairs** derives the conclusion. *"A simple rule to eliminate these paired complementary propositions"* — the first appearance of [[Resolution]], done in full in Deck 03.

### The supervised-learning example

An input/target table that turned out to be **OR** — *"for this there's really no reason to learn, because you're already given all the answers to all possible inputs."* Then the real case: a 10×10 RGB image is a **300-number vector** (100 red + 100 green + 100 blue) with label *dog*; collect many, train, classify a new image. Same shape for speech: encode the waveform as a vector, label it *hat* or *pot*.

## The CNN Scaling Story

Reading the standard bubble chart — **x = compute (giga-ops), y = accuracy, bubble size = parameters (memory footprint)**:

- **AlexNet** (2012): ~**54%** accuracy on ImageNet (~1.5 M images, 1,000 categories), ~**42 M parameters**. *"Did kind of poorly, but this was way better than any non-deep-learning approach."*
- **VGG16 / VGG19**: the **same architecture made deeper and larger** → *"the accuracy just skyrocketed"*, roughly 20 points, *"almost immediately. So people started to realize: deep is good."*
- **Inception** (Google): people were unhappy with VGG's compute and memory, so the goal became **smaller and faster at the same accuracy** — not a flat stack but **repeating modules with bottlenecks**.

A student asked what "operations" meant: compute time, which rises with depth — *"but the number of layers is more related to the size,"* the memory footprint.

**Task escalation**, each step because the previous became too easy to publish on: classification → **classification + bounding box** (*"what and where"*) → **multiple objects** → **pixel-level segmentation** → **multimodal VQA**. VQA successes: *what vegetable is on the plate?* → broccoli; *how many school buses?* → two (*"I initially saw one — there's a tiny bus in the background"*). Failures, which he found more informative: *what is on top of the refrigerator?* → **magnets**, truth **cereal**; *what uniform is she wearing?* → **shorts**, truth **Girl Scout** — *"sometimes you question: is this really the right ground truth? Should there be multiple answers?"*

**Speech recognition** error on a log-log plot: near 100% in the early 1990s → ~10–15% by 2000 with **hidden Markov models** → **flat for a decade** → collapses with deep learning. Asked whether the plateau was the algorithms or the data, he said **both**: *"there wasn't that much data to begin with,"* and the early methods were weak.

## Limitations of Deep Learning

- **Data hunger** and **no complex reasoning** — *"multi-step reasoning beyond, like, 100 steps is still a huge challenge."*
- **No common sense.** Vision models will localize *person, chair, dog* in a photo easily, but *"what do you need to rescue first in case of fire?"* defeats them. He put the question to **chat.tamu.ai** (the university's own free LLM gateway, OpenAI and Gemini models) and it correctly said **the child** — *"it has pretty good common sense. But this is another example of that moving-target thing."*
- **Adversarial inputs.** Panda at 57.7% confidence; add a crafted noise pattern scaled by ~0.0001 and the same-looking image reads **gibbon at 99.3%**. Critics called it unrealistic — so researchers put **stickers on a stop sign**. The model is robust to shading, graffiti, angle and lighting, but *love/hate* stickers make it read **speed limit**. Critics said the words were confusing, so they redid it with **plain black-and-white stickers** — still speed limit. Related: patterned T-shirts that defeat person detection, *"even if it is not on your face."*
- **Spurious features.** Saliency on a Siberian Husky classifier showed the **snow field in the background** had the strongest influence — because husky photos come from Alaska and the Yukon. *"The network only needs to do its task. It doesn't really try to learn the meaning of the world."*
- **Interpretability** — *"a huge research area."*

## The Future

**Neuro-symbolic AI** (combine the two paradigms); **neuroscience-inspired / neuromorphic AI**; **neuroevolution** (networks plus evolution — delivered on 04-08/04-10); **consciousness**; **epistemology** — *"do these AI algorithms have a different epistemology compared to us?"*; and **post-humanism**, brain implants included.

## HW1 and a Peek at Slide02

HW1 posted: *"pretty boring detail, but you really need to read through all of this if you don't want to get any penalty."* Written search problems plus a **Colab notebook** (`dfs.ipynb`), walked through the following week. See [[CSCE 420 Homework 1 — Search]].

Slide02 preview — **138 slides**: uninformed search, informed search, iterative improvement, CSP, game playing. His opening question: *"Do you think search should be part of AI? If someone just searched on Google and produced the answer, is that person intelligent?"* — **maybe not.** *"Search can be thought of as just an algorithm that doesn't require any intelligence. But what I'm going to show you is that search can be a valuable intelligence strategy."*

## See Also

- [[CSCE 420 Spring 2026 — 01-14 Linguistics, Neuroscience, History of AI]]
- [[CSCE 420 Spring 2026 — 01-21 Uninformed Search]]
- [[CSCE 420 Lecture 1 — Introduction to AI]]
- [[Deep Learning]]
- [[History of AI]]
- [[CSCE 420]]
