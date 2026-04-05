from pptx.chart.data import CategoryChartData
from pptx.enum.chart import XL_CHART_TYPE
from pptx.util import Inches

def add_chart_to_slide(slide, chart_type: str, data: dict, labels: list, left, top, width, height):
    """Adds a chart to the given slide."""
    chart_data = CategoryChartData()
    chart_data.categories = labels
    
    for series_name, series_values in data.items():
        chart_data.add_series(series_name, series_values)
        
    ctype = XL_CHART_TYPE.COLUMN_CLUSTERED
    if chart_type == "line":
        ctype = XL_CHART_TYPE.LINE
    elif chart_type == "pie":
        ctype = XL_CHART_TYPE.PIE
        
    chart = slide.shapes.add_chart(
        ctype, left, top, width, height, chart_data
    ).chart
    return chart
