from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.views.generic import ListView, CreateView, DeleteView, DetailView, RedirectView, UpdateView
from .models import Superhero
from .models import Hero

class superheroView(RedirectView):
    url = '/superhero/'

class IndexView(TemplateView):
    template_name = 'Index.html'

class SuperHeroListView(ListView):
    model = Superhero
    template_name = 'superhero_list.html'

class SuperHeroDetailView(DetailView):
    model = Superhero
    template_name = 'superhero_detail.html'

class SuperheroCreateView(CreateView):
    model = Superhero
    template_name = 'superhero_new.html'
    fields = ['name', 'identity', 'description', 'strength', 'weakness', 'image']

class SuperheroUpdateView(UpdateView):
    model = Superhero
    template_name = 'superhero_edit.html'
    fields = ['name', 'identity', 'description', 'strength', 'weakness', 'image']
    success_url = reverse_lazy('templates/superhero_list')

class SuperheroDeleteView(DeleteView):
    model = Superhero
    template_name = 'superhero_delete.html'
    success_url = reverse_lazy('templates/superhero_list')

class SigninView(TemplateView):
    model = Superhero
    template_name = 'signup.html'