from algorithms.recommendation1 import final
from models.Orders import Orders
from models.Restaurants import Restaurants
from models.Reviews import Reviews
#def main():
#    return Restaurant.all()

def main(customer_id, restaurant_prefix):
    restaurants_data=final(Reviews.all(), Restaurants.all(), Orders.all(), customer_id, restaurant_prefix)
    print('data')
    print(restaurants_data)
    return restaurants_data