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
        return reverse_lazy('superhero_detail', args =[str(self.id)])

class Article(models.Model):
    # pointer to Superhero object
    hero = models.CharField(max_length=20, default='none')
    order = models.IntegerField()  # superhero order
    # title text of the superhero
    title = models.CharField(max_length=200)
    markdown = models.TextField()  # markdown text
    html = models.TextField()

    def export_record(self):
        return [self.hero, self.order, self.title]

    @staticmethod
    def import_record(values):
        c = Article.objects.get_or_create(hero=values[0], order=values[1])[0]
        c.title = values[2]
        c.save()

    def __str__(self):
        return f'{self.hero.title} - {self.order} - {self.title}'