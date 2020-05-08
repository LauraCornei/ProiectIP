from algorithms.recommend_food_for_restaurants import final
from models.Restaurants import Restaurants
from models.Reviews import Reviews
from models.Foods import Foods
from models.Orders import Orders


def main(restaurant_id, token):
    orders = Orders.all(token)
    orders_with_userid = []
    for order in orders:
        if 'userId' in order:
            orders_with_userid.append(order)
    foods_ids = final(Restaurants.by_id(id=restaurant_id, token=token), orders_with_userid)
    foods_data = map(lambda e: Foods.by_id(e, token), foods_ids)
    return foods_data
