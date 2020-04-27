from services.recommendation import Food, Restaurant, FoodForRestaurant, RestaurantByFood, Stat10
from services.stats import food_per_restaurant, food_all_restaurants
from flask_classful import FlaskView, route
from hooks.json_response import output_json
from flask import Response
from flask import request


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

    # parameters:
    # order = "asc"/"desc"
    # show_count = number of shows

    @route('stats/food_per_restaurant/<restaurant_id>')
    def food_per_restaurant(self, restaurant_id):
        show_count = -1
        if 'show_count' in request.args:
            show_count = request.args.get('show_count')
        order = "asc"
        if 'order' in request.args:
            order = request.args.get('order')
        return Response(food_per_restaurant.main(restaurant_id, order, show_count), mimetype="image/svg+xml")

    # parameters:
    # order = "asc"/"desc"
    # show_count = number of shows
    @route('stats/food_all_restaurants')
    def food_all_restaurants(self):
        show_count = -1
        if 'show_count' in request.args:
            show_count = request.args.get('show_count')
        order = "asc"
        if 'order' in request.args:
            order = request.args.get('order')
        return Response(food_all_restaurants.main(order, show_count), mimetype="image/svg+xml")