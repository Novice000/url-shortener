from django.db import models

# Create your models here.
class Url(models.Model):
    long_url = models.URLField(max_length = 400)
    short_url = models.CharField(max_length=6, unique=True)
    clicks = models.IntegerField(default=0)
