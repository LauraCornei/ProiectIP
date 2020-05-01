import json
import requests

class Reviews(object):
    @staticmethod
    def all(token):
        url = 'http://159.65.247.164:3003/api/reviews'
        headers = {"Authorization": "Bearer " + token}
        reviewsCollection = json.loads(requests.get(url, headers=headers).text)
        reviewsCollection = reviewsCollection['data']['reviews']
        return reviewsCollection
