from django.shortcuts import render

from .app_services import get_data_about_city
from .forms import PlaceForm


def search_place(request):
    return render(request, 'App/base.html')


def get_place(request):
    if request.method == 'POST':
        form = PlaceForm(request.POST)
        if form.is_valid():
            city = form.cleaned_data["city"]
            full_forecast = get_data_about_city(city)
            return render(request, 'App/weather_forecast.html', full_forecast)
        else:
            return render(request, 'App/base.html')
