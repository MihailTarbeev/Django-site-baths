from django.db import models

# Create your models here.


class Bath(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    time_open = models.TimeField()
    time_close = models.TimeField()
    is_opened = models.BooleanField(default=True)
