import unittest

from django.urls import reverse
from django.test import Client

from jsonschema import validate

from App.app_services import WeatherForecast


class WeatherForecastTests(unittest.TestCase):

    def test_search_page(self):
        """
        Requests a html page and checks its status code and the correctness of the template
        """
        c = Client()
        response = c.get(reverse("loading_search_page"))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response, "App/base.html")

    def test_city_page(self):
        """
        Requests a html page with city and checks its status code and the correctness of the template
        """
        c = Client()
        response = c.post(reverse("displays_weather_forecast_in_the_city"), {'city': 'Москва'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response, "App/weather_forecast.html")

    @staticmethod
    def test_data_processing_for_today():
        """
        Validation of the json schema in the forecast for today
        """
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
        forecast = WeatherForecast('Москва')
        json = {'coord': {'lon': 37.6156, 'lat': 55.7522},
                'weather': [{'id': 804, 'main': 'Clouds', 'description': 'пасмурно', 'icon': '04d'}],
                'base': 'stations',
                'main': {'temp': 5.16, 'feels_like': 2.24, 'temp_min': 3.94, 'temp_max': 6.29, 'pressure': 1011,
                         'humidity': 77, 'sea_level': 1011, 'grnd_level': 993}, 'visibility': 10000,
                'wind': {'speed': 3.69, 'deg': 76, 'gust': 4.83}, 'clouds': {'all': 100}, 'dt': 1697796218,
                'sys': {'type': 2, 'id': 2000314, 'country': 'RU', 'sunrise': 1697774956, 'sunset': 1697811554},
                'timezone': 10800, 'id': 524901, 'name': 'Москва', 'cod': 200}
        response = forecast.data_processing_for_today(json)
        assert not validate(response, schema)

    @staticmethod
    def test_data_processing_for_five_days():
        """
        Validation of the json schema in the forecast for five days
        """
        schema = {
            'type': 'object',
            'required': ['day', 'day_1', 'day_2', 'day_3', 'day_4', 'day_5'],
            'properties': {
                'day': {
                    'type': 'array',
                    'maxItems': 4,
                    'minItems': 4
                },
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
                }
            }
        }

        json = ''
        forecast = WeatherForecast('Москва')
        response = forecast.data_processing_for_five_days(json)
        assert not validate(response, schema)
