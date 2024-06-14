import requests


api_key = API_KEY


def get_route_coords(api_key):
    url = "https://api.routing.yandex.net/v1.0/router/?"
    params = {
        "apikey": api_key,
        "points": f"{starting point of the route},{end point of the route}"
    }

    response = requests.get(url, params=params)
    data = response.json()

    if "error" in data:
        print("Error:", data["message"])
        return None

    coords = []
    for feature in data["response"]["GeoObjectCollection"]["featureMember"]:
        coords.extend(feature["GeoObject"]["Point"]["pos"].split())

    return coords


coords = get_route_coords(api_key)
print(coords)
