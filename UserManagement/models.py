from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    #hours = models.CharField(max_length=10)
    title = models.CharField(max_length=30)
    #image
