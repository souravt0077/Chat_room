from django.shortcuts import render,redirect
# from user.models import User
from.models import Room
from .form import roomForm
# Create your views here.

def home(request):
    rooms=Room.objects.all()
    context={'rooms':rooms}
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
