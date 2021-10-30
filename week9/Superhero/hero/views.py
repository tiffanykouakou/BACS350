from django.contrib.auth.mixins import LoginRequiredMixin
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

    def get_context_data(self, **kwargs):
        hero_id = kwargs['pk']
        hero = Superhero.objects.get(pk=hero_id)
        return {'hero': hero}


class SuperheroCreateView(LoginRequiredMixin, CreateView):
    model = Superhero
    template_name = 'superhero_new.html'
    fields = ['name', 'identity', 'description', 'strength', 'weakness', 'image']

class SuperheroUpdateView(LoginRequiredMixin, UpdateView):
    model = Superhero
    template_name = 'superhero_edit.html'
    fields = ['name', 'identity', 'description', 'strength', 'weakness', 'image']

class SuperheroDeleteView(LoginRequiredMixin, DeleteView):
    model = Superhero
    template_name = 'superhero_delete.html'
    success_url = reverse_lazy('superhero_list')

class SignupView(TemplateView):
    model = Superhero
    template_name = 'signup.html'
   