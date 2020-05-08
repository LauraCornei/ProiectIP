import math

from bson import ObjectId
from models.Restaurants import Restaurants
from algorithms.trie import Trie
import scipy.integrate as integrate
import datetime
from pymongo import MongoClient
from bson import ObjectId

def get_nb_of_orders(orders, customer_id, restaurant_id):
    nb_of_orders =0
    for order in orders:
        if customer_id == order["userId"] and restaurant_id == order["restaurantId"]:
            nb_of_orders=nb_of_orders +1
    return nb_of_orders

def get_review_score(reviews, customer_id, restaurant_id):
    score = 3
    for review in reviews:
      if customer_id == review["userId"] and restaurant_id == review["restaurantId"]:
         score= review["score"]
    return score

def get_latest_order(orders, customer_id, restaurant_id):
    latest_order=math.inf
    current_date=datetime.date.today()
    for order in orders:

        print(order["orderDate"])
        order_date= datetime.datetime.strptime("2008-09-03T20:56:35.450686Z", "%Y-%m-%dT%H:%M:%S.%fZ").date()

        if customer_id == order["userId"] and restaurant_id == order["restaurantId"]:
            if(latest_order> (current_date-order_date).days):
                latest_order=(current_date-order_date).days
    return latest_order


def integrand(x):
    return (20/math.log(x+10))


def calculate_score (review_score, nb_of_orders, latest_order):
    first_integral = integrate.quad(integrand , 0, nb_of_orders)

    word_score = (review_score/5+1.1) *first_integral[0] *1/20+ 20 / math.log(latest_order+10)
    return word_score



def get_restaurant_name(restaurants, restaurant_id, token):
    print('aaaa')
    print(restaurant_id)
    restaurant= Restaurants.by_id( restaurant_id, token)
    #print(restaurant["name"])
    #print(restaurant_id)

    for restaurant in restaurants:
        if restaurant_id == restaurant["_id"]:
            return restaurant["name"]


def insert_restaurant_in_trie(t, restaurants, reviews, orders, customer_id, restaurant_id, token):
    print('bbbb')
    review_score = get_review_score(reviews, customer_id, restaurant_id)
    nb_of_orders = get_nb_of_orders(orders, customer_id, restaurant_id)
    latest_order = get_latest_order(orders, customer_id, restaurant_id)
    word_score = calculate_score(review_score, nb_of_orders, latest_order)
    name = get_restaurant_name(restaurants, restaurant_id, token)
    print(name)
    if name:
       t.insert(name, word_score, restaurant_id)
    return

def get_recommended_restaurant_from_trie(t, restaurant_prefix):
    recommended_restaurant_id=t.special_search(restaurant_prefix)
    if recommended_restaurant_id == False:
        return False
    return recommended_restaurant_id["restaurantId"]

def update_trie(t, restaurants , reviews, orders, customer_id, token):
   print(customer_id)

   for order in orders:
        if customer_id == order["userId"]:
            insert_restaurant_in_trie(t, restaurants, reviews, orders, customer_id, order["restaurantId"],  token)
   return


def final(reviews, restaurants, orders, customer_id, restaurant_prefix, token):
    '''print(reviews)
    print('*')
    print(restaurants)
    print('*')
    print(orders)
    print('*')'''

    #http://127.0.0.1:5000/search/restaurant/5e8c4f351842ba322c5c13ec/Rest

    t = Trie()
    update_trie(t, restaurants, reviews, orders, customer_id, token)
    restaurant_id = get_recommended_restaurant_from_trie(t, restaurant_prefix)

    if restaurant_id == False:
        value = "Recommendation starting with given prefix not found"
    else:
        value = get_restaurant_name(restaurants, restaurant_id, token)
    recommendations = {
        "name_recommended_restaurant": value
    }
    return recommendations



