from django.urls import path
from .views import display, register
urlpatterns=[
    path('reg/',register,name='reg'),
#     path('prof-login',login,name='prof-login'),
    path('display/',display,name='display'),
]
