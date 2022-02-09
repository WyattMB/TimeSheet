from django.db import models

# Create your models here.

class Workday(models.Model):
    user = models.CharField(max_length=60)
    #profile foreign key
    date = models.CharField(max_length=20)
    hours = models.CharField(max_length=3)