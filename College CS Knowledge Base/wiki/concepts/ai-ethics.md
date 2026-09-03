---
title: "AI Ethics"
type: concept
tags: [csce420, ethics, fairness, accountability, transparency, regulation]
sources: [csce420-lecture-08-ai-ethics]
course: CSCE 420
updated: 2026-09-01
---

The final deck of [[CSCE 420]]. **Ethics** is moral philosophy — the discipline concerned with what is morally good and bad, right and wrong — and the deck applies it to AI systems and to the people who build them.

## Two Key Concepts

- **Normative ethics** — theories providing general moral rules governing human behavior
- **Moral agency and responsibility** — the ability to make moral decisions and thus **be accountable**

The second is where AI creates genuinely new difficulty: a system can make consequential decisions without being a moral agent, so accountability must attach somewhere else.

## Why AI Ethics Now

AI's impact on society is growing rapidly, and the deck gives a specific diagnosis:

> AI has become quite powerful and sophisticated, and can possibly cause physical and/or mental harm to people, and potentially cause societal disruption. **Part of the reason is: we do not understand fully why it works so well, and do not know how to fully control it.**

That is an unusually direct admission, and it links the ethical problem to the technical one — the explainability limitation listed on [[Deep Learning]] is *why* accountability is hard, not a separate issue.

## Impact on Society

| Positive | Negative |
|---|---|
| Reduce routine work; help with complex tasks | Privacy risks |
| Improve quality of life — simpler, safer, more efficient | **Exacerbates racism by standardizing people** |
| Accelerate scientific discovery | Takes away human jobs |
| Solve world issues: energy, food, climate, health | Amplifies inequality; polarizes social groups |

## The Issue Areas

**Bias, discrimination, fairness** — age, wealth, social status; concretely in **speech recognition, face recognition, and job screening**. The deck points to TAMU system policy on nondiscrimination.

**Decision making and accountability** — software making critical **financial, judicial, and law-enforcement** decisions may require accountability.

**Transparency and explainability** — DARPA's **XAI** program.

**Privacy and data protection** — AI models can **leak sensitive data**, and **training data can be extracted from a trained model through reverse engineering**. Note this is a property of the model itself, not of a data breach.

**Misuse for malicious purposes** — hacking, phishing, denial of service; fake news and disinformation; forged photos, video, and voice; robots, drones, self-driving cars.

## The Future of Work

The bleakest section:

- Many jobs will disappear
- **Even creativity, thought to be a uniquely human capability, is in peril**
- Retraining is needed, or people become **not just unemployed but unemployable — "the useless class"**

Against this, Brynjolfsson (*Daedalus*, 2022) offers **augmentation vs. automation**:

> "When AI is focused on **augmenting** humans rather than **mimicking** them, humans retain the power to insist on a share of the value created."
> "Augmentation creates new capabilities and new products and services, ultimately generating far more value than merely human-like AI."

The argument is economic rather than sentimental: mimicry makes humans substitutable and hands the surplus to whoever owns the system; augmentation makes them complementary and preserves their bargaining position.

## Regulation and Policy

- **OECD AI Principles**
- **Blueprint for an AI Bill of Rights** (US)
- **The Artificial Intelligence Act** (EU)
- **Partnership on AI**

## Further Considerations

**Pause giant AI experiments?** The Future of Life open letter, explicitly compared to the **Asilomar Conference on Recombinant DNA (1975)** — the precedent for researchers voluntarily pausing their own field.

**Research ethics** (credited to David Touretzky, CMU): plagiarism, conflict of interest, human and animal subjects, data fabrication, authorship and IP, confidentiality, and moral debates over stem cells and weapons of mass destruction.

**Conscious AI** — if AI becomes conscious, should it get basic rights? The analogy offered is animal research: vertebrates are strictly regulated, and **cephalopods are beginning to be** (Directive 2010/63/EU) — a precedent for extending protection as evidence of sentience accumulates.

## Developer Responsibilities

The course's closing instruction to its own students:

- **Strive for public good**
- Be aware of AI ethics principles: fairness, transparency, accountability, safety, privacy
- **Think of direct and potential risks your AI code can cause**
- Be cautious with the data used and generated

## See Also

- [[Deep Learning]]
- [[Artificial Intelligence]]
- [[Strong AI and Weak AI]]
- [[Philosophy of Mind]]
- [[CSCE 420]]
