import io

from matplotlib.backends.backend_svg import FigureCanvasSVG

from models.Restaurants import Restaurant
from models.Orders import Orders
from models.Foods import Foods
from algorithms.statistics_based_on_kind_of_food import get_statistics_per_restaurant


def main(restaurant_id):
    fig = get_statistics_per_restaurant(Restaurant.by_id(restaurant_id), Foods.all(), Orders.all())
    output = io.BytesIO()
    FigureCanvasSVG(fig).print_svg(output)
    return output.getvalue()
