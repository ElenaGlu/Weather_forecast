import json

import pytest

from django.urls import reverse
from rest_framework.test import APIClient


def test_loading_search_page(client):
    response = client.get(reverse('loading_search_page'))
    assert response.status_code == 200


def test_displays_weather_forecast_in_the_city():
    client = APIClient()
    url = reverse('displays_weather_forecast_in_the_city')
    city = {'city': 'Москва'}
    response = client.post(url, city=city)
    assert response.status_code == 200


def test_request_to_api_forecast():
    content = json.loads(response.content)
    assert 'result' in content
    assert content['result'] == 'ok'
