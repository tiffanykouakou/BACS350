from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.views.generic import ListView, CreateView, DeleteView, DetailView, UpdateView, RedirectView
from .models import Superhero

class superheroView(RedirectView):
    url = '/superhero/'
    
class IndexView(TemplateView):
    template_name = 'Index.html'

class SuperheroListView(ListView):
    model = Superhero
    template_name = 'superhero_list.html'

class SuperheroDetailView(DetailView):
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

class SuperheroDeleteView(DeleteView):
    model = Superhero
    template_name = 'superhero_delete.html'
    success_url = reverse_lazy('superhero_list')

class SigninView(TemplateView):
    model = Superhero
    template_name = 'signup.html'
   