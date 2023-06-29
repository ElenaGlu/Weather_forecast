import requests
import json
import datetime


def get_data_about_city(city):
    url_today = ('https://api.openweathermap.org/data/2.5/weather?q=' + city +
                 '&units=metric&lang=ru&appid=cd1ab723a1cf674c1fd4544a78684676')
    forecast_today = requests.get(url_today).text
    data_today = json.loads(forecast_today)

    clouds = str(round(data_today['clouds']['all']))
    pressure = str(round((data_today['main']['pressure']) / 1.333))
    humidity = str(round(data_today['main']['humidity']))
    visibility = str(round(data_today['visibility']))
    wind_speed = str(round(data_today['wind']['speed']))
    temperature_feels = str(round(data_today['main']['feels_like']))
    temperature = str(round(data_today['main']['temp']))
    conditions = str(data_today['weather'][0]['description'])
    sunrise_timestamp = datetime.datetime.fromtimestamp(data_today["sys"]["sunrise"])
    sunset_timestamp = datetime.datetime.fromtimestamp(data_today["sys"]["sunset"])


    url_five_day = ('https://api.openweathermap.org/data/2.5/forecast?q=' + city +
                '&units=metric&lang=ru&appid=cd1ab723a1cf674c1fd4544a78684676')
    forecast_five_day = requests.get(url_five_day).text
    data_week = json.loads(forecast_five_day)

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

    full_forecast = {'city': city, 'conditions': conditions,
                     'temperature': temperature,
                     'temperature_feels': temperature_feels, 'clouds': clouds,
                     'pressure': pressure, 'humidity': humidity,
                     'visibility': visibility, 'wind_speed': wind_speed,
                     'sunrise_timestamp': sunrise_timestamp,
                     'sunset_timestamp': sunset_timestamp,
                     'forecast_five_day': forecast_five_day}

    return full_forecast

# def loads_json():
