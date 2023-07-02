import requests
import json
from config import TOKEN

print("")
city = input("What city do you need to know the weather in?: ")
state = input("What is the state code?: ")
country = input("What is the country code?: ")

lonNlat = requests.get(f'http://api.openweathermap.org/geo/1.0/direct?q={city},{state},{country}&appid={TOKEN}').json()[0]

latitude = lonNlat["lat"]
longitude = lonNlat["lon"]
response = requests.get(f'https://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid={TOKEN}&units=metric')
data = response.json()["main"]

def jprint(obj):
    # create a formatted string of the Python JSON object
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

#jprint(response.json())

print("")
print("================================================================")
print("")
print("City: \033[1m" + response.json()["name"] + "\033[0m")
print("")
print("Current Temperature:\033[1m", data["temp"], "Celcius\033[0m")
print("Feels Like:\033[1m", data["feels_like"], "Celcius\033[0m")
print("")
print("Maximum:\033[1m", data["temp_max"], "Celcius\033[0m")
print("Minimum:\033[1m", data["temp_min"], "Celcius\033[0m")
print("")
