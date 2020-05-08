from services.search import Restaurant, Food
from flask_classful import FlaskView, route
from bson.json_util import dumps

class SearchController(FlaskView):
    @route('restaurant/<customer_id>/<restaurant_prefix>')
    def restaurant(self, customer_id, restaurant_prefix):
        #reviewurile facute de customer_id
        token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJfaWQiOiI1ZWFhOTQ2ODMwYThmMTI5OGQ0ZmMyZjgiLCJpYXQiOjE1ODgzMjc1MDh9.PbCHEKVkf0vfq-An6Ocw98ey4KOhPER3LxPJ4hix32Q"
        return Restaurant.main(customer_id,  restaurant_prefix, token);

    def food(self):
        return Food.main()

