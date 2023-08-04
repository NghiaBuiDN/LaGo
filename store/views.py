from django.shortcuts import render
from django.http import HttpRequest,HttpResponse
from .models import Product
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url = "login")

def home(request):
    return render(request,"store/index.html")

def aboutus(request):
    return render(request,"store/about.html")

def home(request):
    all_product = Product.objects.all()
    context = {'my_product':all_product}
    return render(request,"store/index.html", context)


def product_info(request, product_slug):
    product = get_object_or_404(Product,slug = product_slug)
    all_product = Product.objects.all()
    context = {'product':product,'my_product':all_product}
    return render(request, "store/product-info.html",context)


def search_product(request):
    if request.method == "POST":
        searched = request.POST['searched']

        list_product = Product.objects.filter(title__contains=searched)
        paginator = Paginator(list_product,10)  # Show 25 contacts per page.
        page_number = request.GET.get("page")
        page_obj = paginator.get_page(page_number)
        data = {'searched':searched,"page_obj": page_obj}

        return render(request,"store/search-product.html",data)
    else:
        return render(request,"customer/index.html")
    
def bathbomb(request):
    searched = 'Bubble Bath Bomb'
    list_product = Product.objects.filter(brand__contains= searched)
    paginator = Paginator(list_product,10)  # Show 25 contacts per page.
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    data = {'searched':searched,"page_obj": page_obj}

    return render(request,"store/search-product.html",data)

def salts(request):
    searched = 'salts'
    list_product = Product.objects.filter(brand__contains= searched)
    paginator = Paginator(list_product,10)  # Show 25 contacts per page.
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    data = {'searched':searched,"page_obj": page_obj}

    return render(request,"store/search-product.html",data)

def soap(request):
    searched = 'soap'
    list_product = Product.objects.filter(brand__contains= searched)
    paginator = Paginator(list_product,10)  # Show 25 contacts per page.
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    data = {'searched':searched,"page_obj": page_obj}

    return render(request,"store/search-product.html",data)

def fizzy(request):
    searched = 'fizzy'
    list_product = Product.objects.filter(brand__contains= searched)
    paginator = Paginator(list_product,10)  # Show 25 contacts per page.
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    data = {'searched':searched,"page_obj": page_obj}

    return render(request,"store/search-product.html",data)

    
