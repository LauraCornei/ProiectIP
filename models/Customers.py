import json
import requests
import Constants


class Customers(object):
    @staticmethod
    def all(token):
        url = Constants.URL_USERS
        headers = {"Authorization": "Bearer " + token}
        customersCollection = json.loads(requests.get(url, headers=headers).text)
        customersCollection = customersCollection[Constants.DATA][Constants.USERS]
        return customersCollection

    def by_id(id, token):
        url = Constants.URL_USERS + '/' + id
        headers = {"Authorization": "Bearer " + token}
        customersCollection = json.loads(requests.get(url, headers=headers).text)
        customersCollection = customersCollection[Constants.DATA][Constants.USER]
        print("ASJDOISAJDOISJAIOUDHASIUHDGIUSAHIDUHAS")
        print(customersCollection)
        return customersCollection
