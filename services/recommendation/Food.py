from algorithms.restaurant_food_recommendation import final
from models.Foods import Foods
from models.Orders import Orders
from bson import ObjectId


def recommendForRestaurant(restaurant_id, customer_id, token):
    #customer_id = ObjectId(customer_id)
    #restaurant_id = ObjectId(restaurant_id)
    foods_id = final(customer_id, restaurant_id, Orders.all(token))
    #food_data = map(lambda e: Foods.by_id(foods_id,'1223'), foods_id)
    #return food_data
    return foods_id
