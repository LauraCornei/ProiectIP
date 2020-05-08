from models.Restaurants import Restaurants

# http://127.0.0.1:5000/recommendations/restaurant_by_food
# eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJfaWQiOiI1ZTk4YTIzNzk3YWVhMTM5YzJiOTk1OTIiLCJpYXQiOjE1ODgyNTgxMTZ9.1GCgbuMH_Pi9kNtIR7QTqrH7EIcW86rbjU_Fe1HYSVk
# Bearer Token(Authorization)

REVIEWER_ID = "reviewerId"
PROVIDER_ID = "providerId"
FFIELD = "category"
SCORE = "score"
ID = "_id"

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


def restaurant_top(reviews, fav_res, token):

    cluster = get_cluster(reviews, fav_res)
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


def filter_res(customer, reviews, token):
    fav_res = get_fav_res(customer, reviews)
    res_top = restaurant_top(reviews, fav_res, token)
    filtered_res = []

    res_body = Restaurants.by_id(fav_res, token)
    menu_fav = res_body["details"]["specials"]

    for provider in res_top:
        spec = provider["details"]["specials"]
        for item in menu_fav:
            if spec.count(item):
                filtered_res.append(provider[ID])

    res_dic = score_mean(reviews, list(set(filtered_res)))
    sorted_top = sorted(res_dic, key=lambda item: res_dic[item], reverse=True)

    if len(sorted_top) == 0:
        return res_top

    rtopbody = []
    res_top = sorted_top[0:9]
    for r in res_top:
        rtopbody.append(Restaurants.by_id(r, token))
    return rtopbody
