import requests

apiKey = 'b29b234747070571e4f979b673dc7f29'

city_name = input('Enter city name: ')

url = f'http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={apiKey}'

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    temp= data['main']['temp']
    description = data['weather'][0]['description']
    print(f'Temperature: {temp} K or {round((temp-273),2)} C')
    print(f'Description: {description}')
else:
    print('Error fetching weather data')