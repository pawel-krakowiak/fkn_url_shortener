from django.contrib import admin
from urlgrab.models import URLGrab


@admin.register(URLGrab)
class URLGrabAdmin(admin.ModelAdmin):
    fields = ['shorted_url', 'direction_url']

