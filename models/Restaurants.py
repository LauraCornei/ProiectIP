from db import restaurantsCollection

from bson import ObjectId


class Restaurants(object):
    @staticmethod
    def all():
        return list(restaurantsCollection.find())

    def by_id(id):
        return restaurantsCollection.find_one({"_id": ObjectId(id)})
