
import requests
from geopy.geocoders import Nominatim

def is_city_valid(city: str) -> bool:
    geolocator = Nominatim(user_agent="weathers_project")
    location = geolocator.geocode(city)
    return location is not None


class Weathers:

    def entering_city(self, city):
        self.city = city

    def requests_info(self, data):
        self.data = data

    def print_weather(self):
        print('Темпуратура в городе ', self.city, self.data["current_condition"][0]["temp_C"], ' градусов')

city = input('Введите название своего города: ')

# Проверяем город через GeoPy
if not is_city_valid(city):
    print(f"❌ Город {city} не найден")
    exit()
print(f"✅ Город {city} валиден")

request = requests.get(f'https://wttr.in/{city}?format=j1')
data = request.json()
inputs_weathers= Weathers()
inputs_weathers.entering_city(city)
inputs_weathers.requests_info(data)
inputs_weathers.print_weather()



# import geonamescache
#
# gc = geonamescache.GeonamesCache()
# cities = gc.get_cities()
#
# city_name = "Kyiv"
#
# is_valid = any(
#     city["name"].lower() == city_name.lower()
#     for city in cities.values()
#)