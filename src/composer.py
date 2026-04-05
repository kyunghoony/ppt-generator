from typing import List, Dict, Any
from .primitives import (
    TitleSlide, SectionDivider, ContentSlide, TwoColumnSlide,
    ImageSlide, ChartSlide, TableSlide, ComparisonSlide,
    TimelineSlide, MetricSlide, BlankSlide, SlidePrimitive
)

def parse_input(input_data: Dict[str, Any], template_data: Dict[str, Any] = None) -> List[SlidePrimitive]:
    """Converts JSON input into a list of SlidePrimitives."""
    slides_data = input_data.get("slides", [])
    primitives = []
    
    for slide in slides_data:
        stype = slide.get("type")
        if stype == "title":
            primitives.append(TitleSlide(
                title=slide.get("title", ""),
                subtitle=slide.get("subtitle"),
                background_image=slide.get("background_image")
            ))
        elif stype == "section_divider":
            primitives.append(SectionDivider(
                title=slide.get("title", ""),
                subtitle=slide.get("subtitle")
            ))
        elif stype == "content":
            primitives.append(ContentSlide(
                title=slide.get("title", ""),
                body=slide.get("body", ""),
                bullets=slide.get("bullets")
            ))
        elif stype == "two_column":
            primitives.append(TwoColumnSlide(
                title=slide.get("title", ""),
                left_content=slide.get("left_content", ""),
                right_content=slide.get("right_content", "")
            ))
        elif stype == "image":
            primitives.append(ImageSlide(
                title=slide.get("title", ""),
                image_path=slide.get("image_path", ""),
                caption=slide.get("caption")
            ))
        elif stype == "chart":
            primitives.append(ChartSlide(
                title=slide.get("title", ""),
                chart_type=slide.get("chart_type", "bar"),
                data=slide.get("data", {}),
                labels=slide.get("labels", [])
            ))
        elif stype == "table":
            primitives.append(TableSlide(
                title=slide.get("title", ""),
                headers=slide.get("headers", []),
                rows=slide.get("rows", [])
            ))
        elif stype == "comparison":
            primitives.append(ComparisonSlide(
                title=slide.get("title", ""),
                left_label=slide.get("left_label", ""),
                right_label=slide.get("right_label", ""),
                left_items=slide.get("left_items", []),
                right_items=slide.get("right_items", [])
            ))
        elif stype == "timeline":
            primitives.append(TimelineSlide(
                title=slide.get("title", ""),
                events=slide.get("events", [])
            ))
        elif stype == "metrics":
            primitives.append(MetricSlide(
                title=slide.get("title", ""),
                metrics=slide.get("metrics", [])
            ))
        elif stype == "blank":
            primitives.append(BlankSlide())
            
    return primitives
