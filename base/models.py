from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Report(models.Model):
    location1 = models.CharField(max_length=20)
    location2 = models.CharField(max_length= 50)
    description = models.TextField( max_length= 100)
    security = models.CharField(max_length= 50)
    cause = models.CharField(max_length= 50)
    action = models.CharField(max_length= 50)
    type_env = models.CharField(max_length=20)
    type_inju = models.CharField(max_length=20)
    type_property = models.CharField(max_length=20)
    type_vehicle = models.CharField(max_length=20)
    submitted = models.CharField(max_length=20)



