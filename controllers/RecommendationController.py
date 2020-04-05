from services.recommendation import Food, Restaurant
from flask_classful import FlaskView, route
from bson.json_util import dumps


class RecommendationController(FlaskView):
    @route('restaurant/<customer_id>')
    def restaurant(self, customer_id):
        return dumps(Restaurant.main(customer_id))

    def food(self):
        return Food.main()
