import requests

# address -> Курпской+9+к1
# test улица+Красная+Пресня+44с3
address = input()

url_geo = "http://geocode-maps.yandex.ru/1.x"

params = {
    'apikey': '40d1649f-0493-4b70-98ba-98533de7710b',
    'geocode': address,
    'format': 'json'
}
response = requests.get(url_geo, params)
coords = ''
if response:
    json_response = response.json()
    toponym = json_response["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]
    coords = toponym['Point']['pos']

    params_metro = {
        'apikey': '40d1649f-0493-4b70-98ba-98533de7710b',
        'll': ','.join(coords.split()),
        'geocode': 'Метро',
        'format': 'json'
    }
    response_m = requests.get(url_geo, params_metro)
    if response_m:
        json_response = response_m.json()
        toponym = json_response["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]
        adress = toponym["metaDataProperty"]["GeocoderMetaData"]["Address"]["Components"]
        village = ''
        for dct in adress:
            if dct['kind'] == "metro":
                village = dct['name']
        print(village)
    else:
        print('loooool')
else:
    print('lol')
