from . import models
from . import serializers
from rest_framework import viewsets, permissions


class RoomViewSet(viewsets.ModelViewSet):
    """ViewSet for the Room class"""

    queryset = models.Room.objects.all()
    serializer_class = serializers.RoomSerializer
    permission_classes = [permissions.IsAuthenticated]


class EventViewSet(viewsets.ModelViewSet):
    """ViewSet for the Event class"""

    queryset = models.Event.objects.all()
    serializer_class = serializers.EventSerializer
    permission_classes = [permissions.IsAuthenticated]


