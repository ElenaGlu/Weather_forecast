import requests
import json
import datetime

from typing import Callable


class ForecastWeather:
    def __init__(self, city):
        self.city = city

    def choose_forecast(self, url: str, forecast_method: Callable) -> dict:
        """
        Choosing a forecast for today or 5 days
        :param: url, forecast_method - gets forecast data for the requested city
        :return: dict. Example {"clouds": "98", }
        """
        return forecast_method(self.request_to_api_forecast(url))

    @staticmethod
    def request_to_api_forecast(url: str) -> json:
        """
        Requests the weather forecast in the API service(OpenWeatherMap).
        :param: url
        :return: json
        """
        resp = requests.get(url)
        if resp.status_code == 200:
            return resp.json()
        raise ValueError('Данный город не найден, попробуй другой, дружок')

    def forecast_data_preparation_today(self, request_for_today: json) -> dict:
        """
        Gets forecast data for the requested city for the current time.
        :param: request_for_today - json response
        :return: dict. Example {"clouds": "98", }
        """
        forecast_for_today = {'city': self.city, 'conditions': request_for_today['weather'][0]['description'],
                              'temperature': round(request_for_today['main']['temp']),
                              'temperature_feels': round(request_for_today['main']['feels_like']),
                              'clouds': round(request_for_today['clouds']['all']),
                              'pressure': round((request_for_today['main']['pressure']) / 1.333),
                              'humidity': round(request_for_today['main']['humidity']),
                              'visibility': round(request_for_today['visibility']),
                              'wind_speed': round(request_for_today['wind']['speed']),
                              'sunrise_timestamp': datetime.datetime.fromtimestamp(request_for_today["sys"]["sunrise"]),
                              'sunset_timestamp': datetime.datetime.fromtimestamp(request_for_today["sys"]["sunset"])}
        return forecast_for_today

    @staticmethod
    def forecast_data_preparation(request_for_five_days: json) -> dict:
        """
        Gets forecast data for the requested city for 5 days.
        :param: request_for_five_days - json response
        :return: dict. Example {"2023-07-31": [18, 24, "переменная облачность", "2023-09-08"], }
        """
        forecast_for_five_days = {}
        temp_min_buff = 100
        temp_max_buff = -100
        for part_day in range(len(request_for_five_days['list'])):
            one_full_day = (str(request_for_five_days['list'][part_day]['dt_txt']))[:10]
            weather_description = str(request_for_five_days['list'][part_day]['weather'][0]['description'])
            temp_min = round(request_for_five_days['list'][part_day]['main']['temp_min'])
            temp_max = round(request_for_five_days['list'][part_day]['main']['temp_max'])

            if one_full_day not in forecast_for_five_days.keys():
                forecast_for_five_days[one_full_day] = [
                    min(temp_min_buff, temp_min),
                    max(temp_max_buff, temp_max),
                    weather_description,
                    one_full_day
                ]
                temp_min_buff = forecast_for_five_days[one_full_day][0]
                temp_max_buff = forecast_for_five_days[one_full_day][1]

        rename_keys = ['day', 'day_1', 'day_2', 'day_3', 'day_4', 'day_5']
        forecast_for_five_days = dict(zip(rename_keys, list(forecast_for_five_days.values())))

        return forecast_for_five_days
