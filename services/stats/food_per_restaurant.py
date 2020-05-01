import io

from matplotlib.backends.backend_svg import FigureCanvasSVG

from models.Orders import Orders
from algorithms.statistics_based_on_kind_of_food import get_statistics_per_restaurant


def main(restaurant, order, show_count, token):
    restaurant_id = restaurant
    fig = get_statistics_per_restaurant(restaurant_id, Orders.all(token), order, int(show_count))
    output = io.BytesIO()
    FigureCanvasSVG(fig).print_svg(output)
    return output.getvalue()
