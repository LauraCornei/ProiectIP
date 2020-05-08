# from db import ordersCollection
import json
import requests


class Orders(object):
    @staticmethod
    def all(token):
        url = 'http://159.65.247.164:3000/api/v1/orders/'
        headers = {"Authorization": "Bearer " + token}

        ordersCollection = json.loads(requests.get(url, headers=headers).text)
        ordersCollection = ordersCollection['data']['orders']

        orders_with_userid = []
        for order in ordersCollection:
            if 'userId' in order:
                orders_with_userid.append(order)

        return orders_with_userid
