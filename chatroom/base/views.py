from django.shortcuts import render
from user.models import User
# Create your views here.

def home(request):
    users=User.objects.all()
    context={'users':users}
    return render(request,'home.html',context)
