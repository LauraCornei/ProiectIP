from services.recommendation import Food, Restaurant, FoodForRestaurant, RestaurantByFood, Stat10
from flask_classful import FlaskView, route
from hooks.json_response import output_json
from flask import Response


class RecommendationController(FlaskView):
    representations = {'application/json': output_json}

    @route('restaurant/<customer_id>')
    def restaurant(self, customer_id):
        return Restaurant.main(customer_id)

    @route('asd/<restaurant_id>/<customer_id>')
    def food(self, restaurant_id, customer_id):
        return Food.recommendForRestaurant(restaurant_id, customer_id)

    # recomanda mancaruri pt un restaurant
    @route('food/<restaurant_id>')
    def food_for_restaurant(self, restaurant_id):
        return FoodForRestaurant.main(restaurant_id)

    # ??? todo add comment
    @route('restaurant_by_food/<customer_id>')
    def restaurant_by_food(self, customer_id):
        return RestaurantByFood.main(customer_id)

    @route('stats/customers_per_hours')
    def plot_svg(self):
        return Response(Stat10.main(), mimetype="image/svg+xml")
