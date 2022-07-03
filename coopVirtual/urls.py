from unicodedata import name
from django.urls import path,include

from .views import homeViews

urlpatterns = [
    path('', homeViews.index, name='coop_virtual'),
]