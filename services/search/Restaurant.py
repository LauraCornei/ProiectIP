from algorithms.search_by_restaurant import final
from models.Orders import Orders
from models.Restaurants import Restaurants
from models.Reviews import Reviews
import Constants

# def main():
#    return Restaurant.all()


def main(customer_id, restaurant_prefix, token):

    try:
        restaurants_data = final(Reviews.by_customer_id(customer_id, token),
                                 Restaurants.all(token), Orders.all(token), customer_id, restaurant_prefix, token)
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
