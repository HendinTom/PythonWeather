import requests
from config import TOKEN

latitude = 43.722
longitude = -79.748
response = requests.get(f'https://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid={TOKEN}')

print(response)
print(response.json())