import json
import click
import os
from .styles import load_preset, load_template
from .composer import parse_input
from .renderer import Renderer

def generate(input_data: dict, preset: str = "default", template: str = None, output_path: str = None) -> str:
    """
    Main generation function.
    1. Load preset config (merge default + preset-specific)
    2. If template specified, load deck template YAML
    3. Parse input_data into list of slide primitives via composer
    4. Render each primitive to .pptx via renderer
    5. Save to output_path, return file path
    """
    config = load_preset(preset)
    template_data = load_template(preset, template) if template else None
    
    primitives = parse_input(input_data, template_data)
    
    renderer = Renderer(config)
    
    if not output_path:
        output_path = "output/result.pptx"
        
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    renderer.render(primitives, output_path)
    
    return output_path

@click.command()
@click.option('--input', 'input_file', required=True, help='Path to input JSON file')
@click.option('--preset', default='default', help='Preset name (e.g., default, fv)')
@click.option('--template', default=None, help='Template name (e.g., deal_sourcing)')
@click.option('--output', 'output_file', default='output/result.pptx', help='Output PPTX path')
def cli(input_file, preset, template, output_file):
    """Generate a PPTX file from JSON input."""
    with open(input_file, 'r', encoding='utf-8') as f:
        input_data = json.load(f)
        
    # Auto-detect preset/template from input if not provided
    if "preset" in input_data and preset == 'default':
        preset = input_data["preset"]
    if "template" in input_data and template is None:
        template = input_data["template"]
        
    result_path = generate(input_data, preset, template, output_file)
    click.echo(f"Successfully generated PPTX at: {result_path}")

if __name__ == '__main__':
    cli()
