import json
import requests
from models.Restaurants import Restaurants
from models.dummyReviews import dummy_reviews


class Reviews(object):
    # @staticmethod
    # def all(token):
    #     url = 'http://159.65.247.164:3003/api/reviews'
    #     headers = {"Authorization": "Bearer " + token}
    #     reviewsCollection = json.loads(requests.get(url, headers=headers).text)
    #     reviewsCollection = reviewsCollection['data']['reviews']
    #     return reviewsCollection
    @staticmethod
    def all(token):
        url = 'http://159.65.247.164:3003/api/reviews'
        headers = {"Authorization": "Bearer " + token}
        reviewsCollection = json.loads(requests.get(url, headers=headers).text)
        reviewsCollection = reviewsCollection['data']['reviews']

        return reviewsCollection

    @staticmethod
    def by_provider_id(provider_id, token):
        return dummy_reviews[provider_id]

    # selectare toare reviewurile dupa reviewerId
    def by_customer_id(customer_id, token):
        url = 'http://159.65.247.164:3003/api/reviews'
        headers = {"Authorization": "Bearer " + token}
        reviewsCollection = json.loads(requests.get(url, headers=headers).text)
        reviewsCollection = reviewsCollection['data']['reviews']

        review_by_customer_id = []
        for review in reviewsCollection:
            if (review['reviewerId'] == customer_id):
                review_by_customer_id.append(review)

        return review_by_customer_id
