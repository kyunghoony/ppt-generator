import os
import sys

# Add src to path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.engine import generate
import json

def main():
    base_dir = os.path.dirname(os.path.dirname(__file__))
    
    # Generate generic
    generic_input = os.path.join(base_dir, "examples", "sample_input.json")
    with open(generic_input, "r", encoding="utf-8") as f:
        data = json.load(f)
    out1 = generate(data, preset="default", output_path=os.path.join(base_dir, "output", "generic_sample.pptx"))
    print(f"Generated {out1}")
    
    # Generate FV
    fv_input = os.path.join(base_dir, "examples", "sample_deal_sourcing.json")
    with open(fv_input, "r", encoding="utf-8") as f:
        data2 = json.load(f)
    out2 = generate(data2, preset="fv", template="deal_sourcing", output_path=os.path.join(base_dir, "output", "fv_sample.pptx"))
    print(f"Generated {out2}")

if __name__ == "__main__":
    main()
