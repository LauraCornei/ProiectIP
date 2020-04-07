from pymongo import MongoClient
import json
import clearDataBase
import random as rnd

RANDOM_SEED = 324324;
rnd.seed(RANDOM_SEED)
client = MongoClient("mongodb+srv://test:proiectip@cluster0-cirwn.mongodb.net/test?retryWrites=true&w=majority")
db = client['proiectip']


# shuffle first k elements of the array with any other elements
def fast_shuffle_first_k(my_array, k):
    for i in range(0, k):
        j = rnd.randint(0, len(my_array) - 1)
        aux = my_array[i]
        my_array[i] = my_array[j]
        my_array[j] = aux


def add_customers():
    clearDataBase.clear_collection("customers")
    customers = db["customers"]

    with open('resources/customers.json') as json_file:
        data = json.load(json_file)
        customers.insert_many(data)
        print("Customers added: " + str(customers.count()))


def add_restaurants():
    clearDataBase.clear_collection("restaurants")
    restaurants = db["restaurants"]

    with open('resources/restaurants.json') as json_file:
        data = json.load(json_file)
        restaurants.insert_many(data)
        print("Restaurants added: " + str(restaurants.count()))


def add_reviews():
    clearDataBase.clear_collection("reviews")
    REVIEWS_PER_CUSTOMERS = 5

    restaurants = list(db["restaurants"].find())
    customers = list(db["customers"].find())
    reviews_data = []
    reviews = db["reviews"]

    restaurants_count = len(restaurants)
    restaurants_indices = list(range(restaurants_count))

    assert restaurants_count >= REVIEWS_PER_CUSTOMERS

    for customer in customers:
        # use this function instead of classic randint to avoid duplicate review (customer_id, restaurant_id)
        fast_shuffle_first_k(restaurants_indices, REVIEWS_PER_CUSTOMERS)
        for i in range(0, REVIEWS_PER_CUSTOMERS):
            restaurant = restaurants[restaurants_indices[i]]
            review = dict()
            review["restaurant_id"] = restaurant["_id"]
            review["customer_id"] = customer["_id"]
            review["score"] = rnd.randint(1, 5)
            reviews_data.append(review)
    reviews.insert_many(reviews_data)
    print("Reviews added: " + str(reviews.count()))

def add_orders():
    clearDataBase.clear_collection("orders")
    MAX_ORDERS_PER_CLIENT = 30

    restaurants = list(db["restaurants"].find())
    customers = list(db["customers"].find())
    orders_data = []
    orders = db["orders"]

    restaurants_count = len(restaurants)
    for customer in customers:
        current_customer_orders_count = rnd.randint(0, MAX_ORDERS_PER_CLIENT)
        for i in range(0, current_customer_orders_count):
            restaurant = restaurants[rnd.randint(0, restaurants_count - 1)]
            order = dict()
            order["restaurant_id"] = restaurant["_id"]
            order["customer_id"] = customer["_id"]
            order["order_date"] = rnd.randint(1, 100)  # just for test
            orders_data.append(order)
    orders.insert_many(orders_data)
    print("Orders added: " + str(orders.count()))

add_restaurants()
add_customers()
add_reviews()
add_orders()
