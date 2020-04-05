from algorithms.recommendations_restaurants import final
from models.Customers import Customers
from models.Restaurant import Restaurant
from models.Reviews import Reviews


def main(customer_id):
    restaurants_id = final(Customers.by_id(customer_id), Reviews.all(), Restaurant.all())
    restaurants_data = map(lambda e: Restaurant.by_id(e), restaurants_id)
    return restaurants_data
