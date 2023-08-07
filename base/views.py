from django.shortcuts import render, redirect
from .models import Room
from .forms import RoomForm

def home(req):
    rooms = Room.objects.all()
    context = {'rooms': rooms}
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