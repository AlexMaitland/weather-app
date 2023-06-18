import requests
from config import API_KEY

API = API_KEY


def validate_location(city):
    """
    Checks whether the city input is valid.
    """
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API}'

    response = requests.get(url)

    if response.status_code == 200:
        return True
    else:
        return False


def get_weather(city):
    """
    Gets the requested current weather in the city
    which the user input and displays the temperature
    and description.
    """
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API}'

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


def get_forecast(city):
    """
    Gets the requested 5 day forecast for the city
    which the user input and displays the temperature
    and description.
    """

    url = f'http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={API}'

    response = requests.get(url)
    data = response.json()

    if response.status_code == 200:
        # Extract and display forecasted temperatures and weather descriptions
        print(f"Weather forecast for the next five days in {city}:")
        for forecast in data['list']:
            forecast_date = forecast['dt_txt']
            if forecast_date.endswith('12:00:00'):
                temperature = data['main']['temp'] - 273.15
                description = forecast['weather'][0]['description']
                print(f"Date: {forecast_date}")
                print(f"Temperature: {temperature:.2f}°C")
                print(f"Description: {description}")
    else:
        print("Error occurred while fetching weather forecast data.")    


def main():

    """
    Main function
    """
    print('Welcome to Weather365!\n')
    
    while True:

        city = input("Enter the city name: \n")

        while not validate_location(city):
            print("Invalid city. Please enter a valid city name.")
            city = input("Enter the city name: \n")
        
        choice = input("Enter 'current' for current weather or 'forecast' for the next five days: \n")

        while choice.lower() not in ['current', 'forecast']:
            print("Invalid choice. Please enter 'current' or 'forecast'.")
            choice = input("Enter 'current' for current weather or 'forecast' for the next five days: \n")

        if choice.lower() == 'current':
            get_weather(city)
        elif choice.lower() == 'forecast':
            get_forecast(city)
        
        response = input("Check the weather again? (yes/no): \n")
        if response.lower() != 'yes':
            print("Goodbye and thank you! Come back soon.")
            break


main()