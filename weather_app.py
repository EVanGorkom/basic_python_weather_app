import requests
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv('API_KEY')
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

city = input("Enter a city name: ")
request_url = f"{BASE_URL}?q={city}&appid={API_KEY}"
response = requests.get(request_url)
if response.status_code == 200:
  data = response.json()
  weather = data['weather'][0]['description']
  print("Weather:", weather.title())
  temp = round(data['main']['temp'] - 255.37)
  print(f'Temperature: {temp}F Degrees')
else:
  print("An error occurred.")