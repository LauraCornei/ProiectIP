from flask import jsonify

from services.recommendation import Food, Restaurant
from flask_classful import FlaskView, route


class RecommendationController(FlaskView):
    @route('restaurant/<customer_id>')
    def restaurant(self, customer_id):
        return jsonify(Restaurant.main(customer_id))
    def food(self):
        return Food.main()

