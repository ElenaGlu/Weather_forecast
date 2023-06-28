from django.shortcuts import render

from .forms import PlaceForm
from .app_services import get_data_about_city


def search_place(request):
    return render(request, 'App/base.html')


def get_place(request):
    if request.method == 'POST':
        dict1 = get_data_about_city()
        return render(request, 'App/weather_forecast.html', dict1)
    return render(request, 'App/base.html')
