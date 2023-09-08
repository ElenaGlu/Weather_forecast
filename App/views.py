from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from .app_services import ForecastWeather
from .forms import PlaceForm


def loading_search_page(request: HttpRequest) -> HttpResponse:
    """
    Loads the starting html page.
    :param request: http request
    :return: HTML page with string 'search city'
    """
    return render(request, 'App/base.html')


def displays_weather_forecast_in_the_city(request: HttpRequest) -> HttpResponse:
    """
    Displays the weather forecast for the city request from the form.
    :param request: http request
    :return: HTML page with forecast for today and for five day
    """
    if request.method == 'POST':
        form = PlaceForm(request.POST)
        if form.is_valid():
            city = form.cleaned_data["city"]
            forecast = ForecastWeather(city)
            forecast_for_today = forecast.get_forecast_for_today()
            forecast_for_five_days = forecast.get_forecast_for_five_days()

            return render(request, 'App/weather_forecast.html', {'forecast_for_today': forecast_for_today,
                                                                 'forecast_for_five_days': forecast_for_five_days})

        raise ValueError()

