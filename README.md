# PPT Generator

A universal PPT generation engine designed to be used primarily through Claude Code.

## Architecture Overview
- **Engine is GENERIC**: Produces any PPT for any brand/use case.
- **Presets**: Brand-specific styling is handled through PRESETS (YAML config + assets).
- **Input**: Structured JSON (or natural language → JSON via Claude Code).
- **Output**: `.pptx` file.
- **Core Technology**: Built on `python-pptx`. No external API dependencies for core generation.

## Quick Start
```bash
pip install -r requirements.txt
python -m src.engine --input examples/sample_input.json --preset default --output output/result.pptx
```

## How to Add Presets
1. Create a new directory under `presets/`, e.g., `presets/mybrand/`.
2. Add a `config.yaml` file with colors, fonts, and layout settings.
3. Add any required assets to `presets/mybrand/assets/`.
4. (Optional) Add deck templates like `pitch_deck.yaml`.
