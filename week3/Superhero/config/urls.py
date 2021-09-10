from django.urls import path
from hero.views import HomeView, HulkView, SpiderManView, WonderWomanView, HomeView

urlpatterns = [
    path('', HomeView.as_view()),
    path('hulk', HulkView.as_view()),
    path('wonderwoman', WonderWomanView.as_view()),
    path('spiderman', SpiderManView.as_view()),
]