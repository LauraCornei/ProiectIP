from algorithms.search_by_restaurant import final
from models.Orders import Orders
from models.Restaurants import Restaurants
from models.Reviews import Reviews

#def main():
#    return Restaurant.all()

def main(customer_id, restaurant_prefix, token):

    restaurants_data=final(Reviews.by_customer_id(customer_id, token),
                           Restaurants.all(token), Orders.all(token), customer_id, restaurant_prefix, token)
    return restaurants_data