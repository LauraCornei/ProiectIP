from algorithms.recommendations_restaurants import final
from models.Customers import Customers
from models.Restaurants import Restaurants
from models.Reviews import Reviews
from models.Orders import Orders

def main(customer_id, token):
    restaurants_id = final(Customers.by_id(customer_id, token), Reviews.all(), Restaurants.all())
    restaurants_data = map(lambda e: Restaurants.by_id(e, token), restaurants_id)
    return restaurants_data
