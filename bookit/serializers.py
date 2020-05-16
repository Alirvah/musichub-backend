from . import models

from rest_framework import serializers


class RoomSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Room
        fields = (
            'pk', 
            'name', 
            'size', 
        )


class EventSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Event
        fields = (
            'pk', 
            'name', 
            'created', 
            'start', 
            'end', 
        )


