from django.contrib import admin
from django.contrib.admin import site
from django.urls import path
from django.views.generic import RedirectView
from hero.views import IndexView, SuperheroListView, SuperheroDetailView, SuperheroCreateView,SuperheroUpdateView, SuperheroDeleteView, SignupView
from hero.views_article import ArticleDeleteView, ArticleDetailView, ArticleListView, ArticleCreateView, ArticleUpdateView
from django.conf import settings
from django.urls.conf import include, include
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view()),
    path('superhero/', SuperheroListView.as_view(), name = 'superhero_list'),
    path('superhero/<int:pk>', SuperheroDetailView.as_view(), name='superhero_details'),
    path('superhero/add', SuperheroCreateView.as_view(), name='superhero_add'),
    path('superhero/<int:pk>/edit', SuperheroUpdateView.as_view(), name = 'superhero_edit'),
    path('superhero/<int:pk>/delete', SuperheroDeleteView.as_view(), name='Superhero_delete'),
    path(r'admin/', site.urls),
    path('signin/', SignupView.as_view()),

    # User account urls
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('accounts.urls')),
    path('', RedirectView.as_view(url='accounts/'), name='home'),

    # Article
    path('article/', ArticleListView.as_view(), name='article_list'),
    path('article/<int:pk>', ArticleDetailView.as_view(), name='article_detail'),
    path('article/add', ArticleCreateView.as_view(), name='article_add'),
    path('article/<int:pk>/', ArticleUpdateView.as_view(), name='article_edit'),
    path('article/<int:pk>/delete',
         ArticleDeleteView.as_view(),  name='article_delete'),
] 