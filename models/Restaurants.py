from bson import ObjectId
import json
import requests

class Restaurants(object):
    @staticmethod
    def all(token):
        url = 'http://159.65.247.164:3002/api/users'
        headers = {"Authorization": "Bearer " + token}
        restaurantsCollection = json.loads(requests.get(url, headers=headers).text)
        restaurantsCollection = restaurantsCollection['data']['users']
        return restaurantsCollection

    def by_id(id, token):
        url = 'http://159.65.247.164:3002/api/users' + id
        headers = {"Authorization": "Bearer " + token}
        restaurantsCollection = json.loads(requests.get(url, headers=headers).text)
        restaurantsCollection = restaurantsCollection['data']['user']
        return restaurantsCollection
