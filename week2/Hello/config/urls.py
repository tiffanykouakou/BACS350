
from django.urls import path
from pages.views import AboutView

urlpatterns = [
    path('', AboutView.as_view()),
]