from django.db import models


class date(models.Model):
    date = models.CharField()
    title = models.CharField()
    description = models.TextField()
    media_url = models.URLField()