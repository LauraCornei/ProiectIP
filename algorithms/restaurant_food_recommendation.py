import Constants
from bson import ObjectId


def filter_orders(orders, restaurant_id):
    restaurant_orders = []
    for order in orders:
        if order['restaurantId'] == restaurant_id:
            restaurant_orders.append(order)
    return restaurant_orders


def get_customer_food_dict(customer_id, orders):
    customer_foods = {}
    for order in orders:
        if 'userId' not in order:
            continue

        if order['userId'] == customer_id:
            if 'items' not in order:
                continue
            for item in order['items']:
                #speram ca am ales id bun items (2 optiuni: _id, id)
                if item["id"] not in customer_foods:
                    customer_foods[item["id"]] = 1
                else:
                  customer_foods[item["id"]] += 1
    return customer_foods


def get_similarity(customer_dict1, customer_dict2):
    score = 0
    for food_id in customer_dict1:
        if food_id in customer_dict2:
            score += (customer_dict1[food_id] + customer_dict2[food_id]) / 2
    return score


def get_recommended_foods(similar_customers_foods, similar_customers_ordered):
    food_dict = {}
    for customer_id in similar_customers_foods:
        for food_id in similar_customers_foods[customer_id]:
            if food_id not in food_dict:
                food_dict[food_id] = similar_customers_foods[customer_id][food_id] * similar_customers_ordered[
                    customer_id]
            else:
                food_dict[food_id] += similar_customers_foods[customer_id][food_id] * similar_customers_ordered[
                    customer_id]
    recommended_foods = {k: v for k, v in
                         sorted(food_dict.items(), key=lambda item: item[1], reverse=True)}
    recommended_foods_ids = list(recommended_foods.keys())[:10]
    if len(recommended_foods_ids) < 10:
        return recommended_foods_ids
    else:
        return recommended_foods_ids[:10]


def final(customer_id, restaurant_id, orders):

    if len(customer_id) != 24:
        raise ValueError("the customer id must be 24 characters long")

    if len(restaurant_id) != 24:
        raise ValueError("the restaurant id must be 24 characters long")

    restaurant_orders = filter_orders(orders, restaurant_id)
    customers_orders = {}
    for order in restaurant_orders:
        if 'userId' not in order:
            continue
        if order['userId'] not in customers_orders:
            customers_orders[order['userId']] = get_customer_food_dict(order['userId'],
                                                                       restaurant_orders)
    customers_similarities = {}
    print(customers_orders)
    if customer_id not in customers_orders:
        print('nu apare')
        return []
    for customer2_id in customers_orders:
        customers_similarities[customer2_id] = get_similarity(customers_orders[customer_id],
                                                              customers_orders[customer2_id])

    similar_customers_ordered = {k: v for k, v in
                                 sorted(customers_similarities.items(), key=lambda item: item[1], reverse=True)}
    first_similar_customers = list(similar_customers_ordered.items())[:Constants.NUMBER_OF_CUSTOMERS]
    similar_customers_foods = {}
    for customer_id in first_similar_customers:
        similar_customers_foods[customer_id[0]] = customers_orders[customer_id[0]]
    print(get_recommended_foods(similar_customers_foods, similar_customers_ordered))
    return get_recommended_foods(similar_customers_foods, similar_customers_ordered)



#http://127.0.0.1:5000/recommendations/asd/5e8b6ecd5935d8350c6c2c2a/5ea2b9ea988c7b32c419f299
# http://127.0.0.1:5000/recommendations/asd/5e9494aadd757435187a6dbd/5e8c4f351842ba322c5c13ec nu mai da lista vida 8/5/2020
# http://127.0.0.1:5000/recommendations/asd/5e9494aadd757435187a6dbd cu token:  eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJfaWQiOiI1ZThjNGYzNTE4NDJiYTMyMmM1YzEzZWMiLCJpYXQiOjE1ODgyMzc0NTZ9.pMNWm-7sQNgGM7EDQPdaSFX8a7eZSRWkzEJlD0BYMms


#token: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiX2lkIjoiNWViMTZmZGY0YWZiZjY1NDk2NmNiNjhkIn0.fUS-G5sTekJZhakqYKpoBXJ8Nc5vqrYcUPwWDO-0mL0
# ruta: http://127.0.0.1:5000/recommendations/asd/5e9494aadd757435187a6dbd