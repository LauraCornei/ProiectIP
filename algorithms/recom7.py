from models.Customers import Customers
from models.Reviews import Reviews
from models.Foods import Foods
from models.Restaurants import Restaurants

# http://127.0.0.1:5000/recommendations/restaurant_by_food/5eb16fdf4afbf654966cb68d
# eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJfaWQiOiI1ZTk4YTIzNzk3YWVhMTM5YzJiOTk1OTIiLCJpYXQiOjE1ODgyNTgxMTZ9.1GCgbuMH_Pi9kNtIR7QTqrH7EIcW86rbjU_Fe1HYSVk
# Bearer Token(Authorization)

REVIEWER_ID = "reviewerId"
PROVIDER_ID = "providerId"
FFIELD = "category"
SCORE = "score"
ID = "_id"

token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJfaWQiOiI1ZWFhOTQ2ODMwYThmMTI5OGQ0ZmMyZjgiLCJpYXQiOjE1ODgzMjc1MDh9." \
        "PbCHEKVkf0vfq-An6Ocw98ey4KOhPER3LxPJ4hix32Q"


def get_fav_res(customer, reviews):
    max_review = -1
    fav_res = -1
    for review in reviews:
        if review[REVIEWER_ID] == customer[ID] and review[SCORE] > max_review:
            max_review = review[SCORE]
            fav_res = review[PROVIDER_ID]

    return fav_res


def get_cluster(reviews, fav_res):

    cluster = []
    for review in reviews:
        if review[PROVIDER_ID] == fav_res and review[SCORE] > 0:
            cluster.append(review[REVIEWER_ID])
    return cluster


def restaurant_top(reviews, fav_res):

    cluster = get_cluster(reviews, fav_res)
    print("cluster")
    print(cluster)
    restaurants = []
    for customer_id in cluster:
        for review in reviews:
            if review[REVIEWER_ID] == customer_id and review[SCORE] > 0 and review[PROVIDER_ID] != fav_res:
                restaurants.append(review[PROVIDER_ID])

    rset = list(set(restaurants))
    rset_body = []
    for r in rset:
        rset_body.append(Restaurants.by_id(r, token))

    return rset_body


def score_mean(reviews, res):
    score_dic = dict.fromkeys(res, 0)
    count_dic = dict.fromkeys(res, 0)
    for review in reviews:
        if res.count(review[PROVIDER_ID]):
            score_dic[review[PROVIDER_ID]] += review[SCORE]
            count_dic[review[PROVIDER_ID]] += 1

    mean_dic = dict.fromkeys(res)
    for r in res:
        mean_dic[r] = score_dic[r]/count_dic[r]

    return mean_dic


def filter_res(customer, reviews, foods, providers):
    fav_res = get_fav_res(customer, reviews)
    res_top = restaurant_top(reviews, fav_res)
    print("res_top")
    print(res_top)
    print(len(res_top))
    filtered_res = []
    menu_fav = []

    """for food in foods:
        print(food[PROVIDER_ID])
        if food[PROVIDER_ID] == fav_res:
            length = len(food[COURSES])
            for ii in range(length):
                # print(manjaro[0][COURSES][i][FFIELD])
                menu_fav.append(food[COURSES][ii][FFIELD])
"""
    res_body = Restaurants.by_id(fav_res, token)
    menu_fav = res_body["details"]["specials"]

    """for food in foods:
        for ii in range(len(food[COURSES])):
            if menu_fav.count(food[COURSES][ii][FFIELD]) and res_top.count(food[PROVIDER_ID]):
                filtered_res.append(food[PROVIDER_ID])"""

    for provider in res_top:
        spec = provider["details"]["specials"]
        for item in menu_fav:
            if spec.count(item):
                filtered_res.append(provider[ID])

    res_dic = score_mean(reviews, list(set(filtered_res)))
    sorted_top = sorted(res_dic, key=lambda item: res_dic[item], reverse=True)
    # for s in sorted_top:
    # print(res_dic[s])

    if len(sorted_top) == 0:
        return res_top

    rtopbody = []
    res_top = sorted_top[0:9]
    for r in res_top:
        rtopbody.append(Restaurants.by_id(r, token))
    return rtopbody


manjaro = Foods.all(token)
print(manjaro[0][FFIELD])

"""print(manjaro[0][COURSES][0][FFIELD])
print(manjaro[0][PROVIDER_ID])

l = len(manjaro[0][COURSES])

# Iterating the index
# same as 'for i in range(len(list))'
for i in range(l):
    print(manjaro[0][COURSES][i][FFIELD])
"""

a = Reviews.all(token)
print(a)

b = Customers.by_id("5eb16fdf4afbf654966cb68d", token)
print(b)

c = Reviews.by_provider_id("5eb16d673a637d28884dc226", token)
print(c)

#result = get_fav_res(Customers.by_id('5eb16fdf4afbf654966cb68d', token), Reviews.all(token))

result = filter_res(Customers.by_id('5eb16fdf4afbf654966cb68d', token), Reviews.all(token), Foods.all(token),
                    Restaurants.all(token))

print("result")
for r in result:
    print(r)

"""
#r = Restaurants.by_id(result, token)
#print(r["details"]["specials"])

#print(Foods.by_id('5eb175094afbf654966cb690', token))
"""