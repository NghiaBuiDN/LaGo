from django.contrib import admin
from django.urls import path
from uploadapp import views

urlpatterns = [
    path('', views.upload_app, name="upload_app"),
    path('uploadapp/upload/', views.upload, name='upload')
]