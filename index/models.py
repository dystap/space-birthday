from django.db import models

class info(models.Model):
    month = models.IntegerField()
    date = models.IntegerField()
    name = models.CharField()
    videoPhoto = models.URLField()
    description = models.TextField()
    credit = models.CharField()






