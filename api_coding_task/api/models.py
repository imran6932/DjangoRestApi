from django.db import models
from django.db import models

class Student(models.Model):
    '''Student Model '''
    name = models.CharField(max_length=100)
    roll = models.PositiveIntegerField()
    city = models.CharField(max_length=100)
    

