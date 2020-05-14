import unittest
from algorithms.search_by_restaurant import final
from models.Orders import Orders
from models.Restaurants import Restaurants
from models.Reviews import Reviews
from jwt import decode

import TestConstants
import Constants

class TestSearchByRestaurant(unittest.TestCase):

    #
    def test_recommendation_output(self):
        token = TestConstants.REST_FOOD_RECOMM_TOKEN
        decoded = decode(token, Constants.SECRET)
        customer_id = decoded['_id']
        restaurant_prefix = "Rest"
        orders = Orders.all(token)
        reviews= Reviews.by_customer_id(customer_id, token)
        restaurants = Restaurants.all(token)

        self.assertEquals({ "name_recommended_restaurant": "Recommendation starting with given prefix not found"},
        final(reviews, restaurants, orders, customer_id, restaurant_prefix, token))

    #verif corectitudine functie de decodare
    def test_decoding(self):
        token= TestConstants.SEARCH_BY_REST_TOKEN;
        customer_id = "5eb16fdf4afbf654966cb68d"
        decoded = decode(token, Constants.SECRET)
        customer_id_from_token = decoded['_id']
        self.assertEqual(customer_id,customer_id_from_token)
