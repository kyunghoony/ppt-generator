from src.primitives import TitleSlide

def test_title_slide():
    slide = TitleSlide(title="Hello")
    assert slide.title == "Hello"
    assert slide.slide_type == "title"
