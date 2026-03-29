from django.db import models

class info(models.Model):
    month = models.IntegerField()
    date = models.IntegerField()
    name = models.CharField()
    videoPhoto = models.URLField()
    description = models.TextField()
    credit = models.CharField()


class data(models.Model):
    date = models.CharField()
    title = models.CharField()
    description = models.TextField()
    media_url = models.URLField()


class date(models.Model):
    date = models.CharField()
    title = models.CharField()
    description = models.TextField()
    media_url = models.URLField()