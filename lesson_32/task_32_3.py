#  Write a console application which takes as an input a city name
#  and returns current weather in the format of your choice.
#  For the current task, you can choose any weather API or website or use https://openweathermap.org

import requests


def weather():
    req = ''
    city = input('Please write a city name: ')
    params = {'q': city, 'appid': 'e5ae9e64f88b3ee14ebc5e014731f347', 'units' : 'metric'}
    try:
        req = requests.get(' http://api.openweathermap.org/data/2.5/weather', params=params)
    except Exception:
        print('oops')
    if req:
        res = req.json()
        print('City: ', city)
        print('Temperature: ', res['main']['temp'])
        print('Feels like: ', res['main']['feels_like'])
    else:
        print('city not founded')


if __name__ == '__main__':
    weather()