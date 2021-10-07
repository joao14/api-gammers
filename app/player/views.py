from django.http import HttpResponse
from rest_framework import generics, status
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from core.models import Player

from .serializers import PlayerSerializers


class PlayerViewSet(generics.GenericAPIView):

    serializer_class = PlayerSerializers

    def list(self, request):
        player = Player.objects().all()
        serializer = PlayerSerializers(player, many=True)
        return Response(serializer.data)

    def create_player(self, request):
        print("Vamos a ver...")
        """Create new player"""
        if request.method == "POST":
            serializer = PlayerSerializers(data=request.data)
            if serializer.is_valid():
                serializer.save()
                res = {'msg': 'Player created'}
                json_data = JSONRenderer().render(res)
                return HttpResponse(json_data, content_type='application/json')

        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data, content_type='application/json')
