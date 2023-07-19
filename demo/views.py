from django.shortcuts import render
from django.http import HttpRequest, HttpResponse,HttpResponseRedirect
from .models import ExampleForm
# Create your views here.

def home(request):
    form = ExampleForm()
    # if request.method == "POST":
    #     form = ExampleForm(request.POST)
    #     if form.is_valid():
    #         return HttpResponseRedirect("/info.html/")
    # else:
    #     form = ExampleForm()
    context = {'form':form}
    return render(request,"demo/index.html",context)

def login(request):
    if request.method == "POST":
        form = ExampleForm(request.POST)
        if form.is_valid():
            user = request.POST.get("user_name")
            password = request.POST.get("password")
            data = {"user":user, "password":password}
        return render(request,"demo/info.html",data)
    else:   
        form = ExampleForm()
        context = {"form":form}
        return render(request,"demo/index.html",context)

def regis(request):
    return render(request,"demo/regis.html")







# def home(request):
#     return HttpResponse('Hello Demo')

# def home(request):
#     t = tong()
#     h = hieu()
#     data = {"tong":t, "hieu":h}

#     return render(request,"demo/index.html",data)
# def tong():
#     return 1+2
# def hieu():
#     return 1-2

# def home(request):
#     # so_a = 1
#     # so_b = 2
#     # data = {"tong":t, "hieu":h}
#     t = tong()
#     h = hieu()
#     my_num = Sum.objects.all().values()
#     for i in my_num:
#         t2 = int(i['so_a']) + int(i['so_b'])
#         h2 = int(i['so_a']) - int(i['so_b'])
    
#     data = {'my_num':my_num,"tong":t, "hieu":h, "tong2":t2, "hieu2":h2}
#     return render(request,"demo/index.html",data)