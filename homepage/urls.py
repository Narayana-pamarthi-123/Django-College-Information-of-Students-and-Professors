from django.contrib.auth.views import LogoutView
from django.urls import path

from .views import  signup, login, logout, home

urlpatterns = [
    path('', home, name='home'),
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    path('signup/', signup, name='signup'),
]