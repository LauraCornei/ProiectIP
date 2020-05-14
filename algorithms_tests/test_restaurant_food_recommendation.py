import unittest
from algorithms.restaurant_food_recommendation import final
from models.Orders import Orders

class TestRestaurantFoodRecommendation(unittest.TestCase):
    def test_recommendation(self):
        self.assertRaises(ValueError, final, "12345", "abcdef", Orders.all('1234') )