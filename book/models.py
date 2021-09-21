from django.db import models
from django.db.models.base import Model

# Create your models here.
class Book(models.Model):
    author = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    discription = models.CharField(max_length=1000)
    date_publ = models.CharField(max_length=50)

    def __str__(self):
        return self.author    
    