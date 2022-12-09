from django.db import models
from django.db.models.fields.files import ImageField
from datetime import datetime

# Create your models here.
dt = datetime.now()

class course(models.Model):
    image = models.ImageField()
    title = models.CharField(max_length=100)
    about = models.CharField(max_length=1000)
    time = models.DateTimeField(default=dt, blank=True)
    duration = models.CharField(max_length=50)
    start = models.DateField()
    payment = models.CharField(max_length=100)
    via = models.CharField(max_length=25)
    certification = models.CharField(max_length=30)

class Join(models.Model):
    name = models.CharField(max_length=50)
    interested = models.CharField(max_length=100)
    email = models.CharField(max_length=50)
    contact = models.CharField(max_length=12)
