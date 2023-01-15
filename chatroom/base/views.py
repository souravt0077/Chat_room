from django.shortcuts import render,redirect
# from user.models import User
from .models import *
from .form import roomForm
from django.db.models import Q
from django.contrib.auth.decorators import login_required
# Create your views here.

def home(request):
    rooms=Room.objects.all()
    topics=Topic.objects.all()[0:5]
    q=request.GET.get('q') if request.GET.get('q') !=None else ''
    rooms=Room.objects.filter(
        Q(topic__name__icontains=q)|
        Q(name__icontains=q)|
        Q(host__username__icontains=q)
    )
    room_count=rooms.count()
    room_messages=Messages.objects.all()
    room_messages=Messages.objects.filter(
        Q(user__username__icontains=q)|
        Q(room__name__icontains=q)
    )[0:10]
    # topics=Topic.objects.filter(
    #     Q(name__icontains=q)
    # )
    context={'rooms':rooms,'topics':topics,'room_count':room_count,'room_messages':room_messages}
    return render(request,'home.html',context)

@login_required(login_url='login')
def rooms(request,pk):
    rooms=Room.objects.get(id=pk)
    room_messages=rooms.messages_set.all()
    participants=rooms.participants.all()
    if request.method == 'POST':
        Messages.objects.create(
            user=request.user,
            room=rooms,
            body=request.POST.get('body')
        )
        rooms.participants.add(request.user)
        return redirect('rooms',pk=rooms.id)
    
    context={'rooms':rooms,'room_messages':room_messages,'participants':participants}
    return render(request,'room.html',context)

@login_required(login_url='login')
def createRoom(request):
    form=roomForm()
    if request.method == 'POST':
        form=roomForm(request.POST)
        if form.is_valid():
            room=form.save(commit=False)
            room.name=room.name.capitalize()
            room.save()
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
    return render(request,'delete.html',context)

def deleteMessage(request,pk):
    message=Messages.objects.get(id=pk)
    room=Room.objects.all()
    if request.method == 'POST':
        message.delete()
        return redirect('rooms',pk=message.room.id)
    context={"obj":message,"room":room}
    return render(request,'delete.html',context)


def moreTopics(request):
    topics=Topic.objects.all()
    q=request.GET.get('q') if request.GET.get('q') !=None else ''
    topics=Topic.objects.filter(
        Q(name__icontains=q)
    )
    context={'topics':topics}
    return render(request,'more_topics.html',context)

@login_required(login_url='login')
def userProfile(request,pk):
    users=User.objects.get(id=pk)
    rooms=users.room_set.all()
    rooms_count=rooms.count()
    room_messages=users.messages_set.all()[:5]
    context={'users':users,'rooms':rooms,'room_messages':room_messages,'rooms_count':rooms_count}
    return render(request,'userprofile.html',context)
