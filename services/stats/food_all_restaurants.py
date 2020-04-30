import io

from matplotlib.backends.backend_svg import FigureCanvasSVG

from models.Orders import Orders
from models.Foods import Foods
from algorithms.statistics_based_on_kind_of_food import get_statistics_per_restaurant


def main(order, show_count):
    restaurant_id = 0
    fig = get_statistics_per_restaurant(restaurant_id, Orders.all(), order, int(show_count))
    output = io.BytesIO()
    FigureCanvasSVG(fig).print_svg(output)
    return output.getvalue()
