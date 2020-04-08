import math
import trie
import scipy.integrate as integrate

def get_nb_of_orders(orders, customer_id, restaurant_id):
    nb_of_orders =0
    for order in orders:
        if customer_id == order["customer_id"] and restaurant_id == order["restaurant_id"]:
            nb_of_orders=nb_of_orders +1
    return nb_of_orders

def get_review_score(reviews, customer_id, restaurant_id):
    score = 3
    for review in reviews:
      if customer_id == review["customer_id"] and restaurant_id == review["restaurant_id"]:
         score= review["score"]
    return score

def get_latest_order(orders, customer_id, restaurant_id):
    latest_order= math.inf
    for order in orders:
        if customer_id == order["customer_id"] and restaurant_id == order["restaurant_id"]:
            if(latest_order> order["order_date"]):
                latest_order=order["order_date"]
    return latest_order


def integrand(x):
    return (20/math.log(x+10))


def calculate_score (review_score, nb_of_orders, latest_order):
    first_integral = integrate.quad(integrand , 0, nb_of_orders)
    #print(first_integral[0])
    word_score = (review_score/5+1.1) *first_integral[0] *1/20+ 20 / math.log(latest_order+10)
    return word_score



def get_restaurant_name(restaurants, restaurant_id):

    for restaurant in restaurants:
        if restaurant_id == restaurant["restaurant_id"]:
            return restaurant["name"]


def insert_restaurant_in_trie(t, restaurants, reviews, orders, customer_id, restaurant_id):

    review_score = get_review_score(reviews, customer_id, restaurant_id)
    nb_of_orders = get_nb_of_orders(orders, customer_id, restaurant_id)
    latest_order = get_latest_order(orders, customer_id, restaurant_id)
    word_score = calculate_score(review_score, nb_of_orders, latest_order)
    name = get_restaurant_name(restaurants, restaurant_id)

    if name:
       t.insert(name, word_score, restaurant_id)
    return

def get_recommended_restaurant_from_trie(t, restaurant_prefix):
    recommended_restaurant_id=t.special_search(restaurant_prefix)
    return recommended_restaurant_id

def update_trie(t, restaurants , reviews, orders, customer_id):
    for order in orders:
        if customer_id == order["customer_id"]:
            insert_restaurant_in_trie(t, restaurants, reviews, orders, customer_id, order["restaurant_id"])
    return


'''def final(customer, reviews, restaurants, orders, customer_id, restaurant_prefix):

    t = trie.Trie()
    update_trie(t, restaurants , reviews, orders,  customer_id)
    recommendations = []
    restaurant_id=get_recommended_restaurant_from_trie(t, restaurant_prefix)
    recommendations.append(restaurant_id);
    return recommendations'''

def main(): #def final(customer, reviews, restaurants, orders, customer_id, restaurant_prefix):

    restaurants=[
        {
            "name": "ana",
            "restaurant_id": 1
        },
        {
            "name": "anul",
            "restaurant_id": 2
        },
        {
            "name": "anual",
            "restaurant_id": 3
        }
    ]
    reviews=[
        {
            "restaurant_id":1,
            "customer_id":1,
            "score":3
        },
        {
            "restaurant_id": 1,
            "customer_id": 2,
            "score": 5
        } ,
        {
            "restaurant_id": 3,
            "customer_id": 1,
            "score": 4
        }
    ]
    orders=[
        {
            "restaurant_id": 1,
            "customer_id": 2,
            "order_date":10
        },
        {
            "restaurant_id": 2,
            "customer_id": 1,
            "order_date": 15
        }
    ]
    t = trie.Trie()
    update_trie(t, restaurants , reviews, orders,  1)
    recommendations = []
    restaurant_id=get_recommended_restaurant_from_trie(t, "an")
    recommendations.append(get_restaurant_name(restaurants, restaurant_id));
    print(recommendations)
    return recommendations

if __name__ == '__main__':
    main()