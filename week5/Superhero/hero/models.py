from django.db import models

class Hero (models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.name}'

class Superhero(models.Model):
    name = models.CharField(max_length=20)
    identity = models.CharField(max_length=200)
    image = models.CharField(max_length=200, default= "image")

    def __str__(self):
        return f'{self.name}'