from .models import Event
from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .serializers import EventSerializer


class EventViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows all events to be viewed or edited.
    """
    queryset = Event.objects.all().order_by('-event_at')
    serializer_class = EventSerializer
    permission_classes = [permissions.IsAuthenticated]


    @csrf_exempt
    @action(detail=True, methods=["get"], name="Guests from event")
    def guests(self, request,  pk=None):
        """
        API endpoint that allows all guests from an event to be viewed or edited.
        """
        try:
            event = Event.objects.get(pk=pk)
        except Event.DoesNotExist:
            return HttpResponse(status=404)
        
        return JsonResponse(list(event.guests.values()), safe=False)