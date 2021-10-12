from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout

def index(request):
    return render(request, 'index.html')

def login(request):
    return render(request, 'login.html')

def create_blog(request):
    return render(request, 'create_blog.html')

def read_blog(request):
    return render(request, 'read_blog.html')

def registration(request):
    if request.method =="POST":
        name =  request.POST.get('name','')
        username = request.POST.get('username','')
        email =  request.POST.get('email','')
        password = request.POST.get('password','')
        confpassword = request.POST.get('confpassword','')
        userCheck = User.objects.filter(username=username)
        if len(username)>20:
            messages.warning(request,"Too Long Username!!")
        elif password != confpassword:
            messages.warning(request,"Passwords Don't Match!!")    
        elif userCheck:
            messages.warning(request,"Username Already Exist, Kindly Change!!")   
        else:
            user_obj = User.objects.create_user(first_name=name, email=email, password=password, username=username)
            user_obj.save()
            messages.success(request,"Account Created Successfully!!")
    return render(request, 'registration.html')
