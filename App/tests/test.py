from django.test import SimpleTestCase
from django.urls import reverse
from django.test import Client

import requests
from config import API_KEY_WEATHER

from jsonschema import validate
from cerberus import Validator
from assertpy import assert_that


def test_get_forecast_for_today():
    schema = {
        'coord': {'type': 'dict'},
        'weather': {'id': {'type': 'integer'},
                    'main': {'type': 'string'},
                    'description': {'type': 'string'},
                    'icon': {'type': 'string'}
                    },
        'base': {'type': 'string'},
        'main': {'temp': {'type': 'integer'},
                 'feels_like': {'type': 'integer'},
                 'temp_min': {'type': 'integer'},
                 'temp_max': {'type': 'integer'},
                 'pressure': {'type': 'integer'},
                 'humidity': {'type': 'integer'},
                 'sea_level': {'type': 'integer'},
                 'grnd_level': {'type': 'integer'}
                 },
        'visibility': {'type': 'integer'},
        'wind': {'speed': {'type': 'integer'},
                 'deg': {'type': 'integer'},
                 'gust': {'type': 'integer'}
                 },
        'clouds': {'all': {'type': 'integer'}
                   },
        'dt': {'type': 'integer'},
        'sys': {'type': {'type': 'integer'},
                'id': {'type': 'integer'},
                'country': {'type': 'string'},
                'sunrise': {'type': 'integer'},
                'sunset': {'type': 'integer'}},
        'timezone': {'type': 'integer'},
        'id': {'type': 'integer'},
        'name': {'type': 'string'},
        'cod': {'type': 'integer'}
    }

    response = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q=Москва&units'
                            f'=metric&lang=ru&appid={API_KEY_WEATHER}')
    assert response.headers['Content-Type'] == "application/json; charset=utf-8"

    # assert validate(response.json(), schema) is None

    # v = Validator(schema)
    # validate_response = v.validate(response.json())
    # assert_that(validate_response, description=v.errors).is_true()




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

# def test_request_to_api_forecast():
#     content = json.loads(response.content)
#     assert 'result' in content
#     assert content['result'] == 'ok'
