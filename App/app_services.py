import requests
import json
import datetime
from config import API_KEY_WEATHER


class ForecastWeather:
    def __init__(self, city):
        self.city = city

    def get_forecast_for_today(self) -> dict:
        """
        Gets forecast data for the requested city for the current time.
        :param: str
        :return: dict. Example {"clouds": "98", }
        """
        request_for_today = self.request_to_api_forecast(
            f'https://api.openweathermap.org/data/2.5/weather?q={self.city}&units'
            f'=metric&lang=ru&appid={API_KEY_WEATHER}')

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

    def get_forecast_for_five_days(self) -> dict:
        """
        Gets forecast data for the requested city for 5 days.
        :param: str
        :return: dict. Example {"2023-07-31": [18, 24, "переменная облачность"], }
        """
        request_for_five_days = self.request_to_api_forecast(
            f'https://api.openweathermap.org/data/2.5/forecast?q={self.city}&units'
            f'=metric&lang=ru&appid={API_KEY_WEATHER}')
        forecast_for_five_days = {}
        for part_day in range(len(request_for_five_days['list'])):
            one_full_day = (str(request_for_five_days['list'][part_day]['dt_txt']))[:10]
            weather_description = str(request_for_five_days['list'][part_day]['weather'][0]['description'])
            temp_min = round(request_for_five_days['list'][part_day]['main']['temp_min'])
            temp_max = round(request_for_five_days['list'][part_day]['main']['temp_max'])

            if one_full_day not in forecast_for_five_days.keys():
                forecast_for_five_days[one_full_day] = [100, -100, weather_description, one_full_day]
            if forecast_for_five_days[one_full_day][0] > temp_min:
                forecast_for_five_days[one_full_day][0] = temp_min
            if forecast_for_five_days[one_full_day][1] < temp_max:
                forecast_for_five_days[one_full_day][1] = temp_max

        rename_keys = ['day', 'day_1', 'day_2', 'day_3', 'day_4', 'day_5']
        forecast_for_five_days = dict(zip(rename_keys, list(forecast_for_five_days.values())))

        return forecast_for_five_days

    @staticmethod
    def request_to_api_forecast(url) -> json:
        """
        Requests the weather forecast in the API service(OpenWeatherMap).
        :param: str
        :return: json
        """
        if requests.get(url).status_code == 200:
            return json.loads(requests.get(url).text)
        raise ValueError()
