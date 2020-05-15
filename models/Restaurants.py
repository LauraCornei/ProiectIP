import json
import requests
import Constants

class Restaurants(object):
    @staticmethod
    def all(token):
        url = 'http://159.65.247.164:3002/api/providers'
        headers = {"Authorization": "Bearer " + token}
        restaurantsCollection = json.loads(requests.get(url, headers=headers).text)
        restaurantsCollection = restaurantsCollection[Constants.DATA][Constants.PROVIDERS]
        return restaurantsCollection

    @staticmethod
    def by_id(id, token):
        url = 'http://159.65.247.164:3002/api/providers/' + id
        headers = {"Authorization": "Bearer " + token}
        restaurantsCollection = json.loads(requests.get(url, headers=headers).text)
        if restaurantsCollection[Constants.SUCCESS]:
            if restaurantsCollection[Constants.DATA]:
                restaurantsCollection = restaurantsCollection[Constants.DATA][Constants.PROVIDER]

        if Constants.SUCCESS in restaurantsCollection:
            if restaurantsCollection[Constants.SUCCESS] == Constants.FALSE:
                raise AttributeError("Restaurant not found")
        return restaurantsCollection
