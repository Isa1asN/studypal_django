from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from .models import Room

def home(req):
    rooms = Room.objects.all()
    context = {'rooms': rooms}
    return render(req, 'base/home.html', context)

def room(req, pk):
    room = Room.objects.get(id=pk)
    context = {'room':room}
    return render(req, 'base/room.html', context)

def createRoom(req):
    context = {}
    return render(req, 'base/room_form.html', context )