import json
import requests
import Constants


class Foods(object):
    @staticmethod
    def all(token):
        url = 'http://159.65.247.164:3002/api/courses'
        headers = {"Authorization": "Bearer " + token}
        coursesCollection = json.loads(requests.get(url, headers=headers).text)
        coursesCollection = coursesCollection[Constants.DATA][Constants.COURSES_FILTERED]
        """allCourses = []
        for menu in coursesCollection:
            for restaurant_menu in coursesCollection[menu]:
                for course in coursesCollection[menu][restaurant_menu]:
                    print(course)
        """
        return coursesCollection

    @staticmethod
    def by_id(id, token):
        url = 'http://159.65.247.164:3002/api/courses/'+id
        headers = {"Authorization": "Bearer " + token}
        course = json.loads(requests.get(url, headers=headers).text)
        if Constants.DATA not in course:
            return "the item id : " + id + " from the order api does not appear in the courses api"
        course = course[Constants.DATA]
        return course
