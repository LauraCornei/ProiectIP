from services.recommendation import Food, Restaurant, FoodForRestaurant, RestaurantByFood, NumberOfOrdersPerHour
from services.stats import food_per_restaurant, food_all_restaurants
from flask_classful import FlaskView, route
from hooks.json_response import output_json
from flask import Response
from flask import request


class RecommendationController(FlaskView):
    representations = {'application/json': output_json}

    @route('restaurant/<customer_id>')
    def restaurant(self, customer_id):
        token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJfaWQiOiI1ZWFhOTQ2ODMwYThmMTI5OGQ0ZmMyZjgiLCJpYXQiOjE1ODgzMjc1MDh9.PbCHEKVkf0vfq-An6Ocw98ey4KOhPER3LxPJ4hix32Q"
        return Restaurant.main(customer_id, token)

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

    @route('stats/orders_per_hour/<restaurant_id>')
    def orders_per_hour_per_restaurant(self, restaurant_id):
        token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJfaWQiOiI1ZWFhOTQ2ODMwYThmMTI5OGQ0ZmMyZjgiLCJpYXQiOjE1ODgzMjc1MDh9.PbCHEKVkf0vfq-An6Ocw98ey4KOhPER3LxPJ4hix32Q"

        return Response(NumberOfOrdersPerHour.number_of_orders_by_restaurant(restaurant_id, token),
                        mimetype="image/svg+xml")

    @route('stats/orders_per_hour')
    def orders_per_hour(self):
        token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJfaWQiOiI1ZWFhOTQ2ODMwYThmMTI5OGQ0ZmMyZjgiLCJpYXQiOjE1ODgzMjc1MDh9.PbCHEKVkf0vfq-An6Ocw98ey4KOhPER3LxPJ4hix32Q"

        return Response(NumberOfOrdersPerHour.number_of_orders(token), mimetype="image/svg+xml")



    # parameters:
    # order = "asc"/"desc"
    # show_count = number of shows
    @route('stats/food_per_restaurant/<restaurant_id>')
    def food_per_restaurant(self, restaurant_id):
        token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJfaWQiOiI1ZWFhOTQ2ODMwYThmMTI5OGQ0ZmMyZjgiLCJpYXQiOjE1ODgzMjc1MDh9.PbCHEKVkf0vfq-An6Ocw98ey4KOhPER3LxPJ4hix32Q"
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
        token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJfaWQiOiI1ZWFhOTQ2ODMwYThmMTI5OGQ0ZmMyZjgiLCJpYXQiOjE1ODgzMjc1MDh9.PbCHEKVkf0vfq-An6Ocw98ey4KOhPER3LxPJ4hix32Q"
        show_count = -1
        if 'show_count' in request.args:
            show_count = request.args.get('show_count')
        order = "asc"
        if 'order' in request.args:
            order = request.args.get('order')
        return Response(food_all_restaurants.main(order, show_count, token), mimetype="image/svg+xml")