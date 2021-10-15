from django.contrib import admin
from django.contrib.admin import site
from django.urls import path
from hero.views import IndexView, SuperheroListView, SuperheroDetailView, SuperheroCreateView,SuperheroUpdateView, SuperheroDeleteView, SigninView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view()),
    path('superhero/', SuperheroListView.as_view()),
    path('superhero/<int:pk>', SuperheroDetailView.as_view()),
    path('superhero/add', SuperheroCreateView.as_view()),
    path('superhero/<int:pk>/edit', SuperheroUpdateView.as_view()),
    path('superhero/<int:pk>/delete', SuperheroDeleteView.as_view()),
    path(r'admin/', site.urls),
    path('signin/', SigninView.as_view()),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)