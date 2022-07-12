from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.display_grabber, name='index'),
    path('create', views.create, name='create'),
    path('<str:pk>', views.go, name='go')
]
