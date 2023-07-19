from django.db import models
from django.urls import reverse

class Customer(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=250, db_index=True)
    phone = models.CharField(max_length=250, unique=True)
    address = models.CharField(max_length=250)
    city = models.CharField(max_length=250)
    state = models.CharField(max_length=250)
    date_added = models.DateTimeField(auto_now_add=True)
    def __str__(self):
	    return str(self.id)



	


    