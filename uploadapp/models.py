from django.db import models
from django.urls import reverse

class Course(models.Model):
    id = models.AutoField(primary_key=True)
    author = models.CharField(max_length=250)
    title = models.CharField(max_length=250)
    image = models.ImageField(upload_to='images/')
    document = models.FileField(upload_to='uploads/')