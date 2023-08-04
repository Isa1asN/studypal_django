from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


home = lambda req : render(req, 'home.html')

room = lambda req : render(req, 'room.html')
