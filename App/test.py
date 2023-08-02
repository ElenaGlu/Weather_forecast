from django.test import SimpleTestCase
from django.urls import reverse  


class HomepageTests(SimpleTestCase):
    def test_loading_search_page(self):
        response = self.client.get(reverse("loading_search_page"))
        self.assertEqual(response.status_code, 200)

    def test_template_name_correct(self):  
        response = self.client.get(reverse("loading_search_page"))
        self.assertTemplateUsed(response, "App/base.html")

    def test_template_content(self):
        response = self.client.get(reverse("displays_weather_forecast_in_the_city"))
        self.assertContains(response, "<h1>Weather Forecast</h1>")
        self.assertNotContains(response, "<h1>404 Error Page</h1>")


class Tests(SimpleTestCase):
    def test_displays_weather_forecast_in_the_city(self):
        response = self.client.get(reverse("displays_weather_forecast_in_the_city"))
        self.assertEqual(response.status_code, 200)
