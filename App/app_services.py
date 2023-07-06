import requests
import json
import datetime

from config import API_KEY_WEATHER


def loads_json(url: str):
    forecast_requests = requests.get(url).text
    return json.loads(forecast_requests)


def get_forecast_for_today(city: str) -> dict:
    request_for_today = loads_json(f'https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&lang=ru'
                                   f'&appid={API_KEY_WEATHER}')

    forecast_for_today = {'city': city, 'conditions': str(request_for_today['weather'][0]['description']),
                          'temperature': str(round(request_for_today['main']['temp'])),
                          'temperature_feels': str(round(request_for_today['main']['feels_like'])),
                          'clouds': str(round(request_for_today['clouds']['all'])),
                          'pressure': str(round((request_for_today['main']['pressure']) / 1.333)),
                          'humidity': str(round(request_for_today['main']['humidity'])),
                          'visibility': str(round(request_for_today['visibility'])),
                          'wind_speed': str(round(request_for_today['wind']['speed'])),
                          'sunrise_timestamp': datetime.datetime.fromtimestamp(request_for_today["sys"]["sunrise"]),
                          'sunset_timestamp': datetime.datetime.fromtimestamp(request_for_today["sys"]["sunset"])}
    return forecast_for_today


def get_forecast_for_five_days(city: str) -> dict:
    request_for_five_days = loads_json(f'https://api.openweathermap.org/data/2.5/forecast?q={city}&units=metric&lang'
                                       f'=ru&appid={API_KEY_WEATHER}')
    forecast_for_five_days = {}
    for part_day in range(len(request_for_five_days['list'])):
        one_full_day = (str(request_for_five_days['list'][part_day]['dt_txt']))[:11]
        weather_description = str(request_for_five_days['list'][part_day]['weather'][0]['description'])
        temp_min = int(str(str(round(request_for_five_days['list'][part_day]['main']['temp_min']))))
        temp_max = int(str(str(round(request_for_five_days['list'][part_day]['main']['temp_max']))))

        if one_full_day not in forecast_for_five_days.keys():
            forecast_for_five_days[one_full_day] = [100, -100, '']
        if forecast_for_five_days[one_full_day][0] > temp_min:
            forecast_for_five_days[one_full_day][0] = temp_min
        if forecast_for_five_days[one_full_day][1] < temp_max:
            forecast_for_five_days[one_full_day][1] = temp_max
        forecast_for_five_days[one_full_day][2] = weather_description

    return forecast_for_five_days
