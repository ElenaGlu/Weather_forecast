from django.test import SimpleTestCase
from django.urls import reverse
from django.test import Client


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


