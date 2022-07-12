from django.contrib import admin
from urlgrab.models import URLGrab


@admin.register(URLGrab)
class URLGrabAdmin(admin.ModelAdmin):
    list_display = ['link', 'stored_time', 'uuid']

