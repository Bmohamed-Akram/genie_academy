from django.db import models
from datetime import datetime


# Create your models here.
dt = datetime.now()

class Blogp(models.Model):
    image = models.ImageField()
    title = models.CharField(max_length=100)
    body = models.CharField(max_length=100000)
    time = models.DateTimeField( default=dt, blank=True )