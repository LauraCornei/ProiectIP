from services.search import Restaurant, Food
from flask_classful import FlaskView, route
from bson.json_util import dumps

class SearchController(FlaskView):
    @route('restaurant/<customer_id>/<restaurant_prefix>')
    def restaurant(self, customer_id, restaurant_prefix):
        #print(Restaurant.main(customer_id,  restaurant_prefix))
        return dumps(Restaurant.main(customer_id,  restaurant_prefix))

    def food(self):
        return Food.main()

