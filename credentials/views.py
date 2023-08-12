from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.template.defaulttags import csrf_token

def login(request):

    if  request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"Invalid login")
            return redirect('login')


    return render(request,'login.html')
# Create your views here.
def register(request):

    if request.method=='POST':
        username=request.POST['username']
        first_name=request.POST['first_name']
        second_name=request.POST['second_name']
        email=request.POST['email']
        password=request.POST['psw']
        cpassword=request.POST['psw-repeat']
        if password==cpassword:
            if User.objects.filter(username=username).exists():

                messages.info(request,"User name already exists")
                return redirect('register')
                #print(request,"user error")
            elif User.objects.filter(email=email).exists():
                messages.info(request,"Email already exists")
                return redirect('register')
            else:

                 user=User.objects.create_user(username=username,first_name=first_name,last_name=second_name,email=email, password=password)
                 user.save();
                 return redirect('login')
                 #messages.info(request,"user created")
        else:

            messages.info(request,"Incorrect password")
            return redirect('register')
        return redirect('/')

    return render(request, "register.html")

def logout(request):
    auth.logout(request)
    return redirect('/')