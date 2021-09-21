from django.contrib import admin
from django.urls import path
from hero.views import IndexView, HeroListView, HeroDetailView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view()),
    path('hero/', HeroListView.as_view()),
    path('hero/<int:pk>', HeroDetailView.as_view()),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)