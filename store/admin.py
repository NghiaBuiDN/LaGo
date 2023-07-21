from django.contrib import admin
from .models import Category, Product, Order, Customer

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug' : ('name',)}

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug' : ('title',)}
    list_display = ['id', 'title' , 'brand', 'category', 'price', 'description', 'image' ]

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'customer' , 'date_ordered', 'product', 'quantity','total_order','complete']


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['id', 'name' , 'phone', 'address', 'city','state','date_added']

