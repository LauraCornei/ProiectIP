
# http://127.0.0.1:5000/recommendations/stats/food_per_restaurant/5e958949564a0055b294ce83/desc/false/-1
# http://127.0.0.1:5000/recommendations/stats/food_per_restaurant/5e9494aadd757435187a6dbd?order=asc&token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJfaWQiOiI1ZWFhOTQ2ODMwYThmMTI5OGQ0ZmMyZjgiLCJpYXQiOjE1ODgyMzc0NTZ9.Ll2HDuN79KKWr5OoQTiZVWBemyDqdo3kDz74Bvi6lOA
import Constants

def create_bar_plot(food_label, quantity):
    import numpy as np
    import matplotlib.pyplot as plt

    x = food_label
    y = quantity

    fig, ax = plt.subplots(figsize=(Constants.FIG_WIDTH, Constants.FIG_HEIGHT))
    plt.title('Food per restaurant statistic', fontsize=Constants.TEXT_FONT_SIZE, fontweight='bold')

    width = 0.85
    ind = np.arange(len(y))

    ax.barh(ind, y, width, color=[Constants.COLOR_RED, Constants.COLOR_GREEN, Constants.COLOR_BLACK], alpha=Constants.ALPHA)
    ax.set_yticks(ind + width / 2)
    ax.set_yticklabels(x, minor=False)

    vmax = 0
    for i, v in enumerate(y):
        vmax = max(vmax, v)
    for i, v in enumerate(y):
        ax.text(max(v + 0.5, vmax / 5), i - Constants.PADDING, str(v), color='black', fontweight='bold')

    for i, v in enumerate(x):
        ax.text(0.2, i - Constants.PADDING, v, color=Constants.COLOR_GRAY, fontweight='bold')

    ax.xaxis.set_ticks_position('bottom')
    ax.tick_params(axis='x', colors=Constants.COLOR_BLACK_LIGHT, labelsize=8)
    ax.set_yticks([])
    ax.margins(Constants.MARGIN_LR, Constants.MARGIN_TB)
    ax.grid(which='major', axis='x', linestyle='dashed')
    ax.set_axisbelow(True)
    plt.box(False)
    return fig


def get_statistics_per_restaurant(restaurant_id, orders, sort_order, show_count):
    food_name_by_id = {}
    food_dict = {}
    tick_label = []
    height = []
    for order in orders:
        for item in order["items"]:
            if restaurant_id == 0 or order["restaurantId"] == restaurant_id:
                food_dict[item["item"]["product"]] = 0
                food_name_by_id[item["item"]["product"]] = item["item"]["product"]

    for order in orders:
        for item in order["items"]:
            if restaurant_id == 0 or order["restaurantId"] == restaurant_id:
                food_dict[food_name_by_id[item["item"]["product"]]] += item["item"]["quantity"]

    sorted_food_dict = {}
    if sort_order == "asc":
        sorted_food_dict = sorted(food_dict.items(), key=lambda kv: kv[1])
    elif sort_order == "desc":
        sorted_food_dict = sorted(food_dict.items(), key=lambda kv: kv[1], reverse=True)

    if show_count == -1:
        print_count = 20
    else:
        print_count = show_count

    for food in sorted_food_dict:
        tick_label.append(food[0])
        height.append(food[1])
        print_count -= 1
        if print_count <= 0:
            break

    return create_bar_plot(tick_label, height)



