import json
from datetime import datetime

with open(r"C:\Users\Admin\Downloads\weather.json", "r") as weather_file:
    weather = json.load(weather_file)

sunrise_datestamp = weather["sys"]["sunrise"]
sunset_datestamp = weather["sys"]["sunset"]

sunrise_datetime = datetime.fromtimestamp(sunrise_datestamp)
sunset_datetime = datetime.fromtimestamp(sunset_datestamp)

print("City name: " + weather["name"])
print("Country code: " + weather ["sys"]["country"])
print("Current temperature: " + str(weather["main"]["temp"]))
print("Weather description: " + str(weather["weather"][0]["description"]))
print("Sunrise: " + str(sunrise_datetime) + " sunset: " + str(sunset_datetime))