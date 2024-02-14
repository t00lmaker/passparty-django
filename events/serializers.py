from .models import Event, Guest, Confirmation, Responsible
from rest_framework import serializers


class ResponsableSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Responsible
        lookup_field = 'name'

        fields = [
            'name', 
            'phone',
        ]

class EventSerializer(serializers.HyperlinkedModelSerializer):
    
    responsible = ResponsableSerializer(read_only=True, many=False)

    class Meta:
        model = Event
        fields = [
            'id',
            'name', 
            'description', 
            'cover_image', 
            'event_at', 
            'finished_at', 
            'created_at', 
            'updated_at', 
            'started', 
            'active',
            'responsible',
        ]

class ConfirmationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Confirmation
        fields = ['details', 'created_at', 'updated_at']

class GuestSerializer(serializers.HyperlinkedModelSerializer):
    confirmation = ConfirmationSerializer(read_only=True, many=False)
    class Meta:
        model = Guest
        fields = [
            'id',
            'name', 
            'phone', 
            'email',
            'event',
            'confirmation', 
            'created_at', 
            'updated_at'
        ]

