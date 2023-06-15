from django.shortcuts import get_object_or_404, render


def weather_forecast(request):
    return render(request, 'App/weather_forecast.html')
