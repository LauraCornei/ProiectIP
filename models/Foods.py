from db import foodsCollection

class Foods(object):
    @staticmethod
    def all():
        return list(foodsCollection.find())