from pymongo import MongoClient

client = MongoClient("mongodb+srv://test:proiectip@cluster0-cirwn.mongodb.net/test?retryWrites=true&w=majority")
db = client['proiectip']


def get_preffered_restaurants(customer, reviews):
    preferences = []
    for review in reviews:
        if review["customer_id"] == customer and review["score"] > 3.5:
            preferences.append(review["restaurant_id"])
    return preferences


def get_cluster_top(customer_cluster, reviews):
    top = {}
    for customer in customer_cluster:
        preferences = get_preffered_restaurants(customer, reviews)
        for restaurant in preferences:
            if restaurant not in top:
                top[restaurant] = 1
            else:
                top[restaurant] += 1
    # sorted_top = sorted(top.items(), key=lambda item: item[1])
    # return sorted_top
    return top


def get_reccomendations(customer, customer_clusters, tops):
    reccomendations = []
    for customer_cluster in customer_clusters:
        if customer in customer_cluster:
            top = tops[customer_clusters.index(customer_cluster)]
            reccomendations.append(list(top.keys())[-1])
    return reccomendations


def final(customer, reviews, customers, restaurants):
    tops = []
    customer_clusters = []
    for restaurant in restaurants:
        customer_cluster = []
        for review in reviews:
            if review["score"] > 3.5 and review["restaurant_id"] == restaurant["_id"]:
                customer_cluster.append(review["customer_id"])
        customer_clusters.append(customer_cluster)
        top = get_cluster_top(customer_cluster, reviews)
        tops.append(top)
    reccomendations = get_reccomendations(customer["_id"], customer_clusters, tops)
    reccomendations_names = []
    for rec in reccomendations:
        for restaurant in restaurants:
            if restaurant["_id"] == rec:
                reccomendations_names.append(restaurant["name"])
                break
    return reccomendations_names

restaurantsCollection = db['restaurants']
restaurants = list(restaurantsCollection.find())
customersCollection = db['customers']
customers = list(customersCollection.find())
reviewsCollection = db['reviews']
reviews = list(reviewsCollection.find())
print(final(customers[0], reviews, customers, restaurants))
