from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

rooms = [
    {'id' : 1, 'name' : 'Lets learn python'},
    {'id' : 2, 'name' : 'Design an App'}
]

def home(req):
    context = {'rooms': rooms}
    return render(req, 'base/home.html', context)

def room(req, pk):
    room = None
    for i in rooms:
        if i['id'] == int(pk):
            room = i
    context = {'room':room}
    return render(req, 'base/room.html', context)
