from django.shortcuts import render,redirect
from django.contrib import auth, messages
from django.contrib.auth import logout, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth.models import User


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
    return render(request,"accounts/register.html") 

def process_regis(request):
    if request.method == "POST":
        username = request.POST["userName"]
        password = request.POST["password"]
        email = request.POST["email"]
        user = User.objects.create_user(
            username = username,
            password = password,
            email = email
        )

        messages.success(request, ("Registration Successful"))

        subject = "Đăng ký tài khoản thành công - Lá Gỗ"
        mess = f'Chào mừng {user.username} đến với ngôi nhà Bath Bomb. Cám ơn bạn đã tin tưởng dùng sản phẩm của Lá Gỗ.'
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [user.email,]
        send_mail(subject, mess, email_from, recipient_list)
        return redirect('login')
    return render(request,"accounts/register.html") 