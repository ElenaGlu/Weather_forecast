import requests
import json
import datetime
from WeatherApp.App.views import get_place
from .forms import PlaceForm


def get_data_about_city():
    city = PlaceForm(request.POST or None)
    city = request.POST.get('city')
    url_today = ('https://api.openweathermap.org/data/2.5/weather?q=' + city +
                 '&units=metric&lang=ru&appid=cd1ab723a1cf674c1fd4544a78684676')
    weather_today = requests.get(url_today).text
    data_today = json.loads(weather_today)

    conditions = str(data_today['weather'][0]['description'])
    temperature = str(round(data_today['main']['temp']))
    temperature_feels = str(round(data_today['main']['feels_like']))
    clouds = str(round(data_today['clouds']['all']))
    pressure = str(round((data_today['main']['pressure']) / 1.333))
    humidity = str(round(data_today['main']['humidity']))
    visibility = str(data_today['visibility'])
    wind_speed = str(round(data_today['wind']['speed']))
    sunrise_timestamp = datetime.datetime.fromtimestamp(data_today["sys"]["sunrise"])
    sunset_timestamp = datetime.datetime.fromtimestamp(data_today["sys"]["sunset"])

    url_week = ('https://api.openweathermap.org/data/2.5/forecast?q=' + city +
                '&units=metric&lang=ru&appid=cd1ab723a1cf674c1fd4544a78684676')
    weather_five_day = requests.get(url_week).text
    data_week = json.loads(weather_five_day)

    forecast_five_day = {}

    for i in range(len(data_week['list'])):
        f = (str(data_week['list'][i]['dt_txt']))[:11]
        descript = str(data_week['list'][i]['weather'][0]['description'])
        minimal = int(str(str(round(data_week['list'][i]['main']['temp_min']))))
        maximum = int(str(str(round(data_week['list'][i]['main']['temp_max']))))

        if f not in forecast_five_day.keys():
            forecast_five_day[f] = [100, -100, '']
        if forecast_five_day[f][0] > minimal:
            forecast_five_day[f][0] = minimal
        if forecast_five_day[f][1] < maximum:
            forecast_five_day[f][1] = maximum
        forecast_five_day[f][2] = descript

    dict1 = {'city': city, 'conditions': conditions,
             'temperature': temperature,
             'temperature_feels': temperature_feels, 'clouds': clouds,
             'pressure': pressure, 'humidity': humidity,
             'visibility': visibility, 'wind_speed': wind_speed,
             'sunrise_timestamp': sunrise_timestamp,
             'sunset_timestamp': sunset_timestamp,
             'forecast_five_day': forecast_five_day}

    return dict1
