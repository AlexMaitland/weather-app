import requests
from config import API_KEY

api_key = API_KEY

def get_weather(city):
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'

    response = requests.get(url)
    data = response.json()

    if response.status_code == 200:
        temperature = data['main']['temp'] - 273.15

        description = data['weather'][0]['description']
        

        print(f"Current weather in {city}:")
        print(f"Temperature: {temperature:.2f}°C")
        print(f"Description: {description}")
        

    else:
        print("Error occurred while fetching weather data.")

def main():

    print('Welcome to The Weather App!\n')
    city = input("Please enter the city you require the weather for: ")

    get_weather(city)

main()