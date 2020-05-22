# from db import ordersCollection
import json
import requests
import Constants


class Orders(object):
    @staticmethod
    def all(token):
        url = Constants.URL_ORDERS
        headers = {"Authorization": "Bearer " + token}

        ordersCollection = json.loads(requests.get(url, headers=headers).text)
        ordersCollection = ordersCollection[Constants.DATA][Constants.ORDERS]

        orders_with_userid = []
        for order in ordersCollection:
            if Constants.USER_ID in order:
                orders_with_userid.append(order)

        return orders_with_userid

    @staticmethod
    def by_res_id(id, token):

        url = 'http://159.65.247.164:3000/api/v1/orders/'
        headers = {"Authorization": "Bearer " + token}

        orders_collection = json.loads(requests.get(url, headers=headers).text)
        orders_collection = orders_collection[Constants.DATA][Constants.ORDERS]

        orders_with_userid = []
        for order in orders_collection:
            if Constants.USER_ID in order:
                orders_with_userid.append(order)

        ans = []
        for order in orders_with_userid:
            if order[Constants.RESTAURANT_ID] == id:
                ans.append(order)
        return ans
