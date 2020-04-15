from algorithms.stat10 import main_hours
from matplotlib.backends.backend_svg import FigureCanvasSVG
import io
from models.Orders import Orders


def main():
    fig = main_hours(Orders.all())
    output = io.BytesIO()
    FigureCanvasSVG(fig).print_svg(output)
    return output.getvalue()
