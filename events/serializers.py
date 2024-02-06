from .models import Event, Guest, Confirmation
from rest_framework import serializers


class EventSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Event
        fields = ['name', 'description', 'cover_image', 'event_at', 'finished_at', 'created_at', 'updated_at']

class GuestSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Guest
        fields = ['name', 'phone', 'email', 'event', 'confirmation', 'created_at', 'updated_at']

class ConfirmationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Confirmation
        fields = ['details', 'created_at', 'updated_at']