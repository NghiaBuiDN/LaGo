from django.contrib import admin
from django.urls import path
from store import views

urlpatterns = [
    path('', views.home, name="store"),
    path('product/<slug:product_slug>/',views.product_info,name="product-info"),
    path('search_product',views.search_product,name="search_product"),
    path('aboutus',views.aboutus,name="aboutus"),
    path('bathbomb',views.bathbomb,name="bathbomb"),
    path('fizzy',views.fizzy,name="fizzy"),
    path('salts',views.salts,name="salts"),
    path('soap',views.soap,name="soap"),
    
]
