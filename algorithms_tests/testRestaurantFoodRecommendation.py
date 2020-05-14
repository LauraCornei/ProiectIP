import unittest
from algorithms.restaurant_food_recommendation import final
from models.Orders import Orders
import TestConstants

class TestRestaurantFoodRecommendation(unittest.TestCase):

    def test_raise_exception(self):
        self.assertRaises(ValueError, final, "12345", "abcdef", Orders.all("1234") )
        self.assertRaises(ValueError, final, "1234", "5eb16fdf4afbf654966cb68d", Orders.all("1234"))
        #self.assertRaises(ValueError, final, "5eb16fdf4afbf654966cb68d", "5eb16fdf4afbf654966cb68d", Orders.all("1234"))

    def test_recommendation_output(self):
        token = TestConstants.REST_FOOD_RECOMM_TOKEN
        orders = Orders.all("")
        customer_id = "5eb16fdf4afbf654966cb68d"
        restaurant_id ="5e9494aadd757435187a6dbd"
        self.assertNotEquals({}, final(customer_id, restaurant_id, orders))


