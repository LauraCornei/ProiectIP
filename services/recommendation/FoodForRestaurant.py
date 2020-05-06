from algorithms.recommend_food_for_restaurants import final
from models.Restaurants import Restaurants
from models.Reviews import Reviews
from models.Foods import Foods
from models.Orders import Orders


def main(restaurant_id):
    token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJfaWQiOiI1ZWFhOTQ2ODMwYThmMTI5OGQ0ZmMyZjgiLCJpYXQiOjE1ODgzMjc1MDh9.PbCHEKVkf0vfq-An6Ocw98ey4KOhPER3LxPJ4hix32Q"
    print(Restaurants.by_id(id=restaurant_id, token=token))
    print(Orders.all(token))
    foods_names = final(Restaurants.by_id(id=restaurant_id, token=token), Orders.all(token), Foods.all(token))
    # foods_data = map(lambda e: Foods.by_id(e), foods_id)
    return foods_names
