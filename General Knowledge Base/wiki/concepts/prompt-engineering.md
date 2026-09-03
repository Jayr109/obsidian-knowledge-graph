---
title: "Prompt Engineering"
type: concept
tags: [ai, prompting, llm, claude, gpt]
sources: [2026-04-09-claude-ai-export]
domain: technology
updated: 2026-04-09
---

Prompt engineering is the practice of designing and refining natural-language inputs to large language models (LLMs) in order to elicit accurate, relevant, and well-formatted outputs. It is less about coding and more about communication — structuring requests the way you would brief a knowledgeable colleague.

## Core Principles

### Specificity over vagueness
Vague prompts force the model to guess your intent, producing generic results. Specific prompts with context, constraints, and a defined goal produce targeted, expert-level responses. The same knowledge base is accessed either way; the prompt determines how much of it is activated usefully.

### Structured output requests
Explicitly define the output format — numbered list, table, headers, word count, bullet points. Models default to prose unless told otherwise. Defining structure reduces post-processing and makes responses directly usable.

### Chain-of-thought (CoT)
Asking a model to "think step-by-step" or "explain your reasoning" before giving an answer improves accuracy on complex problems. This works because it forces the model to surface intermediate reasoning rather than jumping to a conclusion. Especially effective for math, logic, and multi-step analysis.

### Role prompting
Assigning a role ("you are a senior CFO", "act as a fabric supplier") shapes the vocabulary, assumptions, and framing of responses. Roles activate domain-specific knowledge and make the model more likely to handle edge cases correctly within that domain.

### Few-shot examples
Providing one or more input→output examples in the prompt (few-shot prompting) is one of the most reliable techniques for getting a specific format or style. The model pattern-matches from the examples rather than interpreting abstract instructions.

### Iterative refinement
LLM outputs are drafts. The workflow is: generate → evaluate → give specific feedback → regenerate. Vague feedback ("make it better") produces vague improvements; specific feedback ("shorten paragraph 2 and make the tone more casual") produces targeted changes.

## Hallucination Mitigation

- Explicitly tell the model it may say "I don't know" — removes the implicit pressure to fill in gaps
- Ask for citations or source references when using documents
- Break large, multi-step tasks into smaller sequential prompts
- Verify factual claims independently for high-stakes outputs

## LLM Memory Note

Most LLMs, including Claude, have no persistent memory across sessions by default. All context must be re-supplied in each new conversation. For ongoing work, maintain a context document (like a `CLAUDE.md`) that the model reads at session start.

## See Also
- [[Claude Prompting Guide]]
- [[2026-04-09 Claude AI Export]]
