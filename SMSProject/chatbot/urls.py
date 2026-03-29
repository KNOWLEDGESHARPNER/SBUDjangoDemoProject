from django.urls import path
from . import views

urlpatterns = [
    path('', views.chat_home, name='chat_home'),
    path('api/response/', views.chat_response, name='chat_response'),
    path('api/history/', views.chat_history, name='chat_history'),
]
