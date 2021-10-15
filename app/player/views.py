from django.http import HttpResponse, Http404
from rest_framework import generics, status
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from core.models import Player

from .serializers import PlayerSerializers


class PlayerViewSet(generics.GenericAPIView):
    serializer_class = PlayerSerializers

    """ Retrieve, update or delete a snippet instance.  """

    def get_object(self, pk):
        try:
            return Player.objects.get(pk=pk)
        except Player.DoesNotExist:
            raise Http404

    #def get_all(self, request, *args, **kwargs):
        #player = Player.objects.all()
        #serializer = PlayerSerializers(player, many=True)
        #return Response(serializer.data)

    def get(self, request, pk, format=None):
        player = self.get_object(pk)
        serializer = PlayerSerializers(player)
        return Response(serializer.data)

    def post(self, request):
        serializer = PlayerSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            res = {'msg': 'Create player'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data, content_type='application/json')

    def delete(self, request, pk, format=None):
        player = self.get_object(pk)
        player.delete()
        res = {'msg': 'Delete player'}
        json_data = JSONRenderer().render(res)
        return HttpResponse(json_data, content_type='application/json')
