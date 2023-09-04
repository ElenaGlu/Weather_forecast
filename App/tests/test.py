from django.test import SimpleTestCase
from django.urls import reverse
from django.test import Client

from config import API_KEY_WEATHER

import requests
from jsonschema import validate


def test_get_forecast_for_today():
    schema = {
        'type': 'object',
        'required': ['city', 'conditions', 'temperature',
                     'temperature_feels', 'clouds', 'pressure',
                     'humidity', 'visibility', 'wind_speed'],
        'properties': {
            'city': {
                'type': 'integer'
            },
            'conditions': {
                'type': 'integer'
            },
            'temperature': {
                'type': 'integer'
            },
            'temperature_feels': {
                'type': 'integer'
            },
            'clouds': {
                'type': 'integer'
            },
            'pressure': {
                'type': 'integer'
            },
            'humidity': {
                'type': 'integer'
            },
            'visibility': {
                'type': 'integer'
            },
            'wind_speed': {
                'type': 'integer'
            },
        }
    }
    #
    # response = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q=Москва&units'
    #                         f'=metric&lang=ru&appid={API_KEY_WEATHER}')
    assert response.headers['Content-Type'] == "application/json; charset=utf-8"

    assert response.status_code == 200
    assert validate(response.json(), schema)


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
