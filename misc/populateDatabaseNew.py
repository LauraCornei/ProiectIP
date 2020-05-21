import json
import requests
from faker import Faker
import random
import Constants

import json
import requests


def create_clients():
    with open('resources/users.json') as json_file:
        users = json.load(json_file)[Constants.USERS]
        url = Constants.URL_REGISTER

        headers = {"Content-type": "application/json"}
        for user in users:
            encoder = json.JSONEncoder()
            user = encoder.encode(user)
            print(user)
            x = requests.post(url, data=user, headers=headers)
            print(x.text)


def create_providers():
    with open('resources/providers.json') as json_file:
        providers = json.load(json_file)[Constants.URL_PROVIDERS]
        url = Constants.URL_REGISTER
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
        providers = json.load(json_file)[Constants.PROVIDERS]
        login_url = Constants.URL_LOGIN
        profile_url = Constants.URL_PROFILE

        encoder = json.JSONEncoder()
        for provider in providers:
            login_data = {"email": provider["email"], "password": provider["password"]}
            headers = {"Content-type": "application/json"}
            login_data = encoder.encode(login_data)
            print(login_data)
            response = json.loads(requests.post(login_url, data=login_data, headers=headers).text)
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
    restaurant_courses = restaurant[Constants.DETAILS][Constants.MENU][Constants.COURSES]
    random_index = random.randint(0, len(restaurant_courses) - 1)
    return restaurant_courses[random_index][Constants.ID]


def add_to_cart(token, restaurant_id, s):
    course_id = pick_course_from_restaurant(restaurant_id, token)
    url = Constants.URL_ADD_PRODUCT + course_id
    headers = {"Authorization": "Bearer " + token}
    x = s.get(url, headers=headers)


def get_provider_id_by_email(email, token):
    restaurants = Restaurants.all(token)
    for restaurant in restaurants:
        if restaurant[Constants.EMAIL] == email:
            return restaurant[Constants.ID]


def create_order_for_user(login_response, s):
    fake = Faker()
    token = login_response[Constants.TOKEN]
    headers = {"Authorization": "Bearer " + token,
               "Content-type": "application/json"}
    while True:
        name = fake.name().split(' ')
        if len(name) >= 2:
            break
    with open('resources/providers.json') as json_file:
        providers = json.load(json_file)[Constants.PROVIDERS]
        provider_index = random.randint(0, len(providers) - 1)
        provider_email = providers[provider_index][Constants.EMAIL]
        provider_id = get_provider_id_by_email(provider_email, token)
        nr_of_courses_in_order = random.randint(1, 3)
        order = {Constants.USER_ID: login_response[Constants.USER][Constants.ID],
                 Constants.EMAIL: login_response[Constants.USER][Constants.EMAIL],
                 "userFirstName": name[0],
                 "userLastName": name[1],
                 "phoneNumber": "0748973012",
                 "paymentMethod": "cash",
                 Constants.RESTAURANT_ID: provider_id
                 }
        for i in range(nr_of_courses_in_order):
            add_to_cart(token, order[Constants.RESTAURANT_ID], s)
        url = Constants.URL_CART_SESSION
        x = s.get(url, headers=headers)
        print("cartul are in el: ", x.text)
        url = Constants.URL_CART
        request_data = {
            Constants.USER_ID: login_response[Constants.USER][Constants.ID]
        }
        encoder = json.JSONEncoder()
        x = s.post(url, headers=headers, data=encoder.encode(request_data))
        url = Constants.URL_ORDERS
        x = s.post(url, headers=headers, data=encoder.encode(order))


def create_orders():
    with open('resources/users.json') as json_file:
        users = json.load(json_file)[Constants.USERS]
        login_url = Constants.URL_LOGIN
        encoder = json.JSONEncoder()
        for user in users:
            s = requests.Session()
            login_data = {Constants.EMAIL: user[Constants.EMAIL], "password": user["password"]}
            headers = {"Content-type": "application/json"}
            login_data = encoder.encode(login_data)
            response = json.loads(s.post(login_url, data=login_data, headers=headers).text)
            if response[Constants.SUCCESS]:
                nr_of_orders = random.randint(3, 5)
                for i in range(nr_of_orders):
                    create_order_for_user(response, s)


class Restaurants(object):
    @staticmethod
    def all(token):
        url = Constants.URL_PROVIDERS
        headers = {"Authorization": "Bearer " + token}
        restaurantsCollection = json.loads(requests.get(url, headers=headers).text)
        restaurantsCollection = restaurantsCollection[Constants.DATA][Constants.PROVIDERS]
        return restaurantsCollection

    @staticmethod
    def by_id(id, token):
        url = Constants.URL_PROVIDERS + '/' + id
        headers = {"Authorization": "Bearer " + token}
        restaurantsCollection = json.loads(requests.get(url, headers=headers).text)
        restaurantsCollection = restaurantsCollection[Constants.DATA][Constants.PROVIDER]
        return restaurantsCollection


create_orders()
