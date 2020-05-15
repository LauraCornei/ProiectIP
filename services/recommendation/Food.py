from algorithms.restaurant_food_recommendation import final
from models.Foods import Foods
from models.Orders import Orders
from bson import ObjectId
import Constants


def recommendForRestaurant(restaurant_id, customer_id, token):
    try:
        foods_ids = final(customer_id, restaurant_id, Orders.all(token))
        foods_data = map(lambda e: Foods.by_id(e, token), foods_ids)

    except Exception as error:
        answer = dict({
            Constants.SUCCESS: "false",
            Constants.ERROR: error.__str__()
        })
        return answer

    answer = dict({
        Constants.SUCCESS: "true",
        Constants.DATA: foods_data
    })
    return answer
