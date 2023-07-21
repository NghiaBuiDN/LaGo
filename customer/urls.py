from django.contrib import admin
from django.urls import path
from customer import views
from .views import export_customer_csv

urlpatterns = [
    path('addcus',views.add_customer, name = "addcus"),
    path('',views.list_customer, name = "list_customer"),
    path('payment',views.add_new_customer, name = "add_new_customer"),
    path('update_customer/<int:customer_id>/',views.update_customer, name = "update_customer"),
    path('update_process/',views.update_process, name = "update_process"),
    path('delete_customer/',views.delete_customer, name = "delete_customer"),
    path('search_customer/',views.search_customer, name = "search_customer"),
    path('get_customer/',views.getCustomer, name = "get_customer"),
    path('post/',views.postCustomer, name = "postCustomer"),
    path('export', export_customer_csv, name='export_customer_csv'),
]
