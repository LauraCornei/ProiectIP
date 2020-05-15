from services.recommendation import Food, Restaurant, FoodForRestaurant, RestaurantByFood, NumberOfOrdersPerHour
from services.stats import food_per_restaurant, food_all_restaurants
from flask_classful import FlaskView, route
from hooks.json_response import output_json
from flask import Response
from flask import request
from jwt import decode
from Constants import AUTHORIZATION, SECRET, TOKEN


class RecommendationController(FlaskView):
    representations = {'application/json': output_json}

    def get_customer_id(self, token):
        decoded = decode(token.split(' ')[1], SECRET)
        return decoded['_id']

    @route('restaurant')
    def restaurant(self):
        token = request.headers.get(AUTHORIZATION)
        return Restaurant.main(self.get_customer_id(token), token)

    @route('food-for-restaurant/<restaurant_id>')
    def food(self, restaurant_id):
        token = request.headers.get(AUTHORIZATION)
        return Food.recommendForRestaurant(restaurant_id, self.get_customer_id(token), token)

    # recomanda mancaruri pt un restaurant
    @route('food/<restaurant_id>')
    def food_for_restaurant(self, restaurant_id):
        token = request.headers.get(AUTHORIZATION)
        return FoodForRestaurant.main(restaurant_id, token)

    # recomanda <=10 restaurante care au specialitati asemanatoare
    # cu cele ale restaurantul fav de clientul din input
    @route('restaurant-by-food')
    def restaurant_by_food(self):
        token = request.headers.get(AUTHORIZATION)
        return RestaurantByFood.main(self.get_customer_id(token), token)

    @route('stats/orders-per-hour/<restaurant_id>')
    def orders_per_hour_per_restaurant(self, restaurant_id):
        token = request.args.get(TOKEN)
        return Response(NumberOfOrdersPerHour.number_of_orders_by_restaurant(restaurant_id, token),
                        mimetype="image/svg+xml")

    @route('stats/orders-per-hour')
    def orders_per_hour(self):
        token = request.args.get(TOKEN)
        return Response(NumberOfOrdersPerHour.number_of_orders(token), mimetype="image/svg+xml")

    # parameters:
    # order = "asc"/"desc"
    # show_count = number of shows
    @route('stats/food-per-restaurant/<restaurant_id>')
    def food_per_restaurant(self, restaurant_id):
        token = request.args.get(TOKEN)
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
    @route('stats/food-all-restaurants')
    def food_all_restaurants(self):
        token = request.args.get(TOKEN)
        show_count = -1
        if 'show_count' in request.args:
            show_count = request.args.get('show_count')
        order = "asc"
        if 'order' in request.args:
            order = request.args.get('order')
        return Response(food_all_restaurants.main(order, show_count, token), mimetype="image/svg+xml")