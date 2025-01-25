
from django.urls import path
from .views import hello_world, post_data, get_countries, post_country_population

urlpatterns = [
    path('', hello_world),
    path('hello/', hello_world),
    path('postdata', post_data),
    path('countries', get_countries),
    path('country-population', post_country_population),

]