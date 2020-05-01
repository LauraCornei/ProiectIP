import matplotlib.pyplot as plt

# http://127.0.0.1:5000/recommendations/stats/customers_per_hours


def get_hour_of(order):
    digit1 = order['orderDate'][11:12]
    digit2 = order['orderDate'][12:13]
    digit1 = int(digit1)
    digit2 = int(digit2)
    ind = digit1*10+digit2
    return ind


def get_min_of(order):
    digit1 = order['orderDate'][11:12]
    digit2 = order['orderDate'][12:13]
    digit1 = int(digit1)
    digit2 = int(digit2)

    digit1_m = order['orderDate'][14:15]
    digit2_m = order['orderDate'][15:16]
    digit1_m = int(digit1_m)
    digit2_m = int(digit2_m)

    ind = (digit1*10+digit2)*60+(digit1_m*10+digit2_m)
    return ind


def calc_no_orders_hours(orders):
    no_orders = [0] * 24
    for order in orders:
        ind = get_hour_of(order)
        no_orders[ind] += 1
    return no_orders


def main_hours(orders):
    fig, ax = plt.subplots()
    hours = [0] * 24
    for ind in range(0, 24):
        hours[ind] = ind

    no_orders = calc_no_orders_hours(orders)

    ax.plot(hours, no_orders)
    ax.set(xlabel='Time of order (hours)', ylabel='No of orders ', title='Number of orders pe hour')
    ax.grid()
    return fig
