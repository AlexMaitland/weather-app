# Weather365

Weather365 is an application designed to take input from users searching for either the current weather or a 5 day forecast in a specific city. 

## Functionality of Weather365

* The user is asked which city they would like the forecast for.![Screenshot by Snip My at 18 Jun 2023 at 20:23:12](https://github.com/AlexMaitland/weather-app/assets/122832821/02fe9eee-78fc-4276-80f0-dc44298ade3b)

* They are then presented with the option to either receive the current or 5-day forecast.
 <img width="953" alt="city-entered" src="https://github.com/AlexMaitland/weather-app/assets/122832821/7aa81ac7-fcd7-401b-a210-b659c3c250ad">

* The application then uses the API key to retrieve information from openweathermap.org.
* Once the information is provided the user may choose to search for the weather in a different location or not. If they do the application will ask for the same input from the user.<img width="953" alt="again" src="https://github.com/AlexMaitland/weather-app/assets/122832821/3e861f39-bd09-4410-bca7-2577d8bbfc04">

* Once the user is happy and they do not wish to continue Weather365 will bid them farewell.

## Testing

Using the PEP8 installed into the GitHub repository I was able to check that the code was formatted in an acceptable manner. There remains a few remianing highlighted errors which are down to the lines being longer than the recommended 79 characters. I worked to keep these down as much as possible, however, struggled with some inputs as I prioritised the users experience. 

It also highlighted the need for spaces beneath the functions which were easily fixed & the need for the API to be capitalised in order to make it clear that this data was not to be changed. 

I struggled to find an online linter which was able to pass my code through as I inported the requests module needed to access the openweathermap.org website. Also, as my API is kept in a seperate file in order to keep it secure this was also a problem I faced. 

## Deployment

The GitHub repository was linked to Heroku where the application was deployed using the following steps.

1. Create 'New App'
2. Choose name 'Weather365' & Region 'Europe'
3. Go to 'Settings' - Config Vars for the API and the PORT were created
4. Still in 'Settings' - Python & NodeJS buildpacks were added
5. Next, go to 'Deploy' where the GitHub repository was linked to the Heroku account & permissions granted. Here we also enabled 'Automatic Deploys' was enabled so that any future pushes to the repository would automatically updatethe Heroku program.

## Credits

The only credit required is for [Open Weather](https://openweathermap.org/) which allowed the creation of an API key so that requests for information can be made by the user & real-time information would be sent back.
