# Rule: Mandatory User Consent Before Heavy Downloads or Imports

- **Always ask for user permission first** before downloading, caching, or importing large files, model weights, checkpoints, or datasets (e.g. any file or package > 100 MB, such as Hugging Face models, PyTorch hub checkpoints, or large corpora).
- **Provide clear transparency before executing**:
  1. State the exact or estimated download size (e.g. ~2.4 GB).
  2. State where the files will be stored on disk (e.g. `~/.cache/huggingface/hub/`).
  3. State the estimated RAM/VRAM footprint during inference or loading.
- **Offer lightweight alternatives**: Always mention whether smaller alternatives exist (e.g. smaller/quantized models, subword toy models, or lighter datasets).
- **Never proceed with heavy network downloads silently** without the user's explicit consent.
