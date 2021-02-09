from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User,auth

# Create your views here.
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
                return redirect('/')
        else:
            messages.info(request,'Password does not match')
            return redirect('register')
    else:
        return render(request,'register.html')
