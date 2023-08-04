
from django.contrib import admin
from django.urls import path, include, re_path
from django.http import HttpResponse

oops = lambda req : HttpResponse('<h1>Oops...<br/> this page does not seem to exist</h1>')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('base.urls')),
    re_path(r'^.*$', oops),
   
]
