from algorithms.recommendation1 import final
from models.Orders import Orders
from models.Restaurants import Restaurants
from models.Reviews import Reviews

#def main():
#    return Restaurant.all()

def main(customer_id, restaurant_prefix, token):
    restaurants_data=final(Reviews.by_customer_id('5eb16d673a637d28884dc226', 'token'),
                           Restaurants.all(token), Orders.all(token), customer_id, restaurant_prefix, token)
    print('data')
    print(restaurants_data)
    return restaurants_data