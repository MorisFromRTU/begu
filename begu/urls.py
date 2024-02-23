from django.urls import path
from . import views
from django.contrib import admin

urlpatterns = [
    path('', views.main, name="main"),
    path('registration/', views.registration, name="registration"),
    path('user_login/', views.user_login, name="user_login"),
    path('products/<int:product_id>/', views.product_detail, name='product_detail'),
]