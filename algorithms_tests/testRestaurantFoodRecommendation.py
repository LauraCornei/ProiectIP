import unittest
import TestConstants
import Constants
from algorithms.restaurant_food_recommendation import final
from models.Orders import Orders
from jwt import decode

class TestRestaurantFoodRecommendation(unittest.TestCase):

    #verif ca restaurant_id si customer_id sa aiba structura unui object id (lungime 24)
    def test_raise_exception(self):
        self.assertRaises(ValueError, final, "12345", "abcdef", Orders.all("1234") )
        self.assertRaises(ValueError, final, "1234", "5eb16fdf4afbf654966cb68d", Orders.all("1234"))
        #self.assertRaises(ValueError, final, "5eb16fdf4afbf654966cb68d", "5eb16fdf4afbf654966cb68d", Orders.all("1234"))

    # verif output diferit de lista vida
    def test_recommendation_output(self):
        token = TestConstants.SEARCH_BY_REST_TOKEN
        orders = Orders.all(token)
        decoded = decode(token, Constants.SECRET)
        customer_id = decoded['_id']
        restaurant_id = "5ebcf11126e32517c46effff"
        self.assertNotEquals({}, final(customer_id, restaurant_id, orders))

    #verif output diferit de lista vida
    def test_recommendation_output(self):
        token = TestConstants.SEARCH_BY_REST_TOKEN
        orders = Orders.all(token)
        customer_id = "5eb16fdf4afbf654966cb68d"
        restaurant_id ="5e9494aadd757435187a6dbd"
        self.assertNotEquals({}, final(customer_id, restaurant_id, orders))


#http://127.0.0.1:5000/recommendations/food-for-restaurant/5ebcf11126e32517c46effff
#eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiX2lkIjoiNWViY2U5MWEyNmUzMjUxN2M0NmVmZmVkIn0.eu0f5Vv_h8OYaslYyXKdb_2Rl8hv9FPnH3dXXEQzykQ
