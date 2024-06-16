def get_spn(json_response):
    # Получаем первый топоним из ответа геокодера.
    toponym = json_response["response"]["GeoObjectCollection"][
        "featureMember"][0]["GeoObject"]
    # Координаты центра топонима:
    lower = list(map(float, toponym["boundedBy"]['Envelope']['lowerCorner'].split()))
    upper = list(map(float, toponym["boundedBy"]['Envelope']['upperCorner'].split()))
    # Долгота и широта:
    return [str(abs(lower[0] - upper[0]) / 2), str(abs(lower[1] - upper[1]) / 2)]
