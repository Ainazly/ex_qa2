import requests
from bs4 import BeautifulSoup as BS
import json


def get_response(url):
    response = requests.get(url)
    response_json = response.text
    return response_json


my_url = 'https://coursive.id/api/v1/courses'


def parse(link):
    data_list = []
    # print(123)
    courses_list_response = get_response(my_url)
    data = json.loads(courses_list_response)
    for item in data["results"]:
        id_ = item['id']
        title = item['title']
        data_list.append({
            'course_id': id_,
            'title': title
        })
    return data_list


get_response(my_url)

parse(my_url)
