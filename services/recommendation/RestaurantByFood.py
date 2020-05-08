from algorithms.recom7 import filter_res
from models.Customers import Customers
from models.Restaurants import Restaurants
from models.Reviews import Reviews
from models.Foods import Foods

# http://127.0.0.1:5000/recommendations/restaurant_by_food/5eb16fdf4afbf654966cb68d
# eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJfaWQiOiI1ZTk4YTIzNzk3YWVhMTM5YzJiOTk1OTIiLCJpYXQiOjE1ODgyNTgxMTZ9.1GCgbuMH_Pi9kNtIR7QTqrH7EIcW86rbjU_Fe1HYSVk
# Bearer Token(Authorization)


def main(customer_id, token):
    x = Customers.by_id(customer_id, token)
    if x is None:
        return "This customer ain't around!"

    restaurants_id = filter_res(Customers.by_id(customer_id, token), Reviews.all(token), token)
    print( restaurants_id )
    return restaurants_id
