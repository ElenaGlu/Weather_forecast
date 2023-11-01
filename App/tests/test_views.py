from django.test import TestCase
from django.urls import reverse


class ViewsTests(TestCase):

    def test_loading_search_page(self):
        """
        Requests a html page and checks its status code and the correctness of the template.
        """
        response = self.client.get(reverse("loading_search_page"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "App/base.html")

    def test_displays_weather_forecast_in_the_city(self):
        """
        Requests a html page with city and checks its status code and the correctness of the template.
        """
        response = self.client.post(reverse("displays_weather_forecast_in_the_city"), {'city': 'Москва'})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "App/weather_forecast.html")