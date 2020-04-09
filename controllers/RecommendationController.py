from services.recommendation import Food, Restaurant, FoodForRestaurant, RestaurantByFood
from flask_classful import FlaskView, route
from hooks.json_response import output_json


class RecommendationController(FlaskView):
    representations = {'application/json': output_json}

    @route('restaurant/<customer_id>')
    def restaurant(self, customer_id):
        return Restaurant.main(customer_id)

    def food(self):
        return Food.main()
       
    @route('food/<restaurant_id>')
    def food_for_restaurant(self, restaurant_id):
        return FoodForRestaurant.main(restaurant_id)

    @route('restaurant_by_food/<customer_id>')
    def restaurant_by_food(self, customer_id):
        return RestaurantByFood.main(customer_id)
