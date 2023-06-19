from django.shortcuts import get_object_or_404, render

from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import PlaceForm

import requests


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

        weather_data = requests.get(url_today).json()
        # conditions = str(round(weather_data['weather'][0]['description']))
        temperature = str(round(weather_data['main']['temp']))
        temperature_feels = str(round(weather_data['main']['feels_like']))
        clouds = str(round(weather_data['clouds']['all']))
        pressure = str(round(weather_data['main']['pressure']))
        humidity = str(round(weather_data['main']['humidity']))
        visibility = str(round(weather_data['visibility']))
        wind_speed = str(round(weather_data['wind']['speed']))
        temp_min = str(round(weather_data['main']['temp_min']))
        temp_max = str(round(weather_data['main']['temp_max']))

        weather_week = requests.get(url_week).json()
        temp_list = round(weather_week['main']['temp'])
        print(temp_list)

        return render(request, 'App/weather_forecast.html', {'place': place, 'temperature': temperature,
                                                             'temperature_feels': temperature_feels, 'clouds': clouds,
                                                             'pressure': pressure, 'humidity': humidity,
                                                             'visibility': visibility, 'wind_speed': wind_speed,
                                                             'temp_min': temp_min, 'temp_max': temp_max,})
        # else:
        #     form = PlaceForm()
    return render(request, 'App/search.html')
