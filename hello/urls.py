
from django.urls import path
from .views import hello_world, post_data

urlpatterns = [
    path('', hello_world),
    path('hello/', hello_world),
    path('postdata', post_data, name='post_data')

]