from models.Restaurants import Restaurants

# http://127.0.0.1:5000/recommendations/restaurant_by_food
# eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJfaWQiOiI1ZWIxNmZkZjRhZmJmNjU0OTY2Y2I2OGQiLCJpYXQiOjE1ODgyMzc0NTZ9.OG3o5XPIDDGlyFusinKVN11w27b5JYCSwLMl9XhYHeI

# Bearer Token(Authorization)
import Constants


def get_fav_res(customer, reviews):
    max_review = -1
    fav_res = -1
    for review in reviews:
        if review[Constants.REVIEWER_ID] == customer[Constants.ID] and review[Constants.SCORE] > max_review:
            max_review = review[Constants.SCORE]
            fav_res = review[Constants.PROVIDER_ID]

    return fav_res


def get_cluster(reviews, fav_res):

    cluster = []
    for review in reviews:
        if review[Constants.PROVIDER_ID] == fav_res and review[Constants.SCORE] > 0:
            cluster.append(review[Constants.REVIEWER_ID])
    return cluster


def restaurant_top(reviews, fav_res, token):

    cluster = get_cluster(reviews, fav_res)
    restaurants = []
    for customer_id in cluster:
        for review in reviews:
            if review[Constants.REVIEWER_ID] == customer_id and review[Constants.SCORE] > 0 and review[Constants.PROVIDER_ID] != fav_res:
                restaurants.append(review[Constants.PROVIDER_ID])

    rset = list(set(restaurants))
    rset_body = []
    for r in rset:
        rset_body.append(Restaurants.by_id(r, token))

    return rset_body


def score_mean(reviews, res):
    score_dic = dict.fromkeys(res, 0)
    count_dic = dict.fromkeys(res, 0)
    for review in reviews:
        if res.count(review[Constants.PROVIDER_ID]):
            score_dic[review[Constants.PROVIDER_ID]] += review[Constants.SCORE]
            count_dic[review[Constants.PROVIDER_ID]] += 1

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
                filtered_res.append(provider[Constants.ID])

    res_dic = score_mean(reviews, list(set(filtered_res)))
    sorted_top = sorted(res_dic, key=lambda item: res_dic[item], reverse=True)

    if len(sorted_top) == 0:
        return res_top

    rtopbody = []
    res_top = sorted_top[0:9]
    for r in res_top:
        rtopbody.append(Restaurants.by_id(r, token))
    return rtopbody
