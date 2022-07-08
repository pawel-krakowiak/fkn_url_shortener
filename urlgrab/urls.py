from django.contrib import admin
from django.urls import path
from .views import display_grabber

urlpatterns = [
    path('shortener/', display_grabber),
]
