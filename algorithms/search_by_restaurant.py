import math
from models.Restaurants import Restaurants
from algorithms.trie import Trie
import scipy.integrate as integrate
import datetime
import Constants


def get_nb_of_orders(orders, customer_id, restaurant_id):
    nb_of_orders = 0
    for order in orders:
        if customer_id == order[Constants.USER_ID] and restaurant_id == order[Constants.RESTAURANT_ID]:
            nb_of_orders = nb_of_orders + 1
    return nb_of_orders


def get_review_score(reviews, customer_id, restaurant_id):
    score = 3
    for review in reviews:
        if customer_id == review[Constants.REVIEWER_ID] and restaurant_id == review[Constants.PROVIDER_ID]:
            score = review[Constants.SCORE]
    return score


def get_latest_order(orders, customer_id, restaurant_id):
    latest_order = math.inf
    current_date = datetime.date.today()

    for order in orders:
        order_date = datetime.datetime.strptime("2008-09-03T20:56:35.450686Z", "%Y-%m-%dT%H:%M:%S.%fZ").date()

        if customer_id == order[Constants.USER_ID] and restaurant_id == order[Constants.RESTAURANT_ID]:
            if latest_order > (current_date-order_date).days:
                latest_order = (current_date-order_date).days
    return latest_order


def integrand(x):
    return 20/math.log(x+10)


def calculate_score(review_score, nb_of_orders, latest_order):
    first_integral = integrate.quad(integrand, 0, nb_of_orders)

    word_score = (review_score/5+1.1) * first_integral[0] * 1/20 + 20 / math.log(latest_order+10)
    return word_score


def get_restaurant_name(restaurants, restaurant_id, token):
    for restaurant in restaurants:
        if restaurant_id == restaurant[Constants.ID]:
            return restaurant[Constants.NAME]


def insert_restaurant_in_trie(t, restaurants, reviews, orders, customer_id, restaurant_id, token, rest_array):
    review_score = get_review_score(reviews, customer_id, restaurant_id)
    nb_of_orders = get_nb_of_orders(orders, customer_id, restaurant_id)
    latest_order = get_latest_order(orders, customer_id, restaurant_id)
    word_score = calculate_score(review_score, nb_of_orders, latest_order)

    name = get_restaurant_name(restaurants, restaurant_id, token)
    if name:
     rest_array.append({Constants.DICT_REST_ID : restaurant_id, Constants.SCORE: word_score})


def get_recommended_restaurants_from_trie(t, restaurant_prefix):
    restaurants_array = t.special_search(restaurant_prefix)
    return restaurants_array

def update_trie(t, restaurants, reviews, orders, customer_id, token, rest_array):
    for order in orders:
        if customer_id == order[Constants.USER_ID]:
            insert_restaurant_in_trie(t, restaurants, reviews, orders, customer_id, order[Constants.RESTAURANT_ID],
                                      token, rest_array)
    return


def final(reviews, restaurants, orders, customer_id, restaurant_prefix, token):
    rest_array = []
    if len(customer_id) != Constants.OBJECT_ID_LENGTH:
        raise ValueError("the customer id must be 24 characters long")
    t = Trie()
    update_trie(t, restaurants, reviews, orders, customer_id, token, rest_array)

    rest_array = sorted(rest_array, key=lambda k: k[Constants.SCORE])
    final_result = []
    for rest in rest_array:
        name=get_restaurant_name(restaurants, rest[Constants.DICT_REST_ID], token)
        print(name)
        if name.startswith(restaurant_prefix):
            print(name)
            restaurant = Restaurants.by_id(rest[Constants.DICT_REST_ID], token)
            final_result.append(restaurant)

    if len(final_result) == 0:
        raise Exception("Recommendation starting with given prefix not found")
    return final_result


# http://127.0.0.1:5000/search/restaurant/Rest
# token: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJfaWQiOiI1ZThjNGYzNTE4NDJiYTMyMmM1YzEzZWMiLCJpYXQiOjE1ODgyMzc0NTZ9.pMNWm-7sQNgGM7EDQPdaSFX8a7eZSRWkzEJlD0BYMms

# user_Id : 5ebcf11126e32517c46effff
# nume restaurant: Ramonita
# http://127.0.0.1:5000/search/restaurant/R
# http://127.0.0.1:5000/search/restaurant/L
# token: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJfaWQiOiI1ZThjNGYzNTE4NDJiYTMyMmM1YzEzZWMiLCJpYXQiOjE1ODgyMzc0NTZ9.pMNWm-7sQNgGM7EDQPdaSFX8a7eZSRWkzEJlD0BYMms

# user_Id=5ebce91a26e32517c46effed
# http://127.0.0.1:5000/search/restaurant/R
# token: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwiX2lkIjoiNWViY2U5MWEyNmUzMjUxN2M0NmVmZmVkIiwiaWF0IjoxNTE2MjM5MDIyfQ.hoDBa28u_XYyP20B0uXAABAzdyosH1wPoRL8gJTyNhw
