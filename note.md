source .venv/bin/activate -> trc khi hoc (hoặc Windows PowerShell: .\.venv\Scripts\Activate.ps1)

================================================================================
PROMPT GENERATE JUPYTER NOTEBOOK PRACTICE SCAFFOLD (BUILD.IPYNB)
================================================================================

Act as a coding mentor. I have the reference solution at [path/to/solution.py] and the lesson documentation at [path/to/docs/en.md].
Please create an interactive practice scaffold Jupyter Notebook for me directly at [path/to/build.ipynb].

Follow these rules strictly:

1. **Intuition Block (Warm-up & Mental Model at the Beginning)**:
   - Place this block right after the Setup cell and before `Step 1`.
   - Purpose: Give the learner an intuitive preview of the algorithms and code structures they will build, building familiarity with new functions and mechanics before coding from scratch.
   - It must contain:
     * A **Markdown Cell**:
       - Title: `## Intuition & Quick Walkthrough`
       - Brief conceptual summary connecting the core mathematical ideas to the programming workflow.
     * A **Code Cell (Fully Working, Runnable Sandbox)**:
       - Provide a compact, self-contained working demo summarizing the core operations of the lesson.
       - **CRITICAL RULE - COMPLETELY DIFFERENT NUMBERS / DATA**: All variables, test inputs, distributions, and numbers MUST be completely different from the actual `docs/en.md` examples and the subsequent Step test cases (e.g. use different toy values, different dimensions, different seeds, or different probabilities).
       - The learner can run this cell immediately to observe output shapes, flow of data, and behavior without spoiling the exact step solutions.

2. **Core Steps (Strictly match `## Build It` in docs)**:
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

3. **Extra Concepts Section (From Reference Solution)**:
   - Compare the author's reference solution in [path/to/solution.py] against the `## Build It` section in [path/to/docs/en.md].
   - Any function that the author implemented in the reference code but is NOT covered in the `## Build It` steps of the docs MUST be placed into an Extra section at the end of the notebook.
   - Sub-split each extra concept individually (`Extra 1: ...`, `Extra 2: ...`), each having:
     * A Markdown cell with brief overview and LaTeX mathematical formula (if the body implements math).
     * A Code cell with scaffold (`pass`, `# TODO:`, `# Hint:`, `# Example:`) and immediate visual test verification (`✅` / `❗`).

4. **Scaffold & Hint Pedagogical Quality (NO SPOON-FEEDING)**:
   - Extract exact signatures, parameters, and type hints from the solution.
   - Replace all implementation logic with `pass`.
   - Inside each function:
     * `# TODO:` explains the objective, the mathematical definition, and parameter roles.
     * `# Example:` a short, concrete sample of input arguments and expected return value (e.g. `# Example: values = [1, 2, 3], probabilities = [0.2, 0.5, 0.3] -> returns 2.1`).
     * `# Hint:` explains algorithmic logic flow, math formula (in general mathematical notation, not Python code), and edge cases.
   - **CRITICAL ANTI-PATTERN TO AVOID**: NEVER provide raw Python one-liner code in hints/TODOs (e.g. NEVER write `# Hint: Return p if k == 1 else 1-p`). The learner must translate the math and logic into Python themselves.

5. **Authentic APIs - Never Use Fake Mock Doubles**:
   - When `docs/en.md` demonstrates real production libraries (such as Hugging Face `transformers`, `torch`, `sacrebleu`, `sentencepiece`, etc.), **REPLICATE the real library calls and APIs directly**.
   - **STRICTLY FORBIDDEN**: NEVER invent synthetic mock/recording classes (such as `RecordingTokenizer`, `RecordingModel`, `RecordingAgent`) that intercept calls or hardcode dummy return values (e.g. `[[11, 12]]` or `["Les chats courent."]`). 
   - Real learning requires authentic interactions with production tools and genuine data structures.

6. **User Consent for Heavy Downloads & Imports**:
   - **MANDATORY PERMISSION CHECK**: Whenever a step requires downloading or importing large files, model weights, checkpoints, or datasets (e.g. > 100 MB from Hugging Face Hub, torch hub, or external URLs), the mentor/assistant **MUST explicitly ask for the user's consent first**.
   - Clearly inform the user of:
     * The exact download size (e.g. ~2.4 GB for NLLB-200-distilled-600M).
     * The expected disk storage location (e.g. `~/.cache/huggingface/hub/`).
     * The estimated RAM/VRAM footprint during inference.
   - Always offer lighter alternative options (e.g. smaller ~300MB models, quantized variants, or running on cloud APIs) so the user is in full control of their machine's storage and bandwidth.

7. **Clear Visual Section Boundaries in Every Code Cell**:
   - Every code cell with exercises must have prominent, explicit section banners separating test fixtures, student code, and automated tests:
     ```python
     # ==============================================================================
     # SETUP / FIXTURES (Do not modify - if applicable)
     # ==============================================================================
     ...

     # ==============================================================================
     # YOUR IMPLEMENTATION
     # ==============================================================================
     def my_function(...):
         ### YOUR CODE HERE ###
         pass
         ### END CODE ###

     # ==============================================================================
     # TESTS & VERIFICATION
     # ==============================================================================
     run_check(...)
     ```
   - This ensures the learner never confuses test fixtures or helper harnesses with the code they are supposed to implement.
8. **Formatting & Language**:
   - Write all Markdown cells, code comments, and test printouts in English.
   - Include a Setup Cell at the very top (imports, seed, and a lightweight `check_test(name, actual, expected, tol=1e-3)` helper for standardized `✅` / `❗` visual test verification).
   - Write the valid JSON `.ipynb` notebook directly to [path/to/build.ipynb] so I can start practicing immediately.