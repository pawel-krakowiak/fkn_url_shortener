from django.shortcuts import render
from .models import URLGrab


def display_grabber(request):
    return render(request, 'grabber_index.html')