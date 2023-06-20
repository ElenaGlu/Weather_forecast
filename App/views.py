from django.shortcuts import get_object_or_404, render

from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import PlaceForm

import requests
import json


def search_place(request):
    return render(request, 'App/search.html')


def get_place(request):
    form = PlaceForm(request.POST or None)
    place = ''
    if request.method == 'POST':
        # if form.is_valid():
        place = request.POST.get('place')
        url_today = ('https://api.openweathermap.org/data/2.5/weather?q=' + place +
                     '&units=metric&lang=ru&appid=cd1ab723a1cf674c1fd4544a78684676')
        url_week = ('https://api.openweathermap.org/data/2.5/forecast?q=' + place +
                    '&units=metric&lang=ru&appid=cd1ab723a1cf674c1fd4544a78684676')

        weather_day = requests.get(url_today).text
        data_day = json.loads(weather_day)

        conditions = str(data_day['weather'][0]['description'])
        temperature = str(round(data_day['main']['temp']))
        temperature_feels = str(round(data_day['main']['feels_like']))
        clouds = str(round(data_day['clouds']['all']))
        pressure = str(round(data_day['main']['pressure']))
        humidity = str(round(data_day['main']['humidity']))
        visibility = str(round(data_day['visibility']))
        wind_speed = str(round(data_day['wind']['speed']))
        temp_min = str(round(data_day['main']['temp_min']))
        temp_max = str(round(data_day['main']['temp_max']))

        weather_week = requests.get(url_week).text
        data_week = json.loads(weather_week)

        dict1 = {}

        for i in range(len(data_week['list'])):
            f = (str(data_week['list'][i]['dt_txt']))[:11]
            minimal = int(str(str(round(data_week['list'][i]['main']['temp_min']))))
            maximum = int(str(str(round(data_week['list'][i]['main']['temp_max']))))
            if f not in dict1.keys():
                dict1[f] = [100, -100]
            if dict1[f][0] > minimal:
                dict1[f][0] = minimal
            if dict1[f][1] < maximum:
                dict1[f][1] = maximum
        print(dict1)

        return render(request, 'App/weather_forecast.html', {'place': place, 'temperature': temperature,
                                                             'temperature_feels': temperature_feels, 'clouds': clouds,
                                                             'pressure': pressure, 'humidity': humidity,
                                                             'visibility': visibility, 'wind_speed': wind_speed,
                                                             'temp_min': temp_min, 'temp_max': temp_max,
                                                             'conditions': conditions, })
        # else:
        #     form = PlaceForm()
    return render(request, 'App/search.html')
