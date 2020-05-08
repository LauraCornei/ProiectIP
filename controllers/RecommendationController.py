from services.recommendation import Food, Restaurant, FoodForRestaurant, RestaurantByFood, NumberOfOrdersPerHour
from services.stats import food_per_restaurant, food_all_restaurants
from flask_classful import FlaskView, route
from hooks.json_response import output_json
from flask import Response
from flask import request
from jwt import decode


class RecommendationController(FlaskView):
    representations = {'application/json': output_json}
    secret = 'agfbkgfdakjhabagdf'

    @route('restaurant')
    def restaurant(self):
        token = request.headers.get('Authorization')
        decoded = decode(token, self.secret)
        customer_id = decoded['_id']
        return Restaurant.main(customer_id, token)

    @route('asd/<restaurant_id>')
    def food(self, restaurant_id):
        token = request.headers.get('Authorization')
        decoded = decode(token, self.secret)
        customer_id = decoded['_id']
        return Food.recommendForRestaurant(restaurant_id, customer_id, token)

    # recomanda mancaruri pt un restaurant
    @route('food/<restaurant_id>')
    def food_for_restaurant(self, restaurant_id):
        token = request.headers.get('Authorization')
        return FoodForRestaurant.main(restaurant_id, token)

    # recomanda <=10 restaurante care au specialitati asemanatoare
    # cu cele ale restaurantul fav de clientul din input
    @route('restaurant_by_food')
    def restaurant_by_food(self):
        token = request.headers.get('Authorization')
        decoded = decode(token, self.secret)
        customer_id = decoded['_id']
        return RestaurantByFood.main(customer_id, token)

    @route('stats/orders_per_hour/<restaurant_id>')
    def orders_per_hour_per_restaurant(self, restaurant_id):
        token = request.args.get("token")
        return Response(NumberOfOrdersPerHour.number_of_orders_by_restaurant(restaurant_id, token),
                        mimetype="image/svg+xml")

    @route('stats/orders_per_hour')
    def orders_per_hour(self):
        token = request.args.get("token")
        return Response(NumberOfOrdersPerHour.number_of_orders(token), mimetype="image/svg+xml")


    # parameters:
    # order = "asc"/"desc"
    # show_count = number of shows
    @route('stats/food_per_restaurant/<restaurant_id>')
    def food_per_restaurant(self, restaurant_id):
        token = request.args.get("token")
        show_count = -1
        if 'show_count' in request.args:
            show_count = request.args.get('show_count')
        order = "asc"
        if 'order' in request.args:
            order = request.args.get('order')
        return Response(food_per_restaurant.main(restaurant_id, order, show_count, token), mimetype="image/svg+xml")

    # parameters:
    # order = "asc"/"desc"
    # show_count = number of shows
    @route('stats/food_all_restaurants')
    def food_all_restaurants(self):
        token = request.args.get("token")
        show_count = -1
        if 'show_count' in request.args:
            show_count = request.args.get('show_count')
        order = "asc"
        if 'order' in request.args:
            order = request.args.get('order')
        return Response(food_all_restaurants.main(order, show_count, token), mimetype="image/svg+xml")