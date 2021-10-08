from django.contrib import admin
from .models import Hero
from .models import Superhero

admin.site.register(Superhero)

admin.site.register(Hero)