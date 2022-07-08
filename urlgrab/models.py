from django.db import models
from urllib.parse import urlparse

class URLGrab(models.Model):
    shorted_url = models.URLField(default="http://127.0.0.8:8000/shorter")
    direction_url = models.URLField(max_length=5000, blank=False)
    stored_time = models.DateTimeField(auto_now=True, editable=False)

    def __str__(self):
        net_location = urlparse(self.shorted_url).netloc
        return f"[{self.id}]: {net_location}"