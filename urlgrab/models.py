from django.db import models
from urllib.parse import urlparse

class URLGrab(models.Model):
    shorted_url = models.CharField(max_length=300, default="http://127.0.0.8:8000/shorter")
    link = models.CharField(max_length=10000)
    uuid = models.CharField(max_length=10)
    stored_time = models.DateTimeField(auto_now=True, editable=False)

    def __str__(self):
        net_location = urlparse(self.link).netloc
        return f"[{self.id}]: {net_location}"