from src.composer import parse_input
from src.primitives import TitleSlide

def test_parse_input():
    data = {
        "slides": [
            {"type": "title", "title": "Parsed Title"}
        ]
    }
    primitives = parse_input(data)
    assert len(primitives) == 1
    assert isinstance(primitives[0], TitleSlide)
    assert primitives[0].title == "Parsed Title"
