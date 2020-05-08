from services.search import Restaurant, Food
from flask_classful import FlaskView, route
from bson.json_util import dumps
from flask import request
from jwt import decode

class SearchController(FlaskView):
    secret = 'agfbkgfdakjhabagdf'

    @route('restaurant/<restaurant_prefix>')
    def restaurant(self, restaurant_prefix):
        token = request.headers.get('Authorization')
        decoded = decode(token.split(' ')[1], self.secret)
        customer_id = decoded['_id']
        return Restaurant.main(customer_id,  restaurant_prefix, token)

    def food(self):
        return Food.main()

