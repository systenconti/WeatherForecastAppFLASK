import requests
from api_key import api_key


def get_data(place, forecast_days=None):
    params = {"q": place, "units": "metric", "cnt": forecast_days * 8, "appid": api_key}

    r = requests.get("http://api.openweathermap.org/data/2.5/forecast", params)
    response = r.json()
    filtered_data = response["list"]
    return filtered_data


if __name__ == "__main__":
    print(get_data("Warsaw", 1))
