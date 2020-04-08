from algorithms.recommendation1 import final
from models.Orders import Orders
from models.Restaurants import Restaurant
from models.Reviews import Reviews
#def main():
#    return Restaurant.all()

def main(customer_id, restaurant_prefix):
    restaurants_data=final(Reviews.all(), Restaurant.all(), Orders.all(), customer_id, restaurant_prefix)
    #restaurants_id = final(Customers.by_id(customer_id), Reviews.all(), Restaurant.all())
    #restaurants_data = map(lambda e: Restaurant.by_id(e), restaurants_id)
    return restaurants_data