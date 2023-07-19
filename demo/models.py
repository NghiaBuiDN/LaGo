from django.db import models
from django import forms

# Create your models here.
class DemoUser(models.Model):
    id = models.AutoField(primary_key=True)
    userName = models.CharField(max_length=50, blank=False)
    passWord = models.CharField(max_length=50, blank=False)

class Sum(models.Model):
    so_a = models.CharField(max_length=255)
    so_b = models.CharField(max_length=255)

class ExampleForm(forms.Form):
    user_name = forms.CharField(label="User name", max_length=100)
    password = forms.CharField(label="Password", widget= forms.PasswordInput)
    remember = forms.BooleanField(label="Remember me")
