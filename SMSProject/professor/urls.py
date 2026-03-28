from django.urls import path
from .views import display, register

app_name = 'professor'

urlpatterns=[
    path('register/',register,name='register'),
#     path('prof-login',login,name='prof-login'),
    path('display/',display,name='display'),
]
