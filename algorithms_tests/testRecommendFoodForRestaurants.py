import unittest
import TestConstants
from algorithms.recommend_food_for_restaurants import final
from models.Restaurants import Restaurants
from models.Foods import Foods
from models.Orders import Orders

class TestRestaurantFoodRecommendation(unittest.TestCase):

    #verif ca restaurant_id si customer_id sa aiba structura unui object id (lungime 24)
    def test_raise_exception(self):
        self.assertRaises(ValueError, final, "12345", "abcdef", Orders.all("1234") )
        self.assertRaises(ValueError, final, "1234", "5eb16fdf4afbf654966cb68d", Orders.all("1234"))
        #self.assertRaises(ValueError, final, "5eb16fdf4afbf654966cb68d", "5eb16fdf4afbf654966cb68d", Orders.all("1234"))

    #verif output
    def test_recommendation_output(self):
        token = TestConstants.REST_FOOD_FOR_REST_TOKEN
        orders = Orders.all(token)
        restaurant_id ="5e9494aadd757435187a6dbd"
        self.assertNotEquals({}, final(restaurant_id, orders))


