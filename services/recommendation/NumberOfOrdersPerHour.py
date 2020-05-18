from algorithms.number_of_orders_per_hour import main_hours
from matplotlib.backends.backend_svg import FigureCanvasSVG
import io
from models.Orders import Orders


def number_of_orders(token):
    fig = main_hours(Orders.all(token))
    output = io.BytesIO()
    FigureCanvasSVG(fig).print_svg(output)
    return output.getvalue()


def number_of_orders_by_restaurant(restaurant_id, token):
    fig = main_hours(Orders.by_res_id(restaurant_id, token))
    output = io.BytesIO()
    FigureCanvasSVG(fig).print_svg(output)
    return output.getvalue()
