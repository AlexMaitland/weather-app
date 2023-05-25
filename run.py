import requests
from config import API_KEY

api_key = API_KEY

def get_weather(city):
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'

    response = requests.get(url)
    data = response.json()

    if response.status_code == 200:
        print(data)
        

    else:
        print("Error occurred while fetching weather data.")

get_weather('Tokyo')