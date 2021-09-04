from week2.Hello.pages.views import HomeView
from django.urls import path
from pages.views import AboutView

urlpatterns = [
    path('', AboutView.as_view()),
    path('about', AboutView.as_view()),
    path('home', HomeView.as_view()),
]