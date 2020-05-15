import Constants


def get_food_by_id(food_id, foods):
    for food in foods:
        if food[Constants.ID] == food_id:
            return food
    return -1


# returneaza o lista cu numele mancarurilor disponibile la restaurant
# not used
def get_restaurant_menu(restaurant, foods):
    menu = []
    for food in foods:
        if food[Constants.RESTAURANT_ID] == restaurant[Constants.ID]:
            menu.append(food['name'])
    return menu


def get_customer_other_course_ids(user_id, orders, restaurant_courses_ids):
    customer_other_foods = {}
    for order in orders:
        if order[Constants.USER_ID] == user_id:
            for item in order[Constants.ITEMS]:
                if item[Constants.ID] not in restaurant_courses_ids:
                    if item[Constants.ID] not in customer_other_foods:
                        customer_other_foods[item[Constants.ID]] = 1
                    else:
                        customer_other_foods[item[Constants.ID]] += 1
            # food = get_food_by_id(order['food_id'], foods)
            # if food['name'] not in restaurant_menu:
            #     if food['name'] not in customer_other_foods:
            #         customer_other_foods[food['name']] = 1
            #     else:
            #         customer_other_foods[food['name']] += 1
    return customer_other_foods


# returneaza un dictionar cu perechi customer_id - numar de comenzi la restaurant
def get_restaurant_clients(restaurant, orders):
    clients = {}
    for order in orders:
        if order[Constants.RESTAURANT_ID] == restaurant[Constants.ID]:
            if order[Constants.USER_ID] not in clients:
                clients[order[Constants.USER_ID]] = 1
            else:
                clients[order[Constants.USER_ID]] += 1
    return clients


# am sters foods de la parametri
def final(restaurant, orders):
    recommendations = {}
    clients = get_restaurant_clients(restaurant, orders)
    restaurant_menu = restaurant[Constants.DETAILS][Constants.MENU][Constants.COURSES]
    restaurant_courses_ids = []
    for course in restaurant_menu:
        restaurant_courses_ids.append(course[Constants.ID])
    # print(restaurant_menu)
    for userId in clients:
        customer_other_foods = get_customer_other_course_ids(userId, orders, restaurant_courses_ids)
        for food in customer_other_foods:
            if food not in recommendations:
                recommendations[food] = 1 + 0.2 * customer_other_foods[food] * clients[userId]
            else:
                recommendations[food] = 1 + 0.2 * customer_other_foods[food] * clients[userId]

    result = {k: v for k, v in sorted(recommendations.items(), key=lambda item: item[1], reverse=True)}
    print(list(result.keys())[:10])
    return list(result.keys())[:10]


# ruta de test: http://127.0.0.1:5000/recommendations/food/5eb16d673a637d28884dc226 7 mai 2020
# http://127.0.0.1:5000/recommendations/food/5e9494aadd757435187a6dbd
