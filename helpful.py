import random

import requests

url = "http://geocode-maps.yandex.ru/1.x"
url_image = 'https://static-maps.yandex.ru/1.x'
params = {
    'apikey': '40d1649f-0493-4b70-98ba-98533de7710b',
    'format': 'json'
}


def get_town_photo(town):
    params['geocode'] = town
    response = requests.get(url, params)
    if response:
        json_response = response.json()
        toponym = json_response["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]
        coords = toponym['Point']['pos'].split()

        pikch = requests.get(url_image,
                             {'ll': ','.join(coords), 'z': 14, 'l': random.choice(['sat', 'map', 'sat,skl'])})
        if pikch:
            with open('static/images/town.jpg', 'wb') as f:
                f.write(pikch.content)


# print(get_town_photo('Yaroslaval'))
get_town_photo('Ярославль')
