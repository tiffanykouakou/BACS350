from django.urls import path
from hero.views import HulkView, SpiderManView, WonderWomanView

urlpatterns = [
    path('hulk', HulkView.as_view()),
    path('wonderwoman', WonderWomanView.as_view()),
    path('spiderman', SpiderManView.as_view()),
]