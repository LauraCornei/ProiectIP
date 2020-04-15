from algorithms.recom7 import filter_res
from models.Customers import Customers
from models.Restaurants import Restaurants
from models.Reviews import Reviews
from models.Foods import Foods


def main(customer_id):
    restaurants_id = filter_res(Customers.by_id(customer_id), Reviews.all(), Foods.all())
    restaurants_data = map(lambda e: Restaurants.by_id(e), restaurants_id)
    return restaurants_data
