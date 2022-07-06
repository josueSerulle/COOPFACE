from unicodedata import name
from django.urls import path,include

from .views import HomeView, LoginView

urlpatterns = [
    path('', HomeView.index, name='coop_virtual'),
    path('login', LoginView.loginForm, name ='login'),
    path('login_post', LoginView.login, name ='login_post'),
]