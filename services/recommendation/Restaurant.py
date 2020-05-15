from algorithms.recommendations_restaurants import final
from models.Customers import Customers
from models.Restaurants import Restaurants
from models.Reviews import Reviews
import Constants


def main(customer_id, token):
    try:
        restaurants_id = final(Customers.by_id(customer_id, token), Reviews.all(token), Restaurants.all(token))
        restaurants_data = map(lambda e: Restaurants.by_id(e, token), restaurants_id)

    except Exception as error:
        answer = dict({
            Constants.SUCCESS: "false",
            Constants.ERROR: error.__str__()
        })
        return answer

    answer = dict({
        Constants.SUCCESS: "true",
        Constants.DATA: restaurants_data
    })
    return answer
