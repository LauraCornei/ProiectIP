from bson.objectid import ObjectId
import json
import requests


class Customers(object):
    @staticmethod
    def all(token):
        url = 'http://159.65.247.164:3002/api/users'
        headers = {"Authorization": "Bearer " + token}
        customersCollection = json.loads(requests.get(url, headers=headers).text)
        customersCollection = customersCollection['data']['users']
        return customersCollection

    def by_id(id, token):
        url = 'http://159.65.247.164:3002/api/users/' + id
        headers = {"Authorization": "Bearer " + token}
        customersCollection = json.loads(requests.get(url, headers=headers).text)
        customersCollection = customersCollection['data']['user']

        return customersCollection
