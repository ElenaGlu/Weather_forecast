import requests
import json
import datetime

from config import API_KEY_WEATHER


def get_data_about_city(city: str) -> dict:
    url_today = f'https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&lang=ru&appid={API_KEY_WEATHER}'
    data_today = loads_json(url_today)
    forecast_today = {'city': city, 'conditions': str(data_today['weather'][0]['description']),
                      'temperature': str(round(data_today['main']['temp'])),
                      'temperature_feels': str(round(data_today['main']['feels_like'])),
                      'clouds': str(round(data_today['clouds']['all'])),
                      'pressure': str(round((data_today['main']['pressure']) / 1.333)),
                      'humidity': str(round(data_today['main']['humidity'])),
                      'visibility': str(round(data_today['visibility'])),
                      'wind_speed': str(round(data_today['wind']['speed'])),
                      'sunrise_timestamp': datetime.datetime.fromtimestamp(data_today["sys"]["sunrise"]),
                      'sunset_timestamp': datetime.datetime.fromtimestamp(data_today["sys"]["sunset"])}

    url_five_day = f'https://api.openweathermap.org/data/2.5/forecast?q={city}&units=metric&lang=ru&appid={API_KEY_WEATHER}'
    data_week = loads_json(url_five_day)
    forecast_five_day = {}
    for part_day in range(len(data_week['list'])):
        one_full_day = (str(data_week['list'][part_day]['dt_txt']))[:11]
        weather_description = str(data_week['list'][part_day]['weather'][0]['description'])
        temp_min = int(str(str(round(data_week['list'][part_day]['main']['temp_min']))))
        temp_max = int(str(str(round(data_week['list'][part_day]['main']['temp_max']))))

        if one_full_day not in forecast_five_day.keys():
            forecast_five_day[one_full_day] = [100, -100, '']
        if forecast_five_day[one_full_day][0] > temp_min:
            forecast_five_day[one_full_day][0] = temp_min
        if forecast_five_day[one_full_day][1] < temp_max:
            forecast_five_day[one_full_day][1] = temp_max
        forecast_five_day[one_full_day][2] = weather_description

    full_forecast = {'forecast_today': forecast_today, 'forecast_five_day': forecast_five_day}
    return full_forecast


def loads_json(url: str):
    forecast_requests = requests.get(url).text
    return json.loads(forecast_requests)
