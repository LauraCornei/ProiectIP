import json
import requests
from faker import Faker
# from models.Restaurants import Restaurants
import random

import json
import requests


class Restaurants(object):
    @staticmethod
    def all(token):
        url = 'http://159.65.247.164:3002/api/providers'
        headers = {"Authorization": "Bearer " + token}
        restaurantsCollection = json.loads(requests.get(url, headers=headers).text)
        restaurantsCollection = restaurantsCollection['data']['providers']
        return restaurantsCollection

    @staticmethod
    def by_id(id, token):
        url = 'http://159.65.247.164:3002/api/providers/' + id
        headers = {"Authorization": "Bearer " + token}
        restaurantsCollection = json.loads(requests.get(url, headers=headers).text)
        restaurantsCollection = restaurantsCollection['data']['provider']
        return restaurantsCollection


def create_clients():
    with open('resources/users.json') as json_file:
        users = json.load(json_file)["users"]
        url = 'http://159.65.247.164:3002/api/users/register'

        headers = {"Content-type": "application/json"}
        for user in users:
            encoder = json.JSONEncoder()
            user = encoder.encode(user)
            print(user)
            x = requests.post(url, data=user, headers=headers)
            print(x.text)


def create_providers():
    with open('resources/providers.json') as json_file:
        providers = json.load(json_file)["providers"]
        url = 'http://159.65.247.164:3002/api/users/register'
        headers = {"Content-type": "application/json"}
        for provider in providers:
            encoder = json.JSONEncoder()
            provider = encoder.encode(provider)
            print(provider)
            x = requests.post(url, data=provider, headers=headers)
            print(x.text)


def create_providers_profile():
    with open('resources/providersProfile.json') as json_file:
        profiles = json.load(json_file)["providersProfile"]

    provider_count = 0
    with open('resources/providers.json') as json_file:
        providers = json.load(json_file)["providers"]
        login_url = 'http://159.65.247.164:3002/api/users/login'
        profile_url = 'http://159.65.247.164:3002/api/users/profile'

        encoder = json.JSONEncoder()
        for provider in providers:
            login_data = {"email": provider["email"], "password": provider["password"]}
            headers = {"Content-type": "application/json"}
            login_data = encoder.encode(login_data)
            print(login_data)
            response = json.loads(requests.post(login_url, data=login_data, headers=headers).text)
            print(response["success"])
            print(response["success"] == True)
            if response["success"] == True:
                token = response["token"]
                print(token)
                headers = {"Authorization": "Bearer " + token,
                           "Content-type": "application/json"}
                data = profiles[provider_count]
                data = encoder.encode(data)
                x = requests.post(profile_url, headers=headers, data=data)
                print(x.text)
                provider_count += 1


def pick_course_from_restaurant(restaurant_id, token):
    restaurant = Restaurants.by_id(restaurant_id, token)
    restaurant_courses = restaurant['details']['menu']['courses']
    random_index = random.randint(0, len(restaurant_courses) - 1)
    return restaurant_courses[random_index]['_id']


def add_to_cart(token, restaurant_id, s):
    course_id = pick_course_from_restaurant(restaurant_id, token)
    url = 'http://159.65.247.164:3000/api/v1/cart/add-product/' + course_id
    headers = {"Authorization": "Bearer " + token}
    print("folosesc tokenul: ", token)
    print("adaug la cart ")
    print("url-ul e ", url)
    x = s.get(url, headers=headers)
    print(x.text)
    url = "http://159.65.247.164:3000/api/v1/cart/session"
    # x = s.get(url, headers=headers)
    # print("cartul are in el: ", x.text)


def get_provider_id_by_email(email, token):
    restaurants = Restaurants.all(token)
    for restaurant in restaurants:
        if restaurant['email'] == email:
            return restaurant['_id']


def create_order_for_user(user_dict, login_response, s):
    fake = Faker()
    token = login_response["token"]
    headers = {"Authorization": "Bearer " + token,
               "Content-type": "application/json"}
    while True:
        name = fake.name().split(' ')
        if len(name) >= 2:
            break
    with open('resources/providers.json') as json_file:
        providers = json.load(json_file)["providers"]
        provider_index = random.randint(0, len(providers) - 1)
        provider_email = providers[provider_index]['email']
        provider_id = get_provider_id_by_email(provider_email, token)
        nr_of_courses_in_order = random.randint(1, 3)
        order = {"userId": login_response["user"]["_id"],
                 "email": login_response["user"]["email"],
                 "userFirstName": name[0],
                 "userLastName": name[1],
                 "phoneNumber": "0748973012",
                 "paymentMethod": "cash",
                 "restaurantId": provider_id
                 }
        for i in range(nr_of_courses_in_order):
            add_to_cart(token, order['restaurantId'], s)
        url = "http://159.65.247.164:3000/api/v1/cart/session"
        x = s.get(url, headers=headers)
        print("cartul are in el: ", x.text)
        url = "http://159.65.247.164:3000/api/v1/cart"
        request_data = {
            "userId": login_response["user"]["_id"]
        }
        encoder = json.JSONEncoder()
        print("url-ul e ", url)
        print("headerurile sunt ", headers)
        print("body ul e ", encoder.encode(request_data))
        x = s.post(url, headers=headers, data=encoder.encode(request_data))
        print("in cart se afla la adaugare : ", x.text)
        url = "http://159.65.247.164:3000/api/v1/orders"
        print("encodarea de la order e ", encoder.encode(order))
        x = s.post(url, headers=headers, data=encoder.encode(order))
        print("am adaugat in orders, speram ca are items ", x.text)


def create_orders():
    with open('resources/users.json') as json_file:
        users = json.load(json_file)["users"]
        login_url = 'http://159.65.247.164:3002/api/users/login'
        encoder = json.JSONEncoder()
        for user in users:
            s = requests.Session()
            print("sunt la userul ", user)
            login_data = {"email": user["email"], "password": user["password"]}
            headers = {"Content-type": "application/json"}
            login_data = encoder.encode(login_data)
            response = json.loads(s.post(login_url, data=login_data, headers=headers).text)
            print("am primit response-ul: ", response)
            if response["success"]:
                nr_of_orders = random.randint(3, 5)
                for i in range(nr_of_orders):
                    print("creez orderul nr", i)
                    create_order_for_user(user, response, s)


print("am porit")
create_orders()
