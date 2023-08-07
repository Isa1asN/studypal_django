from django.shortcuts import render, redirect
from django.db.models import Q
from .models import Room, Topic
from .forms import RoomForm

def home(req):
    q = req.GET.get('q') if req.GET.get('q') != None else ''
    rooms = Room.objects.filter(
        Q(topic__name__icontains=q) |
        Q(name__icontains=q) |
        Q(description__icontains=q) 
        )
    topics = Topic.objects.all()
    room_count = rooms.count()
    context = {'rooms': rooms, 'topics' : topics, 'room_count' : room_count}
    return render(req, 'base/home.html', context)

def room(req, pk):
    room = Room.objects.get(id=pk)
    context = {'room':room}
    return render(req, 'base/room.html', context)

def createRoom(req):
    form = RoomForm()

    if req.method == 'POST':
        form = RoomForm(req.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form' : form}
    return render(req, 'base/room_form.html', context )

def updateRoom(req, pk):
    room = Room.objects.get(id = pk)
    form = RoomForm(instance=room)

    if req.method == 'POST':
        form = RoomForm(req.POST, instance=room)
        if form.is_valid:
            form.save()
            return redirect('home')
    context = {'form' : form }
    return render(req, 'base/room_form.html', context)

def deleteRoom(req, pk):
    room = Room.objects.get(id=pk)
    if req.method == 'POST':
        room.delete()
        return redirect('home')
    return render(req, 'base/delete.html', {'obj':room})



