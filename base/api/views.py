from rest_framework.decorators import api_view
from rest_framework.response import Response
from base.models import Room
from .serializer import RoomSerializer


@api_view(['GET'])
def getRoutes(req):
    routes = [
        'GET api/rooms',
        'GET api/rooms/:id'
    ]
    return Response(routes)

@api_view(['GET'])
def getRooms(req):
    rooms = Room.objects.all()
    serializer = RoomSerializer(rooms, many=True)
    return Response(serializer.data)