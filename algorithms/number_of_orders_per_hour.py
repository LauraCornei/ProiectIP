import matplotlib.pyplot as plt

# http://127.0.0.1:5000/recommendations/stats/orders_per_hour
import Constants


def get_hour_of(order):
    ind = int(order[Constants.ORDER_DATE][11:13])
    return ind


# not used
def get_min_of(order):
    digit_h = int(order[Constants.ORDER_DATE][11:13])
    digit_m = int(order[Constants.ORDER_DATE][14:16])

    ind = digit_h*60+digit_m
    return ind


def calc_no_orders_hours(orders):
    no_orders = [0] * 24
    for order in orders:
        ind = get_hour_of(order)
        no_orders[ind] += 1
    return no_orders


def main_hours(orders):
    print(orders)
    fig, ax = plt.subplots()
    hours = [0] * 24
    for ind in range(0, 24):
        hours[ind] = ind

    no_orders = calc_no_orders_hours(orders)

    ax.plot(hours, no_orders)
    ax.set(xlabel='Time of order (hours)', ylabel='No of orders ', title='Number of orders per hour')
    ax.grid()
    return fig
