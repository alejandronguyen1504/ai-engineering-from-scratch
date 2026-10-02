source .venv/bin/activate -> trc khi hoc (hoặc Windows PowerShell: .\.venv\Scripts\Activate.ps1)

================================================================================
PROMPT GENERATE JUPYTER NOTEBOOK PRACTICE SCAFFOLD (BUILD.IPYNB)
================================================================================

Act as a coding mentor. I have the reference solution at [path/to/solution.py] and the lesson documentation at [path/to/docs/en.md].
Please create an interactive practice scaffold Jupyter Notebook for me directly at [path/to/build.ipynb].

Follow these rules strictly:

1. **Core Steps (Strictly match `## Build It` in docs)**:
   - Cross-reference with the `## Build It` section in [path/to/docs/en.md].
   - Divide into sequential Steps (Step 1, Step 2, ...) matching the docs 1-to-1.
   - Each Step must contain:
     * A **Markdown Cell**: Brief overview, mathematical definitions, and list of functions to implement.
     * A **Code Cell**: Function scaffolds with `# TODO:`, `# Hint:`, and concrete `# Example inputs:`.
     * **Immediate Verification / Test Code**: Directly at the bottom of the **same code cell**, include runnable test/demo code (matching docs/en.md examples) with `(Expected: ...)` output values. Wrap tests safely (e.g. handle `None` gracefully so running before implementation prints `None` instead of throwing raw TypeErrors).

2. **Extra Concepts Section (Sub-split individually)**:
   - Identify any additional theoretical concepts or functions from the theory section of [path/to/docs/en.md] or [path/to/solution.py] that are NOT covered in the `## Build It` steps.
   - Place them under an Extra section at the end, sub-split individually (`Extra 1: ...`, `Extra 2: ...`).
   - Give each Extra concept its own Markdown cell and Code cell (scaffold + test block).

3. **Scaffold & Hint Pedagogical Quality (NO SPOON-FEEDING)**:
   - Extract exact signatures, parameters, and type hints from the solution.
   - Replace all implementation logic with `pass`.
   - Inside each function:
     * `# TODO:` explains the objective, the mathematical definition, and parameter roles.
     * `# Example:` a short, concrete sample of input arguments and expected return value (e.g. `# Example: values = [1, 2, 3], probabilities = [0.2, 0.5, 0.3] -> returns 2.1`).
     * `# Hint:` explains algorithmic logic flow, math formula (in general mathematical notation, not Python code), and edge cases.
   - **CRITICAL ANTI-PATTERN TO AVOID**: NEVER provide raw Python one-liner code in hints/TODOs (e.g. NEVER write `# Hint: Return p if k == 1 else 1-p`). The learner must translate the math and logic into Python themselves.

4. **Formatting & Language**:
   - Write all Markdown cells, code comments, and test printouts in English.
   - Include a Setup Cell at the very top (imports, seed, setup check).
   - Write the valid JSON `.ipynb` notebook directly to [path/to/build.ipynb] so I can start practicing immediately.