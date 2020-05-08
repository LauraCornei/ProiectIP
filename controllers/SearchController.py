from services.search import Restaurant, Food
from flask_classful import FlaskView, route
from bson.json_util import dumps
from flask import request


class SearchController(FlaskView):
    @route('restaurant/<customer_id>/<restaurant_prefix>')
    def restaurant(self, customer_id, restaurant_prefix):
        #reviewurile facute de customer_id
        token = request.headers.get('Authorization')
        return Restaurant.main(customer_id,  restaurant_prefix, token)

    def food(self):
        return Food.main()

