import unittest
import TestConstants
from algorithms.restaurant_food_recommendation import final
from models.Orders import Orders

class TestRestaurantFoodRecommendation(unittest.TestCase):

    #verif ca restaurant_id si customer_id sa aiba structura unui object id (lungime 24)
    def test_raise_exception(self):
        self.assertRaises(ValueError, final, "12345", "abcdef", Orders.all("1234") )
        self.assertRaises(ValueError, final, "1234", "5eb16fdf4afbf654966cb68d", Orders.all("1234"))
        #self.assertRaises(ValueError, final, "5eb16fdf4afbf654966cb68d", "5eb16fdf4afbf654966cb68d", Orders.all("1234"))

    #verif output diferit de lista vida
    def test_recommendation_output(self):
        token = TestConstants.REST_FOOD_RECOMM_TOKEN
        orders = Orders.all(token)
        customer_id = "5eb16fdf4afbf654966cb68d"
        restaurant_id ="5e9494aadd757435187a6dbd"
        self.assertNotEquals({}, final(customer_id, restaurant_id, orders))


