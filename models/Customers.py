from db import customersCollection
from bson.objectid import ObjectId


class Customers(object):
    @staticmethod
    def all():
        return list(customersCollection.find())

    def by_id(id):
        return customersCollection.find_one({"_id": ObjectId(id)})
