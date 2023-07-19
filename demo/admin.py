from django.contrib import admin

# Register your models here.

from .models import DemoUser, Sum
@admin.register(DemoUser)
class DemoUserAdmin(admin.ModelAdmin):
    list_display = ["id", "userName", "passWord"]
    list_display_links = ["userName", "passWord"]
    list_per_page = 1
    list_filter = ["userName"]
@admin.register(Sum)
class SumAdmin(admin.ModelAdmin):
    list_display = ["so_a" , "so_b"]
    list_display_links = ["so_a" , "so_b"]