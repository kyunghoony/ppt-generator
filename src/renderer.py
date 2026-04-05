from pptx import Presentation
from pptx.util import Inches, Pt
from typing import List, Dict, Any
from .primitives import (
    SlidePrimitive, TitleSlide, SectionDivider, ContentSlide,
    TwoColumnSlide, ImageSlide, ChartSlide, TableSlide,
    ComparisonSlide, TimelineSlide, MetricSlide, BlankSlide
)
from .utils import hex_to_rgb, apply_text_style
from .charts import add_chart_to_slide

class Renderer:
    def __init__(self, config: Dict[str, Any]):
        self.config = config
        self.prs = Presentation()
        
        # Set slide size
        width = config.get("slide_size", {}).get("width", 13.333)
        height = config.get("slide_size", {}).get("height", 7.5)
        self.prs.slide_width = Inches(width)
        self.prs.slide_height = Inches(height)
        
        # Layouts
        self.title_layout = self.prs.slide_layouts[0]
        self.blank_layout = self.prs.slide_layouts[6]
        
    def render(self, primitives: List[SlidePrimitive], output_path: str):
        for primitive in primitives:
            self._render_slide(primitive)
        self.prs.save(output_path)
        
    def _render_slide(self, primitive: SlidePrimitive):
        if isinstance(primitive, TitleSlide):
            slide = self.prs.slides.add_slide(self.title_layout)
            title = slide.shapes.title
            subtitle = slide.placeholders[1]
            title.text = primitive.title
            if primitive.subtitle:
                subtitle.text = primitive.subtitle
            # Apply styles
            self._apply_title_style(title)
            self._apply_subtitle_style(subtitle)
            
        elif isinstance(primitive, ContentSlide):
            slide = self.prs.slides.add_slide(self.blank_layout)
            # Add title
            title_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.5), Inches(11.7), Inches(1))
            title_box.text = primitive.title
            self._apply_title_style(title_box)
            
            # Add body
            body_box = slide.shapes.add_textbox(Inches(0.8), Inches(1.8), Inches(11.7), Inches(5))
            tf = body_box.text_frame
            tf.text = primitive.body
            if primitive.bullets:
                for bullet in primitive.bullets:
                    p = tf.add_paragraph()
                    p.text = bullet
                    p.level = 1
            self._apply_body_style(body_box)
            
        elif isinstance(primitive, ChartSlide):
            slide = self.prs.slides.add_slide(self.blank_layout)
            title_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.5), Inches(11.7), Inches(1))
            title_box.text = primitive.title
            self._apply_title_style(title_box)
            
            add_chart_to_slide(
                slide, primitive.chart_type, primitive.data, primitive.labels,
                Inches(0.8), Inches(1.8), Inches(11.7), Inches(5)
            )
            
        elif isinstance(primitive, MetricSlide):
            slide = self.prs.slides.add_slide(self.blank_layout)
            title_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.5), Inches(11.7), Inches(1))
            title_box.text = primitive.title
            self._apply_title_style(title_box)
            
            # Simple layout for metrics
            num_metrics = len(primitive.metrics)
            if num_metrics > 0:
                width = 11.7 / num_metrics
                for i, metric in enumerate(primitive.metrics):
                    left = 0.8 + (i * width)
                    box = slide.shapes.add_textbox(Inches(left), Inches(3), Inches(width-0.2), Inches(2))
                    tf = box.text_frame
                    tf.text = f"{metric.get('label', '')}\n{metric.get('value', '')}\n{metric.get('delta', '')}"
                    self._apply_body_style(box)
                    
        else:
            # Fallback for other types
            slide = self.prs.slides.add_slide(self.blank_layout)
            title_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.5), Inches(11.7), Inches(1))
            title_box.text = getattr(primitive, 'title', 'Untitled Slide')
            self._apply_title_style(title_box)

    def _apply_title_style(self, shape):
        font_name = self.config.get("fonts", {}).get("title", "Arial")
        font_size = self.config.get("fonts", {}).get("title_size", 28)
        color = self.config.get("colors", {}).get("text_primary", "#000000")
        for paragraph in shape.text_frame.paragraphs:
            for run in paragraph.runs:
                apply_text_style(run, font_name, font_size, color)

    def _apply_subtitle_style(self, shape):
        font_name = self.config.get("fonts", {}).get("body", "Arial")
        font_size = self.config.get("fonts", {}).get("body_size", 18)
        color = self.config.get("colors", {}).get("text_secondary", "#555555")
        for paragraph in shape.text_frame.paragraphs:
            for run in paragraph.runs:
                apply_text_style(run, font_name, font_size, color)

    def _apply_body_style(self, shape):
        font_name = self.config.get("fonts", {}).get("body", "Arial")
        font_size = self.config.get("fonts", {}).get("body_size", 14)
        color = self.config.get("colors", {}).get("text_primary", "#000000")
        for paragraph in shape.text_frame.paragraphs:
            for run in paragraph.runs:
                apply_text_style(run, font_name, font_size, color)
