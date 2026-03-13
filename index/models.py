from django.db import models

class info(models.Model):
    month = models.IntegerField()
    date = models.IntegerField()
    name = models.CharField()
    video = models.URLField()
    photo = models.URLField()
    description = models.TextField()
    credit = models.CharField()






