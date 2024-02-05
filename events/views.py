from .models import Event
from rest_framework import viewsets, permissions

from .serializers import EventSerializer


class EventViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Event.objects.all().order_by('-event_at')
    serializer_class = EventSerializer
    permission_classes = [permissions.IsAuthenticated]