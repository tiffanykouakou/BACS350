from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic import ListView
from .models import Superhero

class IndexView(TemplateView):
    template_name = 'Index.html'

class SuperheroListView(ListView):
    model = Superhero
    template_name = 'superhero_list.html'

class SuperheroDetailView(TemplateView):
    model = Superhero
    template_name = 'superhero_detail.html'

    def get_context_data(self, **kwargs):
        hero_id = kwargs['pk']
        hero = Hero.objects.get(pk=hero_id)
        return {'superhero': superhero}