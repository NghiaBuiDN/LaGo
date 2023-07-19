from django.contrib import admin
from django.urls import path, include
from demo import views

urlpatterns = [
    path('', views.home, name="demo"),
    path('login', views.login, name="login"),
    path('regis', views.regis, name="regis"),
    
]