from .models import Event
from rest_framework import serializers


class EventSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Event
        fields = ['name', 'description', 'cover_image', 'event_at', 'finished_at', 'created_at', 'updated_at']