import json
import requests


class Foods(object):
    @staticmethod
    def all(token):
        url = 'http://159.65.247.164:3002/api/courses'
        headers = {"Authorization": "Bearer " + token}
        coursesCollection = json.loads(requests.get(url, headers=headers).text)
        coursesCollection = coursesCollection['data']['menus']
        allCourses = []
        for menu in coursesCollection:
            for restaurant_menu in coursesCollection[menu]:
                for course in coursesCollection[menu][restaurant_menu]:
                    print(course)
        return coursesCollection

    @staticmethod
    def by_id(id, token):
        url = 'http://159.65.247.164:3002/api/providers/' + id
        headers = {"Authorization": "Bearer " + token}
        restaurantsCollection = json.loads(requests.get(url, headers=headers).text)
        restaurantsCollection = restaurantsCollection['data']['provider']
        return restaurantsCollection
