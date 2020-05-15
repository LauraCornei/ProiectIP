import unittest
import algorithms_tests.TestConstants as TestConstants
import Constants
from algorithms.search_by_restaurant import final
from models.Orders import Orders
from models.Restaurants import Restaurants
from models.Reviews import Reviews
from jwt import decode

class TestSearchByRestaurant(unittest.TestCase):

    #verif corectitudine output
    def test_recommendation_output(self):
        token = TestConstants.SEARCH_BY_REST_TOKEN
        decoded = decode(token, Constants.SECRET)
        customer_id = decoded['_id']
        restaurant_prefix = "R"
        orders = Orders.all(token)
        reviews= Reviews.by_customer_id(customer_id, token)
        restaurants = Restaurants.all(token)

        print(final(reviews, restaurants, orders, customer_id, restaurant_prefix, token))
        self.assertEqual({'name_recommended_restaurant': 'Ramonita'},
        final(reviews, restaurants, orders, customer_id, restaurant_prefix, token))

        # verif corectitudine output

    def test_recommendation_output(self):
        token = TestConstants.SEARCH_BY_REST_TOKEN
        decoded = decode(token, Constants.SECRET)
        customer_id = decoded['_id']
        restaurant_prefix = "L"
        orders = Orders.all(token)
        reviews = Reviews.by_customer_id(customer_id, token)
        restaurants = Restaurants.all(token)

        self.assertEqual({'name_recommended_restaurant': 'Lauryn'},
         final(reviews, restaurants, orders, customer_id, restaurant_prefix, token))

    #verif corectitudine functie de decodare
    def test_decoding(self):
        token= TestConstants.SEARCH_BY_REST_TOKEN;
        customer_id = "5ebce91a26e32517c46effed"
        decoded = decode(token, Constants.SECRET)
        customer_id_from_token = decoded['_id']
        self.assertEqual(customer_id,customer_id_from_token)

        # http://127.0.0.1:5000/search/restaurant/R
        # restaurant_id:  5ebcf11126e32517c46effff
        # user_id:  5ebce91a26e32517c46effed
        # token: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiX2lkIjoiNWViY2U5MWEyNmUzMjUxN2M0NmVmZmVkIn0.eu0f5Vv_h8OYaslYyXKdb_2Rl8hv9FPnH3dXXEQzykQ
