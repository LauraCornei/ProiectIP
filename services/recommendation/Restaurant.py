from algorithms.recommendations_restaurants import final
from models.Customers import Customers
from models.Restaurant import Restaurant
from models.Reviews import Reviews

def main(customer_id):
   return final(Customers.byId(customer_id), Reviews.all(), Customers.all(), Restaurant.all())
