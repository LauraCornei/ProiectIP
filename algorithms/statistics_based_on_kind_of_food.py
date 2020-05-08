
# http://127.0.0.1:5000/recommendations/stats/food_per_restaurant/5e958949564a0055b294ce83/desc/false/-1
# http://127.0.0.1:5000/recommendations/stats/food_per_restaurant/5eb16d673a637d28884dc226?order=asc&token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJfaWQiOiI1ZWFhOTQ2ODMwYThmMTI5OGQ0ZmMyZjgiLCJpYXQiOjE1ODgyMzc0NTZ9.Ll2HDuN79KKWr5OoQTiZVWBemyDqdo3kDz74Bvi6lOA


def create_bar_plot(food_label, quantity):
    import numpy as np
    import matplotlib.pyplot as plt

    COLOR_RED = "#a71d31"      
    COLOR_GREEN = "#386150"  
    COLOR_BLACK = "#2b2633"  
    COLOR_BLACK_LIGHT = "#453d52"  
    COLOR_GRAY = "#dbdbdb"
    FIG_WIDTH = 14
    FIG_HEIGHT = 8
    TEXT_FONT_SIZE = 18
    PADDING = 0.08
    ALPHA = 0.95
    MARGIN_LR = 0
    MARGIN_TB = 0.2 

    x = food_label
    y = quantity
    

    fig, ax = plt.subplots(figsize=(FIG_WIDTH, FIG_HEIGHT))
    plt.title('Food per restaurant statistic', fontsize=TEXT_FONT_SIZE, fontweight='bold')

    width = 0.85
    ind = np.arange(len(y))

    ax.barh(ind, y, width, color=[COLOR_RED, COLOR_GREEN, COLOR_BLACK], alpha=ALPHA)
    ax.set_yticks(ind + width / 2)
    ax.set_yticklabels(x, minor=False)

    vmax = 0
    for i, v in enumerate(y):
        vmax = max(vmax, v)
    for i, v in enumerate(y):
        ax.text(max(v + 0.5, vmax / 5), i - PADDING, str(v), color='black', fontweight='bold')

    for i, v in enumerate(x):
        ax.text(0.2, i - PADDING, v, color=COLOR_GRAY, fontweight='bold')

    ax.xaxis.set_ticks_position('bottom')
    ax.tick_params(axis='x', colors=COLOR_BLACK_LIGHT, labelsize=8)
    ax.set_yticks([])
    ax.margins(MARGIN_LR, MARGIN_TB)
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



