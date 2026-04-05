import os
from src.engine import generate

def test_generate_simple():
    input_data = {
        "slides": [
            {"type": "title", "title": "Test Title"}
        ]
    }
    output_path = "output/test_result.pptx"
    result = generate(input_data, output_path=output_path)
    assert os.path.exists(result)
