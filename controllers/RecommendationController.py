from services.recommendation import Food, Restaurant, FoodForRestaurant, RestaurantByFood
from flask_classful import FlaskView, route
from bson.json_util import dumps

class RecommendationController(FlaskView):
    @route('restaurant/<customer_id>')
    def restaurant(self, customer_id):
        return dumps(Restaurant.main(customer_id))

    def food(self):
        return Food.main()
       
    @route('food/<restaurant_id>')
    def food_for_restaurant(self, restaurant_id):
        return dumps(FoodForRestaurant.main(restaurant_id))

    @route('restaurant_by_food/<customer_id>')
    def restaurant_by_food(self, customer_id):
        return dumps(RestaurantByFood.main(customer_id))
