from django.test import SimpleTestCase
from django.urls import reverse
from django.test import Client

from App.app_services import get_forecast_for_today, get_forecast_for_five_days

from jsonschema import validate


def test_get_forecast_for_today():
    schema = {
        'type': 'object',
        'required': ['city', 'conditions', 'temperature',
                     'temperature_feels', 'clouds', 'pressure',
                     'humidity', 'visibility', 'wind_speed',
                     'sunrise_timestamp', 'sunset_timestamp'],
        'properties': {
            'city': {
                'type': 'string'
            },
            'conditions': {
                'type': 'string'
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
            'sunrise_timestamp': {
                'format': 'date'
            },
            'sunset_timestamp': {
                'format': 'date'
            },
        }
    }

    response = get_forecast_for_today('Москва')
    assert not validate(response, schema)


def test_get_forecast_for_five_days():
    schema = {
        'type': 'object',
        'required': ['day_1', 'day_2', 'day_3', 'day_4', 'day_5', 'day_6'],
        'properties': {
            'day_1': {
                'type': 'array',
                'maxItems': 4,
                'minItems': 4

            },
            'day_2': {
                'type': 'array',
                'maxItems': 4,
                'minItems': 4
            },
            'day_3': {
                'type': 'array',
                'maxItems': 4,
                'minItems': 4
            },
            'day_4': {
                'type': 'array',
                'maxItems': 4,
                'minItems': 4
            },
            'day_5': {
                'type': 'array',
                'maxItems': 4,
                'minItems': 4
            },
            'day_6': {
                'type': 'array',
                'maxItems': 4,
                'minItems': 4
            }
        }
    }

    response = get_forecast_for_five_days('Москва')
    assert not validate(response, schema)


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
