import requests
from bs4 import BeautifulSoup as BS
import json


response = requests.get("https://coursive.id/api/v1/courses/chto-takoe-vlog-i-kak-ego-vesti/")
if response.status_code == 200:
    x = response.text
    data = json.loads(x)
    for item in data["blocks"]:
        my_result = item['id'], item['title']
        my_dict = dict(my_result[i:i+2] for i in range(0, len(my_result), 2))
        print(my_dict)

