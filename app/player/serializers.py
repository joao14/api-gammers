from rest_framework import serializers
from core.models import Player


class PlayerSerializers(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = '__all__'
