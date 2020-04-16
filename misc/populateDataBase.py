from pymongo import MongoClient
import json
import clearDataBase
import random as rnd
import db

RANDOM_SEED = 324324
rnd.seed(RANDOM_SEED)


# shuffle first k elements of the array with any other elements
def fast_shuffle_first_k(my_array, k):
    for i in range(0, k):
        j = rnd.randint(0, len(my_array) - 1)
        aux = my_array[i]
        my_array[i] = my_array[j]
        my_array[j] = aux


def add_ingredients():
    clearDataBase.clear_collection("ingredients")
    ingredients = db.ingredientsCollection

    with open('resources/ingredients.json') as json_file:
        data = json.load(json_file)
        ingredients.insert_many(data)
        print("Ingredients added: " + str(ingredients.count()))


def add_customers():
    clearDataBase.clear_collection("customers")
    customers = db.customersCollection
    MIN_ALLERGIES_PER_CUSTOMER = 0
    MAX_ALLERGIES_PER_CUSTOMER = 3
    ingredients = list(db.ingredientsCollection.find())

    ingredients_indices = list(range(len(ingredients)))

    with open('resources/customers.json') as json_file:
        data = json.load(json_file)
        customers_data = []
        for customer_name in data:
            customer = dict()
            customer["first_name"] = customer_name["first_name"]
            customer["last_name"] = customer_name["last_name"]
            allergies_number = rnd.randint(MIN_ALLERGIES_PER_CUSTOMER, MAX_ALLERGIES_PER_CUSTOMER)
            fast_shuffle_first_k(ingredients_indices, allergies_number)
            allergies = []
            for i in range(allergies_number):
                allergies.append(ingredients[ingredients_indices[i]]["_id"])

            customer["allergies"] = allergies

            customers_data.append(customer)

        customers.insert_many(customers_data)
        print("Customers added: " + str(customers.count()))


def add_restaurants():
    clearDataBase.clear_collection("restaurants")
    restaurants = db.restaurantsCollection

    with open('resources/restaurants.json') as json_file:
        data = json.load(json_file)
        restaurants_data = []
        for restaurant_name in data:
            restaurant = dict()
            restaurant["name"] = restaurant_name["name"]
            restaurant["image"] = "https://loremflickr.com/320/240"
            restaurants_data.append(restaurant)

        restaurants.insert_many(restaurants_data)
        print("Restaurants added: " + str(restaurants.count()))


def add_foods():
    clearDataBase.clear_collection("foods")
    MIN_FOODS_PER_RESTAURANT = 3
    MAX_FOODS_PER_RESTAURANT = 20
    MIN_INGREDIENTS_PER_FOOD = 3
    MAX_INGREDIENTS_PER_FOOD = 10
    foods = db.foodsCollection
    restaurants = list(db.restaurantsCollection.find())
    ingredients = list(db.ingredientsCollection.find())

    ingredients_indices = list(range(len(ingredients)))
    with open('resources/foods.json') as json_file:
        data = json.load(json_file)
        foods_data = []
        for restaurant in restaurants:
            food_count = rnd.randint(MIN_FOODS_PER_RESTAURANT, MAX_FOODS_PER_RESTAURANT)

            for i in range(0, food_count):
                food = dict()
                food["name"] = data[rnd.randint(0, len(data) - 1)]["name"]
                food["restaurant_id"] = restaurant["_id"]
                food["serving_size"] = rnd.randint(100, 999)
                food["price"] = rnd.randint(10, 100)

                ingredients_number = rnd.randint(MIN_INGREDIENTS_PER_FOOD, MAX_INGREDIENTS_PER_FOOD)
                fast_shuffle_first_k(ingredients_indices, ingredients_number)
                food_ingredients = []
                for i in range(ingredients_number):
                    food_ingredients.append(ingredients[ingredients_indices[i]]["_id"])

                food["ingredients"] = food_ingredients
                foods_data.append(food)

        foods.insert_many(foods_data)
        print("Foods added: " + str(foods.count()))


def add_reviews():
    clearDataBase.clear_collection("reviews")
    REVIEWS_PER_CUSTOMERS = 5

    restaurants = list(db.restaurantsCollection.find())
    customers = list(db.customersCollection.find())
    reviews_data = []
    reviews = db.reviewsCollection

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


def get_food_per_restaurant(foods):
    food_per_restaurant = dict()
    for food in foods:
        if food["restaurant_id"] not in food_per_restaurant:
            food_per_restaurant[food["restaurant_id"]] = []
        food_per_restaurant[food["restaurant_id"]].append(food)
    return food_per_restaurant


def add_orders():
    from generateRandomDatetime import gen_datetime
    clearDataBase.clear_collection("orders")
    MAX_ORDERS_PER_CLIENT = 30

    restaurants = list(db.restaurantsCollection.find())
    customers = list(db.customersCollection.find())
    foods = list(db.foodsCollection.find())
    orders_data = []
    orders = db.ordersCollection

    restaurants_count = len(restaurants)
    super_restaurant = restaurants[0]
    foods_per_restaurant = get_food_per_restaurant(foods)
    for customer in customers:
        current_customer_orders_count = rnd.randint(1, MAX_ORDERS_PER_CLIENT)
        for i in range(0, current_customer_orders_count):
            restaurant = restaurants[rnd.randint(0, restaurants_count - 1)]
            order = dict()
            order["restaurant_id"] = restaurant["_id"]
            order["customer_id"] = customer["_id"]

            specific_food = foods_per_restaurant[restaurant["_id"]]
            order["food_id"] = specific_food[rnd.randint(0, len(specific_food) - 1)]["_id"]
            order["order_date"] = str(gen_datetime())

            orders_data.append(order)

        # just for test
        for i in range(0, 40):
            restaurant = super_restaurant
            order = dict()
            order["restaurant_id"] = restaurant["_id"]
            order["customer_id"] = customer["_id"]

            specific_food = foods_per_restaurant[restaurant["_id"]]
            order["food_id"] = specific_food[rnd.randint(0, len(specific_food) - 1)]["_id"]
            order["order_date"] = str(gen_datetime())

            orders_data.append(order)

    print("Restaurant id: " + str(super_restaurant["_id"]))
    orders.insert_many(orders_data)
    print("Orders added: " + str(orders.count()))


add_restaurants()
add_customers()
add_ingredients()
add_foods()
add_reviews()
add_orders()
