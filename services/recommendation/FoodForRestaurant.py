from algorithms.recommend_food_for_restaurants import final
from models.Restaurants import Restaurant
from models.Reviews import Reviews
from models.Foods import Foods

def main(restaurant_id):
    restaurants_id = final(Restaurants.by_id(restaurant_id), Orders.all(), Foods.all())
    restaurants_data = map(lambda e: Restaurant.by_id(e), restaurants_id)
    return restaurants_data
