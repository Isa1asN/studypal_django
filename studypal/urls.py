
from django.contrib import admin
from django.urls import path, include, re_path
from django.http import HttpResponse

oops = lambda req : HttpResponse('<style>body{background-color:black; color:white}</style><center><h1>Oops...<br/> This page does not seem to exist</h1></center>')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('base.urls')),
    path('api/', include('base.api.urls')),
    re_path(r'^.*$', oops),
   
]
 