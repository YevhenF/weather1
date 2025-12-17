city = str(input('Введите название своего города: '))
import requests
response = requests.get(f'https://wttr.in/{city}?format=j1')
data = response.json()
print('Темпуратура в городе ', city,data["current_condition"][0]["temp_C"], ' градусов')
