import json
import requests
from models.Restaurants import Restaurants 

class Reviews(object):
    @staticmethod
    def all(token):
        restaurants = Restaurants.all(token)
        
        all_reviews = []

        for restaunt in restaurants:

            url = 'http://159.65.247.164:3003/api/reviews' + "?providerID=" + restaunt['_id']
            headers = {"Authorization": "Bearer " + token}
            reviewsCollection = json.loads(requests.get(url, headers=headers).text)
            reviewsCollection = reviewsCollection['data']['reviews']
            
            for review in reviewsCollection:
                reviewsCollection['providerID'] = restaunt['_id']
            
            all_reviews.append(reviewsCollection)

        return all_reviews
