# Prompt Template: Build-It Notebook Generator

Use this prompt to generate a self-paced, hands-on Jupyter Notebook for any lesson in the curriculum.

---

## The Prompt

Copy and send the prompt below to your AI assistant. Replace the bracketed placeholders `[LESSON_DOCS_PATH]` and `[TARGET_NOTEBOOK_PATH]` with your current lesson paths.

```markdown
Read the "Build It" section in [LESSON_DOCS_PATH].
Generate a hands-on Jupyter Notebook at [TARGET_NOTEBOOK_PATH] following the specification below.

### 1. Goal
Create a step-by-step implementation notebook where the learner codes the core algorithmic logic from scratch for each build step.

### 2. Constraints and Style
- Language: English only. Use Simplified Technical English (short sentences, simple tenses, direct instructions).
- Minimalism: Zero emojis, zero decorative icons, and zero conversational filler.
- Standard Library: Use Python standard library or basic NumPy only. Do not use high-level frameworks.
- Output Format: Valid Jupyter Notebook (.ipynb) format (nbformat 4, nbformat_minor 5).

### 3. Step Structure
For each step in the build section, provide:
1. Markdown Cell:
   - Step title and concept explanation.
   - Exact input and output specifications.
   - Clear hints explaining the mathematical or algorithmic operations.
2. Code Cell (Starter):
   - Function or class signature with type hints.
   - Docstring containing concrete sample input and expected sample output.
   - Conceptual `# TODO:` comments explaining what needs to be done in plain English prose.
   - No spoon-feeding: Do not write out exact Python code expressions, list comprehensions, or solution syntax in the hints or TODOs.
   - Body contains only `pass`.
3. Test Cell:
   - Self-contained assertions (`assert`) checking edge cases, shapes, and values.
   - Prints `Step X passed.` upon success.

### 4. Boilerplate vs Core Logic
- Pre-implement repetitive utility functions (such as standard mathematical formulas, vocabulary builders, or imports) in separate helper cells.
- Reserve the core algorithm for the learner in the `# TODO:` starter cells.
- Guide the learner on *what* to do, not *how* to type the syntax.

### 5. Final Cell
Provide an end-to-end runnable demo integrating all steps on a small, realistic example dataset.
```

---

## Example Usage

```markdown
Read the "Build It" section in phases/11-llm-engineering/06-rag/docs/en.md.
Generate a hands-on Jupyter Notebook at phases/11-llm-engineering/06-rag/code/RAG-my_build.ipynb following the specification below.

[Paste the prompt constraints above]
```
