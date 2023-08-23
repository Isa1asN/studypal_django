from django.forms import ModelForm
from .models import Room, User



class RoomForm(ModelForm):
    class Meta:
        model = Room 
        exclude = ['host', 'participants']

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']
        