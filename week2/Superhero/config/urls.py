from django.urls import path
from pages.views import AboutView

urlpatterns = [
    path('hulk', IndexView.as_view()),
    path('ironman', AboutView.as_view()),
    path('Blackwidow', HomeView.as_view()),
]