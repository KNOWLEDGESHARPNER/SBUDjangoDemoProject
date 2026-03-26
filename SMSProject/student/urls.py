from django.urls import path
from .views import display, home,register,login

urlpatterns = [
    path('',home,name='home'),
    path('register/',register,name='reg'),
    path('login/',login,name='login'),
    path('display/',display,name='display'),
]
