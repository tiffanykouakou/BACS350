from django.db import models
from django.urls.base import reverse_lazy

class Hero (models.Model):
    name = models.CharField(max_length=20)
    identity = models.CharField(max_length=200, default = "--")
    description = models.TextField(default= "--")
    strength = models.CharField(max_length=500, default= "--")
    weakness = models.CharField(max_length=500, default= "--")
    image = models.CharField(max_length=200, default= "image")


    def __str__(self):
        return f'{self.name}'

class Superhero(models.Model):
    name = models.CharField(max_length=20)
    identity = models.CharField(max_length=200, default= "--")
    description = models.TextField(default= "--")
    strength = models.CharField(max_length=500, default= "--")
    weakness = models.CharField(max_length=500, default= "--")
    image = models.CharField(max_length=200, default= "image")
   
    def __str__(self):
        return f'{self.name}'

    def get_absolute_url(self):
        return reverse_lazy('superhero_detail')