import json
import requests
from faker import Faker

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


def create_orders():
    fake = Faker()
    with open('resources/users.json') as json_file:
        users = json.load(json_file)["users"]
        login_url = 'http://159.65.247.164:3002/api/users/login'
        profile_url = 'http://159.65.247.164:3002/api/users/profile'

        encoder = json.JSONEncoder()
        for user in users:
            login_data = {"email": user["email"], "password": user["password"]}
            headers = {"Content-type": "application/json"}
            login_data = encoder.encode(login_data)
            response = json.loads(requests.post(login_url, data=login_data, headers=headers).text)
            if response["success"]:
                token = response["token"]
                headers = {"Authorization": "Bearer " + token,
                           "Content-type": "application/json"}

                while True:
                    name = fake.name().split(' ')
                    if len(name) >= 2:
                        break

                foodOrder = get_random_food_order()

                order = {"userId": response["user"]["_id"],
                         "email": response["user"]["email"],
                         "userFirstName": name[0],
                         "userLastName": name[1],
                         "phoneNumber": "0748973012",
                         "restaurantId": "a"
                         }

                order = encoder.encode(order)
                x = requests.post(profile_url, headers=headers, data=order)
                print(x.text)


def get_random_food_order():


create_providers_profile()