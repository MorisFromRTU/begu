from django.urls import path
from . import views

urlpatterns = [
    path('main/', views.main, name="main"),
    path('registration/', views.registration, name="registration"),
    path('login/', views.user_login, name="user_login")
]