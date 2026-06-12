#py -m pip install requests

import requests
import json
city = input("Enter City Name: ")
url = f"https://wttr.in/{city}?format=j1"
try:
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        current = data['current_condition'][0]
        print("\nWeather Report: ")
        print("=" * 40)
        print("Temperature: ",current['temp_C'],"C")
        print("Humidity: ",current['humidity'],"%")
        print("Wind Speed: ",current['windspeedKmph'],"Km/h")
        print("Description: ",current['weatherDesc'][0]['value'])
        with open("weather_data.json", "w") as file:
                json.dump(data, file, indent=4)
        print("Weather data saved Successfully.")
    else:
         print("Unable to fetch weather data.")
except Exception as e:
     print("Error: ",e)
  