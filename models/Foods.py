from db import foodsCollection

from bson import ObjectId

class Foods(object):
    @staticmethod
    def all(token):
        return list(foodsCollection.find())

    def by_id(id, token):
        return foodsCollection.find_one({"_id": ObjectId(id)})