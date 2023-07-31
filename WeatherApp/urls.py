from django.contrib import admin
from django.urls import path

from App import views

urlpatterns = [
    path('', views.loading_search_page, name='loading_search_page'),
    path('city/', views.displays_weather_forecast_in_the_city, name='displays_weather_forecast_in_the_city'),
    path('admin/', admin.site.urls),
]
