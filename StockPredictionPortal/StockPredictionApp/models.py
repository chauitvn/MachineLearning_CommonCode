from django.db import models

class Configuration(models.Model):
    key = models.CharField(max_length=50, blank=True)
    value = models.CharField(max_length=200, blank=True)
    HasActive = models.BooleanField()