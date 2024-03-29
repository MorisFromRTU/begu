from django.urls import path
from . import views
from django.contrib import admin

urlpatterns = [
    path('', views.main, name="main"),
    path('apply_filters/', views.apply_filters, name='apply_filters'),
    path('search_objects/', views.search_objects, name='search_objects'),
    path('registration/', views.registration, name="registration"),
    path('user_login/', views.user_login, name="user_login"),
    path('products/<int:product_id>/', views.product_detail, name='product_detail'),
]