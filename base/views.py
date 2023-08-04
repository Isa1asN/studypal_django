from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


home = lambda req : HttpResponse('<h1 >Home Page</h1><button >click here</button><input />')

room = lambda req : HttpResponse('ROOM')
