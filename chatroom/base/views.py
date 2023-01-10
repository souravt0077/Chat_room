from django.shortcuts import render,redirect
# from user.models import User
from.models import *
from .form import roomForm
from django.db.models import Q
# Create your views here.

def home(request):
    rooms=Room.objects.all()
    topics=Topic.objects.all()
    q=request.GET.get('q') if request.GET.get('q') !=None else ''
    rooms=Room.objects.filter(
        Q(topic__name__icontains=q)|
        Q(name__icontains=q)|
        Q(host__username__icontains=q)
    )
    room_count=rooms.count()
    context={'rooms':rooms,'topics':topics,'room_count':room_count}
    return render(request,'home.html',context)

def rooms(request,pk):
    rooms=Room.objects.get(id=pk)
    context={'rooms':rooms}
    return render(request,'room.html',context)

def createRoom(request):
    form=roomForm()
    if request.method == 'POST':
        form=roomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    context={'form':form}
    return render(request,'room_form.html',context)

def updateRoom(request,pk):
    room=Room.objects.get(id=pk)
    form=roomForm(instance=room)
    if request.method == 'POST':
        form=roomForm(request.POST,instance=room)
        if form.is_valid():
            form.save()
            return redirect('rooms',room.id)
    context={'form':form}
    return render(request,'room_form.html',context)

def deleteRoom(request,pk):
    room=Room.objects.get(id=pk)
    if request.method == 'POST':
        room.delete()
        return redirect('home')
    context={'obj':room}
    return render(request,'deleteRoom.html',context)
