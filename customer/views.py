from django.shortcuts import render, redirect
from django.http import HttpRequest,HttpResponse
from django.shortcuts import get_object_or_404
from .models import Customer
from django.http import JsonResponse
from django.core.paginator import Paginator
from django.contrib.postgres.search import SearchVector
from cart.cart import Cart
from store.models import Product, Order

from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializer import CustomerSerializer
from decimal import Decimal
# Create your views here.


def list_customer(request):
    list_customer = Customer.objects.all()
    paginator = Paginator(list_customer,10)  # Show 25 contacts per page.
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request,"customer/list-customer.html",{"page_obj": page_obj})

def add_customer(request):
    return render(request,"customer/add-customer.html")

def add_new_customer(request):
    cart = Cart(request)
    if request.method == "POST":
        rq_name = request.POST.get("name")
        print("-------"+rq_name)
        rq_phone = request.POST.get("phone")
        rq_address = request.POST.get("address")
        rq_city = request.POST.get("city")
        rq_state = request.POST.get("state")
        data = Customer(name = rq_name, phone = rq_phone, address = rq_address,
                        city = rq_city , state = rq_state)
        data.save()
        
        for product_id in cart:
            product = Product.objects.filter(id = product_id)
            # rq_product_name = cart.item_title()
            # rq_quantity = cart.__len__()
            # rq_total_order = cart.get_total()
            data_order = Order(customer=data, product = product,
                                quantity = cart[product_id]["qty"], total_order = 0)
            data_order.save()

    customer_list = Customer.objects.all()
    paginator = Paginator(customer_list, 10)  
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    
    return render(request, "customer/payment.html", {"page_obj": page_obj},)
    

def update_customer(request,customer_id):
    customer = get_object_or_404(Customer, id = customer_id)
    context = {'customer' : customer}
    return render(request,"customer/update-customer.html",context)

def update_process(request):
    if request.method == "POST":
        rq_id = request.POST.get("customer_id")
        rq_name = request.POST.get("name")
        rq_phone = request.POST.get("phone")
        rq_address = request.POST.get("address")
        rq_city = request.POST.get("city")
        rq_state = request.POST.get("state")
        Customer.objects.filter(id=rq_id).update(name = rq_name, phone = rq_phone,
                                                address = rq_address, city = rq_city , state = rq_state)
        all_customer = Customer.objects.all()
        context = {'all_customer':all_customer}
        return render(request,"customer/list-customer.html",context)
    
def delete_customer(request):
    if request.method == "GET":
        rq_id = request.GET['customer_id']
        Customer.objects.get(id=rq_id).delete()
        context = {'mess':'Xóa đã thành công'}
    return JsonResponse(context)

def search_customer(request):
    if request.method == "POST":
        searched = request.POST['searched']

        list_customer = Customer.objects.filter(name__contains=searched)
        paginator = Paginator(list_customer,5)  # Show 25 contacts per page.
        page_number = request.GET.get("page")
        page_obj = paginator.get_page(page_number)
        data = {'searched':searched,"page_obj": page_obj}

        return render(request,"customer/search-customer.html",data)
    else:
        return render(request,"customer/list-customer.html")
    

    
@api_view(['GET'])
def getCustomer(request):
    customer = Customer.objects.all()
    serializer = Customer(customer, many=True)
    return Response(serializer.data)
@api_view(['POST'])
def postCustomer(request):
    serializer = CustomerSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

    