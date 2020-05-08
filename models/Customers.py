from bson.objectid import ObjectId
import json
import requests


class Customers(object):
    @staticmethod
    def all(token):
        url = 'http://159.65.247.164:3002/api/clients'
        headers = {"Authorization": "Bearer " + token}
        customersCollection = json.loads(requests.get(url, headers=headers).text)
        customersCollection = customersCollection['data']['clients']
        return customersCollection

    @staticmethod
    def by_id(id, token):
        url = 'http://159.65.247.164:3002/api/clients/' + id
        headers = {"Authorization": "Bearer " + token}
        customersCollection = json.loads(requests.get(url, headers=headers).text)
        customersCollection = customersCollection['data']['client']
        return customersCollection
