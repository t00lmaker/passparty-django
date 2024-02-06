from .models import Event, Guest, Confirmation
from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .serializers import EventSerializer, GuestSerializer, ConfirmationSerializer


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
            return JsonResponse({"detail": "Event not found."}, status=404)
        
        return JsonResponse(list(event.guests.values()), safe=False)
    
class GuestViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows all events to be viewed or edited.
    """
    queryset = Guest.objects.all().order_by('-name')
    serializer_class = GuestSerializer
    permission_classes = [permissions.IsAuthenticated]


    @csrf_exempt
    @action(detail=True, methods=["post"], name="Confirm Guests in event")
    def confirm(self, request,  pk=None):
        """
        API endpoint that allows confirm guest in event.
        """
        try:
            guest = Guest.objects.get(pk=pk)
        except Guest.DoesNotExist:
            return JsonResponse({"detail": "Guest not found."}, status=404)
        
        if hasattr(guest, 'confirmation'):
            return JsonResponse({"detail": "Guest already has a confirmation"}, status=420)
        
        confirmation = Confirmation.objects.create(details=request.data.get('details'), event=guest.event, guest=guest)
        serializer = ConfirmationSerializer(confirmation)
        return JsonResponse(serializer.data, status=200)
        