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
     * A **Markdown Cell**: 
       - Brief overview and concise step explanation.
       - A bullet list of all functions to implement in this step.
       - **Mathematical Formulas**: If a function's body implements a mathematical formula, distribution, or equation (e.g. factorial, distributions PMF/PDF, expected value, softmax, loss functions, Box-Muller, etc.), explicitly provide that exact mathematical formula using LaTeX notation (`$...$` or `$$...$$`) directly beside the function name in the brief.
     * A **Code Cell**: Function scaffolds with `# TODO:`, `# Hint:`, and concrete `# Example inputs:`.
     * **Immediate Visual Test Verification**: Directly at the bottom of the **same code cell**, include runnable test/demo code (matching docs/en.md examples).
       - **Passing (Expected matched)**: Print a green tick `✅` along with the result (e.g. `✅ factorial(5) = 120`).
       - **Failing / Unimplemented / Error**: Print a red exclamation mark `❗` clearly showing actual output vs expected (e.g. `❗ factorial(5) = None (Expected: 120)`).
       - Wrap tests safely in `try...except` and handle `None` gracefully so running before implementation never crashes the cell with unhandled `TypeError`.

2. **Extra Concepts Section (From Reference Solution)**:
   - Compare the author's reference solution in [path/to/solution.py] against the `## Build It` section in [path/to/docs/en.md].
   - Any function that the author implemented in the reference code but is NOT covered in the `## Build It` steps of the docs MUST be placed into an Extra section at the end of the notebook.
   - Sub-split each extra concept individually (`Extra 1: ...`, `Extra 2: ...`), each having:
     * A Markdown cell with brief overview and LaTeX mathematical formula (if the body implements math).
     * A Code cell with scaffold (`pass`, `# TODO:`, `# Hint:`, `# Example:`) and immediate visual test verification (`✅` / `❗`).

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
   - Include a Setup Cell at the very top (imports, seed, and a lightweight `check_test(name, actual, expected, tol=1e-3)` helper for standardized `✅` / `❗` visual test verification).
   - Write the valid JSON `.ipynb` notebook directly to [path/to/build.ipynb] so I can start practicing immediately.