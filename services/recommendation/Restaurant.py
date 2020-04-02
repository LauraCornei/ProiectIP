from flask import jsonify
from algorithms.recommendations_restaurants import final
from models.Customers import Customers
from models.Restaurant import Restaurant
from models.Reviews import Reviews

def main():
   return jsonify(final(Customers.all()[0], Reviews.all(), Customers.all(), Restaurant.all()))
