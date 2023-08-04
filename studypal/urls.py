
from django.contrib import admin
from django.urls import path
from django.http import HttpResponse

home = lambda req : HttpResponse('<h1 style="color:red;">Home Page</h1><button rf="www.google.com">click here</button><input />')

room = lambda req : HttpResponse('ROOM')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('room/', room)
]
