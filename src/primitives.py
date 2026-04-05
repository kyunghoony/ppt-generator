from dataclasses import dataclass, field
from typing import List, Dict, Any, Optional

@dataclass
class SlidePrimitive:
    slide_type: str = field(init=False)

@dataclass
class TitleSlide(SlidePrimitive):
    title: str
    subtitle: Optional[str] = None
    background_image: Optional[str] = None
    slide_type: str = field(default="title", init=False)

@dataclass
class SectionDivider(SlidePrimitive):
    title: str
    subtitle: Optional[str] = None
    slide_type: str = field(default="section_divider", init=False)

@dataclass
class ContentSlide(SlidePrimitive):
    title: str
    body: str
    bullets: Optional[List[str]] = None
    slide_type: str = field(default="content", init=False)

@dataclass
class TwoColumnSlide(SlidePrimitive):
    title: str
    left_content: str
    right_content: str
    slide_type: str = field(default="two_column", init=False)

@dataclass
class ImageSlide(SlidePrimitive):
    title: str
    image_path: str
    caption: Optional[str] = None
    slide_type: str = field(default="image", init=False)

@dataclass
class ChartSlide(SlidePrimitive):
    title: str
    chart_type: str  # bar, line, pie
    data: Dict[str, List[float]]
    labels: List[str]
    slide_type: str = field(default="chart", init=False)

@dataclass
class TableSlide(SlidePrimitive):
    title: str
    headers: List[str]
    rows: List[List[str]]
    slide_type: str = field(default="table", init=False)

@dataclass
class ComparisonSlide(SlidePrimitive):
    title: str
    left_label: str
    right_label: str
    left_items: List[str]
    right_items: List[str]
    slide_type: str = field(default="comparison", init=False)

@dataclass
class TimelineSlide(SlidePrimitive):
    title: str
    events: List[Dict[str, str]]  # date, description
    slide_type: str = field(default="timeline", init=False)

@dataclass
class MetricSlide(SlidePrimitive):
    title: str
    metrics: List[Dict[str, str]]  # label, value, delta
    slide_type: str = field(default="metrics", init=False)

@dataclass
class BlankSlide(SlidePrimitive):
    slide_type: str = field(default="blank", init=False)
