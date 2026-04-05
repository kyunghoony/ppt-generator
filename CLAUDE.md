# PPT Generator — Claude Code Instructions

## What This Is
Python-based PPT generation engine. You create .pptx files by calling the engine with structured input.

## Quick Start
```bash
cd /path/to/ppt-generator
pip install -r requirements.txt
python -m src.engine --input examples/sample_input.json --preset default --output output/result.pptx
```

## How to Generate a PPT

### Step 1: Prepare Input JSON
Structure your content as JSON matching the slide primitives:
```json
{
  "title": "Deck Title",
  "preset": "fv",
  "template": "deal_sourcing",
  "slides": [
    {"type": "title", "title": "Company X — Deal Sourcing", "subtitle": "2026.04"},
    {"type": "metrics", "title": "Key Metrics", "metrics": [
      {"label": "ARR", "value": "₩2.4B", "delta": "+42% YoY"},
      {"label": "Burn Rate", "value": "₩180M/mo"},
      {"label": "Runway", "value": "14 months"}
    ]},
    {"type": "content", "title": "Investment Thesis", "body": "..."}
  ]
}
```

### Step 2: Run Generation
```bash
python -m src.engine --input input.json --output output/deck.pptx
```

Or programmatically:
```python
from src.engine import generate
result = generate(input_data=data, preset="fv", template="deal_sourcing")
```

## Preset Auto-Detection Rules
- Keywords: 딜소싱, 딜, deal, sourcing → preset=fv, template=deal_sourcing
- Keywords: 포트폴리오, portfolio, review → preset=fv, template=portfolio_report
- Keywords: IDM, 투심, investment memo → preset=fv, template=idm
- No FV keyword detected → preset=default, no template

## Adding a New Preset
1. Create `presets/{name}/config.yaml` (copy from default)
2. Add brand assets to `presets/{name}/assets/`
3. Optionally create deck templates as `{template_name}.yaml`

## Slide Types Available
title, section_divider, content, two_column, image, chart, table, comparison, timeline, metrics, blank

## Rules
- Always output .pptx to `output/` directory
- Korean text: ensure font supports Hangul (Pretendard, 맑은 고딕, Noto Sans KR)
- Charts: use preset colors for consistency
- Images: auto-resize to fit slide, maintain aspect ratio
- If user gives natural language, convert to JSON structure first, then generate
