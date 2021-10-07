from rest_framework import serializers
from core.models import Player


class PlayerSerializers(serializers.Serializer):
    class Meta:
        model = Player
        fields = '__all__'


def create(self, validated_data):
    return Player.objects.create(**validated_data)
