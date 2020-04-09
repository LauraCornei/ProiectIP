from db import foodsCollection

from bson import ObjectId

class Foods(object):
    @staticmethod
    def all():
        return list(foodsCollection.find())
        
        
    def by_id(id):
        return foodsCollection.find_one({"_id": ObjectId(id)})