from django.test import SimpleTestCase
from django.urls import reverse
from django.test import Client

from config import API_KEY_WEATHER

import requests
from json_checker import Checker


def test_get_forecast_for_today():
    response = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q=Москва&units'
                            f'=metric&lang=ru&appid={API_KEY_WEATHER}')
    assert response.headers['Content-Type'] == "application/json; charset=utf-8"

    schema = {
        'city': str,
        'conditions': str,
        'temperature': int,
        'temperature_feels': int,
        'clouds': int,
        'pressure': int,
        'humidity': int,
        'visibility': int,
        'wind_speed': int,
    }

    dict1 = {'city': 'Москва', 'conditions': 'пасмурно', 'temperature': 22, 'temperature_feels': 21, 'clouds': 95,
             'pressure': 766, 'humidity': 52, 'visibility': 10000, 'wind_speed': 5}

    checker = Checker(schema)
    result = checker.validate(dict1)

    assert result == dict1


class WeatherForecastTests(SimpleTestCase):
    def test_search_page(self):
        response = self.client.get(reverse("loading_search_page"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "App/base.html")

    def test_city_page(self):
        c = Client()
        response = c.post(reverse("displays_weather_forecast_in_the_city"), {'city': 'Москва'})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "App/weather_forecast.html")
