from algorithms.recommend_food_for_restaurants import final
from models.Restaurants import Restaurants
from models.Reviews import Reviews
from models.Foods import Foods
from models.Orders import Orders

def main(restaurant_id):
    foods_names = final(Restaurants.by_id(restaurant_id), Orders.all(), Foods.all())
    #foods_data = map(lambda e: Foods.by_id(e), foods_id)
    return foods_names
