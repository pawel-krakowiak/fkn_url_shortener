from django.contrib import admin
from django.urls import path
from .views import display_grabber

urlpatterns = [
    path('', display_grabber, name='index'),
    path('create', create, name='create')
]
