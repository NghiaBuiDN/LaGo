from django.shortcuts import render,redirect
from django.contrib import auth, messages
from django.contrib.auth import logout, authenticate
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def login(request):
    return render(request,"accounts/login.html") 

def process_login(request):
    if request.method == 'POST':
        username = request.POST['userName']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            if (request.user.is_authenticated):
                # return render(request,'/customer/')
                return redirect('/customer/')
        else:
            return redirect('login')

def process_logout(request):
    logout(request)
    messages.success(request, ("you were logout"))       
    return redirect('login')

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username = username , password = password)
            login(request,user)
            messages.success(request, ("Registration Successful"))
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request,"accounts/register.html",{'form':form}) 