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
        restaurants = Restaurants.all(token)
        
        all_reviews = []

        for restaurant in restaurants:

            # url = 'http://159.65.247.164:3003/api/reviews' + "?providerID=" + restaurant['_id']
            # headers = {"Authorization": "Bearer " + token}
            # reviewsCollection = json.loads(requests.get(url, headers=headers).text)
            # reviewsCollection = reviewsCollection['data']['reviews']
            
            reviewsCollection = Reviews.by_provider_id(restaurant['_id'], token)

            for review in reviewsCollection:
                all_reviews.append(review)

        return all_reviews
    
    @staticmethod 
    def by_provider_id(provider_id, token):
        return dummy_reviews[provider_id]

