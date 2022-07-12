from django.shortcuts import render, redirect
import uuid
from django.http import HttpResponse
from .models import URLGrab


def display_grabber(request):
    return render(request, 'grabber_index.html')


def create(request):
    if request.method == 'POST':
        link = request.POST['link']
        uid = str(uuid.uuid4())[:5]
        new_url = URLGrab(link=link, uuid=uid)
        new_url.save()
        return HttpResponse(uid)

def go(request, pk):
    url_details = URLGrab.objects.get(uuid=pk)
    return redirect(url_details.link)