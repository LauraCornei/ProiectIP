from db import reviewsCollection


class Reviews(object):
    @staticmethod
    def all():
        return list(reviewsCollection.find())
