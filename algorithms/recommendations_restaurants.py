import Constants


def get_preferred_restaurants(customer, reviews):
    preferences = []
    for review in reviews:
        if review[Constants.REVIEWER_ID] == customer and review[Constants.SCORE] > 3.5:
            preferences.append(review[Constants.PROVIDER_ID])
    return preferences


def get_cluster_top(customer_cluster, reviews):
    top = {}
    for customer in customer_cluster:
        preferences = get_preferred_restaurants(customer, reviews)
        for restaurant in preferences:
            if restaurant not in top:
                top[restaurant] = 1
            else:
                top[restaurant] += 1
    return top


def get_recommendations(customer, customer_clusters, tops):
    recommendations = []
    for customer_cluster in customer_clusters:
        if customer in customer_cluster:
            top = tops[customer_clusters.index(customer_cluster)]
            recommendations.append(list(top.keys())[-1])
    return recommendations


def final(customer, reviews, restaurants):
    if len(customer) != Constants.OBJECT_ID_LENGTH:
        raise ValueError("the customer id must be 24 characters long")
    tops = []
    customer_clusters = []
    for restaurant in restaurants:
        customer_cluster = []
        for review in reviews:
            if review[Constants.SCORE] > 3.5 and review[Constants.PROVIDER_ID] == restaurant[Constants.ID]:
                customer_cluster.append(review[Constants.REVIEWER_ID])

        customer_clusters.append(customer_cluster)
        top = get_cluster_top(customer_cluster, reviews)
        tops.append(top)
    return get_recommendations(customer[Constants.ID], customer_clusters, tops)

# http://127.0.0.1:5000/recommendations/restaurant
# token: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJfaWQiOiI1ZWIxNmZkZjRhZmJmNjU0OTY2Y2I2OGQiLCJpYXQiOjE1ODgyMzc0NTZ9.OG3o5XPIDDGlyFusinKVN11w27b5JYCSwLMl9XhYHeI
