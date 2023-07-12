from django.shortcuts import render, redirect
from .models import loginForm
from django.contrib.auth import authenticate, login,logout
from .models import *

# Create your views here.


def indexFirst(request):
    return render(request,'Home/first.html')

def indexPage1(request):
    return render(request,'Home/page1.html')

def indexHome(request):
    return render(request,'Home/indexHome.html')


def LogoinPage(request):
    l = loginForm.objects.all()
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username=username,password=password)
        if user is not None:
            print('login complete')
            login(request,user) 
            return render(request,'Home/indexHome.html')
        else:
            print('Enter correct user or pass')
            return redirect('page1')
    else:
        print("hello")
        return redirect('page1')



def LogoutPage(request):
    logout(request)
    return redirect('page1')