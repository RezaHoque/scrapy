from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User,auth
from django.contrib.auth.decorators import login_required


# Create your views here.

def login(request):
    if request.method=='POST':
         uname=request.POST['userName']
         password=request.POST['password']

         user=auth.authenticate(username=uname,password=password)

         if user is not None:
             auth.login(request,user)
             return redirect('/')
         else:
            messages.info(request,'Authentication failed')
    else:
        return render(request,'login.html')
        
def register(request):
    if request.method=='POST':
        fname=request.POST['firstName']
        lname=request.POST['lastName']
        uname=request.POST['userName']
        email=request.POST['email']
        password=request.POST['password']
        confirmPassword=request.POST['confirmPassword']

        if password==confirmPassword:
            if User.objects.filter(username=uname).exists():
                messages.info(request,'User name taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'Email already exists')
                return redirect('register')
            else:
                user=User.objects.create_user(username=uname,password=password,email=email,first_name=fname,last_name=lname)
                user.save()
                print('user created')
                return redirect('login')
        else:
            messages.info(request,'Password does not match')
            return redirect('register')
    else:
        return render(request,'register.html')

def logout(request):
    auth.logout(request)
    return redirect('/')

@login_required(login_url='/accounts/login')
def users(request):
    users=User.objects.all
    return render(request,'users.html')
