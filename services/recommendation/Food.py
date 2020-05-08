from algorithms.restaurant_food_recommendation import final
from models.Foods import Foods
from models.Orders import Orders
from bson import ObjectId


def recommendForRestaurant(restaurant_id, customer_id, token):
    foods_ids = final(customer_id, restaurant_id, Orders.all(token))
    foods_data = map(lambda e: Foods.by_id(e, token), foods_ids)
    return foods_data
