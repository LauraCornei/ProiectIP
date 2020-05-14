from bson import ObjectId
import json
import requests


class Restaurants(object):
    @staticmethod
    def all(token):
        url = 'http://159.65.247.164:3002/api/providers'
        headers = {"Authorization": "Bearer " + token}
        restaurantsCollection = json.loads(requests.get(url, headers=headers).text)
        restaurantsCollection = restaurantsCollection["data"]["provider"]
        return restaurantsCollection

    @staticmethod
    def by_id(id, token):
        url = 'http://159.65.247.164:3002/api/providers/' + id
        headers = {"Authorization": "Bearer " + token}
        restaurantsCollection = json.loads(requests.get(url, headers=headers).text)
        if(restaurantsCollection["success"]):
          print(restaurantsCollection["data"])
          if(restaurantsCollection["data"]):
             restaurantsCollection = restaurantsCollection["data"]["provider"]
        return restaurantsCollection
