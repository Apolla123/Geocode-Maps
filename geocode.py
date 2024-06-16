def geocode(toponym_to_find):
    geocoder_api_server = "http://geocode-maps.yandex.ru/1.x/"

    geocoder_params = {
        "apikey": API_KEY,
        "geocode": toponym_to_find,
        "format": "json"}

    response = requests.get(geocoder_api_server, params=geocoder_params)

    if not response:
        print("Ошибка выполнения запроса ", response.url)
        print("Http статус:", response.status_code, "(", response.reason, ")")
        sys.exit(1)

    # Преобразуем ответ в json-объект
    return response.json()
