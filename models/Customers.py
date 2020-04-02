from db import customersCollection


class Customers(object):
    @staticmethod
    def all():
        return list(customersCollection.find())
