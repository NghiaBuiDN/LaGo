from django.contrib import admin
from django.urls import path
from accounts import views

urlpatterns = [
    path('',views.login, name = "login"),
    path('process_login',views.process_login, name = "process_login"),
    path('process_logout',views.process_logout, name = "process_logout"),
    path('register',views.register, name = "register"),
    path('process_regis',views.process_regis, name = "process_regis"),


]