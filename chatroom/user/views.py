from django.shortcuts import render,redirect
from .models import User
from django.contrib import messages
from django.contrib.auth import login,logout,authenticate
from .form import myUserForm,updateUserForm
from django.contrib.auth.decorators import login_required
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
    form=myUserForm()
    if request.method == 'POST':
        form=myUserForm(request.POST,request.FILES)
        if form.is_valid():
            user=form.save(commit=False)
            user.username=user.username.upper()
            user.save()
            login(request,user)
            return redirect('home')

    context={'form':form}
    return render(request,'login_register.html',context)

def userLogout(request):
    logout(request)
    return redirect('home')

@login_required(login_url='login')
def updateUser(request):
    user=request.user
    form=updateUserForm(instance=user)
    if request.method =='POST':
        form=updateUserForm(request.POST,request.FILES,instance=user)
        if form.is_valid():
            form.save()
            login(request,user)
            return redirect('userprofile',user.id)
        else:
            messages.error(request,'something wrong...!')

    context={'form':form}
    return render(request,'updateuser.html',context)    
