import requests


api_key = API_KEY


def find(api_key, cityes):
    min = 9999999
    result = ''
    res = []
    for city in cityes.split(', '):
        geocoder_request = f"http://geocode-maps.yandex.ru/1.x/?apikey={api_key}&geocode={city}&format=json"
        response = requests.get(geocoder_request)
        if response:
            json_response = response.json()
            toponym = (json_response["response"]
                                    ["GeoObjectCollection"]['metaDataProperty']['GeocoderResponseMetaData']['results'])
            toponym_coodrinates = toponym['featureMember'][0]['GeoObject']["Point"]["pos"]
            res.append((toponym_coodrinates.split(' ')[1], city))
        else:
            print("Ошибка выполнения запроса:")
            print(geocoder_request)
            print("Http статус:", response.status_code, "(", response.reason, ")")

    for param in res:
        if param[0] < min:
            min = param[0]
            result = param[1]

    print(result)


find(api_key, "Москова, Санкт-Петербург, Йошкар-Ола, Волгоград, Новосибирск, Нижний Новгород")