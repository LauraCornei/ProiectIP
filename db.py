from pymongo import MongoClient
import json
import requests
client = MongoClient("mongodb+srv://test:proiectip@cluster0-cirwn.mongodb.net/test?retryWrites=true&w=majority")
db = client['proiectip']

restaurantsCollection = db['restaurants']
customersCollection = db['customers']
reviewsCollection = db['reviews']
ordersCollection = db['orders']
foodsCollection = db['foods']
ingredientsCollection = db['ingredients']


ordersCollection = json.loads(requests.get('http://159.65.247.164:3000/api/v1/orders/').text)
ordersCollection = ordersCollection['data']['orders']