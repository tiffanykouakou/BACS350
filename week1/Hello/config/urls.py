
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
]

from django.urls import path
from pages.views import homePageView

urlpatterns = [
    path('', homePageView),
]
