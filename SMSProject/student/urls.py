from django.urls import path
from .views import contact, delete, display, home,register,login, update

urlpatterns = [
    path('',home,name='home'),
    path('register/',register,name='reg'),
    path('login/',login,name='login'),
    path('display/',display,name='display'),
    path('update/<int:id>/',update,name='update'),
    path('delete/<int:id>/',delete,name='delete'),
    path('contact/',contact,name='contact'),
]
