
def create_barh_plot(food_label, quantity):
    import os
    import numpy as np
    import matplotlib.pyplot as plt

    x = food_label
    y = quantity
    color_1 = "#a71d31"  # red
    color_2 = "#386150"  # green
    color_3 = "#2b2633"  # black
    color_4 = "#453d52"  # light-black

    fig, ax = plt.subplots(figsize=(14, 8))
    plt.title('Food per restaurant statistic', fontsize=18, fontweight='bold')

    width = 0.85
    ind = np.arange(len(y))

    ax.barh(ind, y, width, color=[color_1, color_2, color_3], alpha=0.95)
    ax.set_yticks(ind + width / 2)
    ax.set_yticklabels(x, minor=False)

    for i, v in enumerate(y):
        ax.text(v + 0.02, i - 0.08, str(v), color='black', fontweight='bold')

    for i, v in enumerate(x):
        ax.text(0.2, i - 0.08, v, color='white', fontweight='bold')

    ax.xaxis.set_ticks_position('bottom')
    ax.tick_params(axis='x', colors=color_4, labelsize=8)
    ax.set_yticks([])
    ax.margins(0, 0.02)
    ax.grid(which='major', axis='x', linestyle='dashed')
    ax.set_axisbelow(True)
    plt.box(False)

    plt.savefig("test.svg", format="svg")

    plt.show()


def get_statistics_per_restaurant(restaurant_id, foods, orders):

    food_dict = {}
    tick_label = []
    height = []

    for food in foods:
        if food["restaurant_id"] == restaurant_id:
            food_dict[food["_id"]] = {"name": food["name"], "quantity": 0}

    for order in orders:
        if order["restaurant_id"] == restaurant_id:
            food_dict[order["food_id"]]["quantity"] += 1

    for food in food_dict:
        tick_label.append(food_dict[food]["name"])
        height.append(food_dict[food]["quantity"])

    create_barh_plot(tick_label, height)


from db import restaurantsCollection

get_statistics_per_restaurant(restaurantsCollection.find()[53]["_id"])
