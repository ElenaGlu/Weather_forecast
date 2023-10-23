from django.test import TestCase
from django.urls import reverse


from jsonschema import validate


from App.app_services import WeatherForecast


class WeatherForecastTests(TestCase):

    def test_search_page(self):
        """
        Requests a html page and checks its status code and the correctness of the template
        """
        response = self.client.get(reverse("loading_search_page"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "App/base.html")

    def test_city_page(self):
        """
        Requests a html page with city and checks its status code and the correctness of the template
        """
        response = self.client.post(reverse("displays_weather_forecast_in_the_city"), {'city': 'Москва'})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "App/weather_forecast.html")

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
        json = {
            "coord": {
                "lon": 37.6156,
                "lat": 55.7522
            },
            "weather": [
                {
                    "id": 804,
                    "main": "Clouds",
                    "description": "пасмурно",
                    "icon": "04d"
                }
            ],
            "base": "stations",
            "main": {
                "temp": 5.16,
                "feels_like": 2.24,
                "temp_min": 3.94,
                "temp_max": 6.29,
                "pressure": 1011,
                "humidity": 77,
                "sea_level": 1011,
                "grnd_level": 993
            },
            "visibility": 10000,
            "wind": {
                "speed": 3.69,
                "deg": 76,
                "gust": 4.83
            },
            "clouds": {
                "all": 100
            },
            "dt": 1697796218,
            "sys": {
                "type": 2,
                "id": 2000314,
                "country": "RU",
                "sunrise": 1697774956,
                "sunset": 1697811554
            },
            "timezone": 10800,
            "id": 524901,
            "name": "Москва",
            "cod": 200
        }

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
        forecast = WeatherForecast('Москва')
        json = {
            "cod": "200",
            "message": 0,
            "cnt": 40,
            "list": [
                {
                    "dt": 1698073200,
                    "main": {
                        "temp": 5.52,
                        "feels_like": 4.02,
                        "temp_min": 5.52,
                        "temp_max": 5.61,
                        "pressure": 1001,
                        "sea_level": 1001,
                        "grnd_level": 982,
                        "humidity": 95,
                        "temp_kf": -0.09
                    },
                    "weather": [
                        {
                            "id": 500,
                            "main": "Rain",
                            "description": "небольшой дождь",
                            "icon": "10n"
                        }
                    ],
                    "clouds": {
                        "all": 100
                    },
                    "wind": {
                        "speed": 1.95,
                        "deg": 9,
                        "gust": 3.08
                    },
                    "visibility": 10000,
                    "pop": 1,
                    "rain": {
                        "3h": 1.67
                    },
                    "sys": {
                        "pod": "n"
                    },
                    "dt_txt": "2023-10-23 15:00:00"
                },

                {
                    "dt": 1698105600,
                    "main": {
                        "temp": 2.91,
                        "feels_like": -0.84,
                        "temp_min": 2.91,
                        "temp_max": 2.91,
                        "pressure": 1005,
                        "sea_level": 1005,
                        "grnd_level": 987,
                        "humidity": 96,
                        "temp_kf": 0
                    },
                    "weather": [
                        {
                            "id": 500,
                            "main": "Rain",
                            "description": "небольшой дождь",
                            "icon": "10n"
                        }
                    ],
                    "clouds": {
                        "all": 100
                    },
                    "wind": {
                        "speed": 4.21,
                        "deg": 326,
                        "gust": 9.34
                    },
                    "visibility": 27,
                    "pop": 0.96,
                    "rain": {
                        "3h": 0.62
                    },
                    "sys": {
                        "pod": "n"
                    },
                    "dt_txt": "2023-10-24 00:00:00"
                },

                {
                    "dt": 1698192000,
                    "main": {
                        "temp": -0.61,
                        "feels_like": -3.22,
                        "temp_min": -0.61,
                        "temp_max": -0.61,
                        "pressure": 1017,
                        "sea_level": 1017,
                        "grnd_level": 999,
                        "humidity": 78,
                        "temp_kf": 0
                    },
                    "weather": [
                        {
                            "id": 802,
                            "main": "Clouds",
                            "description": "переменная облачность",
                            "icon": "03n"
                        }
                    ],
                    "clouds": {
                        "all": 39
                    },
                    "wind": {
                        "speed": 2.04,
                        "deg": 18,
                        "gust": 3.8
                    },
                    "visibility": 10000,
                    "pop": 0,
                    "sys": {
                        "pod": "n"
                    },
                    "dt_txt": "2023-10-25 00:00:00"
                },

                {
                    "dt": 1698278400,
                    "main": {
                        "temp": -0.96,
                        "feels_like": -4.32,
                        "temp_min": -0.96,
                        "temp_max": -0.96,
                        "pressure": 1020,
                        "sea_level": 1020,
                        "grnd_level": 1001,
                        "humidity": 76,
                        "temp_kf": 0
                    },
                    "weather": [
                        {
                            "id": 803,
                            "main": "Clouds",
                            "description": "облачно с прояснениями",
                            "icon": "04n"
                        }
                    ],
                    "clouds": {
                        "all": 62
                    },
                    "wind": {
                        "speed": 2.65,
                        "deg": 95,
                        "gust": 6.36
                    },
                    "visibility": 10000,
                    "pop": 0,
                    "sys": {
                        "pod": "n"
                    },
                    "dt_txt": "2023-10-26 00:00:00"
                },

                {
                    "dt": 1698364800,
                    "main": {
                        "temp": -1.53,
                        "feels_like": -7.03,
                        "temp_min": -1.53,
                        "temp_max": -1.53,
                        "pressure": 1014,
                        "sea_level": 1014,
                        "grnd_level": 995,
                        "humidity": 70,
                        "temp_kf": 0
                    },
                    "weather": [
                        {
                            "id": 801,
                            "main": "Clouds",
                            "description": "небольшая облачность",
                            "icon": "02n"
                        }
                    ],
                    "clouds": {
                        "all": 17
                    },
                    "wind": {
                        "speed": 5.34,
                        "deg": 87,
                        "gust": 12.76
                    },
                    "visibility": 10000,
                    "pop": 0,
                    "sys": {
                        "pod": "n"
                    },
                    "dt_txt": "2023-10-27 00:00:00"
                },

                {
                    "dt": 1698451200,
                    "main": {
                        "temp": -1.08,
                        "feels_like": -6.6,
                        "temp_min": -1.08,
                        "temp_max": -1.08,
                        "pressure": 1010,
                        "sea_level": 1010,
                        "grnd_level": 991,
                        "humidity": 94,
                        "temp_kf": 0
                    },
                    "weather": [
                        {
                            "id": 600,
                            "main": "Snow",
                            "description": "небольшой снег",
                            "icon": "13n"
                        }
                    ],
                    "clouds": {
                        "all": 100
                    },
                    "wind": {
                        "speed": 5.58,
                        "deg": 112,
                        "gust": 12.56
                    },
                    "visibility": 279,
                    "pop": 1,
                    "snow": {
                        "3h": 1.12
                    },
                    "sys": {
                        "pod": "n"
                    },
                    "dt_txt": "2023-10-28 00:00:00"
                }

            ],
            "city": {
                "id": 524901,
                "name": "Москва",
                "coord": {
                    "lat": 55.7522,
                    "lon": 37.6156
                },
                "country": "RU",
                "population": 1000000,
                "timezone": 10800,
                "sunrise": 1698034530,
                "sunset": 1698070324
            }
        }

        response = forecast.data_processing_for_five_days(json)
        assert not validate(response, schema)
