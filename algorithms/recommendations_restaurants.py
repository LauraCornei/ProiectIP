REVIEWER_ID = "reviewerId"
PROVIDER_ID = "providerId"
SCORE = "score" 
ID = "_id" 

def get_preferred_restaurants(customer, reviews):
    preferences = []
    for review in reviews:
        if review[REVIEWER_ID] == customer and review[SCORE] > 3.5:
            preferences.append(review[PROVIDER_ID])
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
    # sorted_top = sorted(top.items(), key=lambda item: item[1])
    # return sorted_top
    return top


def get_recommendations(customer, customer_clusters, tops):
    recommendations = []
    for customer_cluster in customer_clusters:
        if customer in customer_cluster:
            top = tops[customer_clusters.index(customer_cluster)]
            recommendations.append(list(top.keys())[-1])
    return recommendations


def final(customer, reviews, restaurants):
    tops = []
    customer_clusters = []
    for restaurant in restaurants:
        customer_cluster = []
        for review in reviews:
            if review[SCORE] > 3.5 and review[PROVIDER_ID] == restaurant[ID]:
                customer_cluster.append(review[REVIEWER_ID])
        customer_clusters.append(customer_cluster)
        top = get_cluster_top(customer_cluster, reviews)
        tops.append(top)
    return get_recommendations(customer[ID], customer_clusters, tops)
