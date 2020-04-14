from pymongo import MongoClient
client = MongoClient("mongodb+srv://test:proiectip@cluster0-cirwn.mongodb.net/test?retryWrites=true&w=majority")
db = client['proiectip']

restaurantsCollection = db['restaurants']
customersCollection = db['customers']
reviewsCollection = db['reviews']
ordersCollection = db['orders']
foodsCollection = db['foods']
ingredientsCollection = db['ingredients']