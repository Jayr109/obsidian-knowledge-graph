---
title: "Claude Prompting Guide"
type: work
tags: [claude, ai, prompting, anthropic]
sources: [2026-04-09-claude-ai-export]
domain: technology
updated: 2026-04-09
---

Anthropic's official prompting guide, distributed as the document inside the "How to Use Claude" starter project on Claude.ai. Covers general techniques, task-specific strategies, and hallucination mitigation for working effectively with Claude.

## Structure

The guide is organized into three sections:

### 1. General Tips for Effective Prompting
Six core techniques:
- **Be clear and specific** — state the task upfront, provide context, break complex asks into steps
- **Use examples** — show Claude the format or tone you want via a concrete sample
- **Encourage thinking** — ask Claude to "think step-by-step" for complex problems; improves accuracy
- **Iterative refinement** — treat the first response as a draft; give specific adjustment instructions
- **Leverage Claude's knowledge** — Claude has broad domain coverage; provide context so it's targeted
- **Use role-playing** — assigning a role ("you are a CFO") improves the nuance and relevance of responses

### 2. Task-Specific Tips
- **Content creation** — specify audience, tone/style, and desired output structure
- **Document Q&A** — reference files by name, ask for citations, specify summary length and format
- **Data analysis** — define the output format explicitly (table, bullet list, chart suggestions)
- **Brainstorming** — specify count, categorization, and output structure (numbered list vs. table)

### 3. Troubleshooting and Hallucination Reduction
- Tell Claude it's okay to say "I don't know" — reduces confabulation
- Break large tasks into sequential messages if Claude misses steps
- Always include all context in a new conversation — Claude has no memory across sessions

## Key Thesis

The guide's implicit argument is that **prompt quality scales response quality almost linearly**. A vague prompt gets a generic response; a structured prompt with context, examples, and a defined output format gets expert-level output. The bad/good example pairs throughout the guide demonstrate this consistently.

## See Also
- [[Prompt Engineering]]
- [[2026-04-09 Claude AI Export]]
