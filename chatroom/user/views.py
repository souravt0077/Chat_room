from django.shortcuts import render,redirect
from .models import User
from django.contrib import messages
from django.contrib.auth import login,logout,authenticate
# Create your views here.

def userLogin(request):
    page='login'
    if request.method == 'POST':
        Email=request.POST.get('email')
        Password=request.POST.get('password')

        try:
            user=User.objects.get(email=Email)
        except:
            messages.error(request,"Username dosn't matching...! User Authentication failed")
        
        try:
            user=User.objects.get(password=Password)
        except:
            messages.error(request,"Password dosn't matching...! User Authentication failed")

        user=authenticate(request,email=Email,password=Password)

        if user is not None:
            login(request,user)
            return redirect('home')
        # else:
        #     messages.error(request,'Authentication failed..!')




    context={'page':page}
    return render(request,'login_register.html',context)

def userRegister(request):
    context={}
    return render(request,'login_register.html',context)

def userLogout(request):
    pass
