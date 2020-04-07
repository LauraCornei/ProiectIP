from db import ordersCollection

class Orders(object):
    @staticmethod
    def all():
        return list(ordersCollection.find())