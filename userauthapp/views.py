from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User
from datetime import datetime
from userauthapp.models import Register
from django.contrib import messages
from django.contrib.auth import authenticate, login , logout


# Create your views here.
def index(request):
    if request.User.is_anonymous:
        return redirect('user/register/')
    return render(request ,'index.html')


def register(request):
    if request.method=="POST":
        username= request.POST.get("username")
        fistname=request.POST.get("firstName")
        LastName=request.POST.get("Lastname")
        password1=request.POST.get("password1")
        password2=request.POST.get("password2")
        email=request.POST.get("email")
        if password1!=password2:
            messages.info(request, "password mismatch")
            print("password mismatch")
        user=Register(username=username,fistname=fistname,LastName=LastName,password=password1,email=email,date=datetime.today())
        user.save()
        messages.success(request, "you have been registered")
        return render(request,"index.html")


def loginUser(request):
    if request.method=="POST":
        username= request.POST.get("username")
        password=request.POST.get("password")
        #check if user have entered correct credentials
        user = authenticate(username= username, password=password)
        print(request.user)
        if User is not None:
            login(request,user)
            return redirect('user/login/')
        else:
            print("error ho gyi babu")
            #return render(request ,'login.html')

    return render(request ,'login.html')

def logoutUser(request):
    logout(request)
    return redirect('user/login/')