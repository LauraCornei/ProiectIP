import unittest
import TestConstants
import Constants
from algorithms.recommendations_restaurants import final
from models.Customers import Customers
from models.Restaurants import Restaurants
from models.Reviews import Reviews
from jwt import decode


class TestRestaurantRecommendations(unittest.TestCase):
    def test_recommendation_output(self):
        token= TestConstants.REST_RECOMM_TOKEN
        decoded = decode(token, Constants.SECRET)
        customer_id = decoded['_id']
        restaurant_id = final(Customers.by_id(customer_id, token), Reviews.all(token), Restaurants.all(token))
        self.assertEqual("5eb17a5b251c5187bd97251a",restaurant_id)


