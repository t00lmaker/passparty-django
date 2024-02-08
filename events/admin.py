# In myapp/admin.py
from django.contrib import admin
from .models import Event, Guest
from django.contrib.admin import SimpleListFilter

class EventNameFilter(SimpleListFilter):
    title = 'event name'  # A title for the filter
    parameter_name = 'event__name'

    def lookups(self, request, model_admin):
        # Get the client name from the request's GET parameters
        client_name = request.GET.get('event__client__name')
        if client_name:
            # If a client name is selected, only include events from that client
            events = Event.objects.filter(client__name=client_name)
            return [(event.name, event.name) for event in events]
        else:
            # If no client name is selected, include all events
            return [(event.name, event.name) for event in Event.objects.all()]

    def queryset(self, request, queryset):
        # Filter the queryset based on the selected event name
        if self.value():
            return queryset.filter(event__name=self.value())
        else:
            return queryset

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    ordering = ('client',)
    list_display = ('client', 'name', 'description', 'event_at', 'finished_at', 'created_at', 'updated_at', 'active', )
    readonly_fields = ('created_at', 'updated_at',)
    list_filter = ('client__name', 'active')
    search_fields = ('name',) 

@admin.register(Guest)
class GuestAdmin(admin.ModelAdmin):
    ordering = ('event',)
    list_display = ('event', 'name', 'phone', 'email', 'created_at', 'updated_at',)
    readonly_fields = ('created_at', 'updated_at',)
    list_filter = ('event__client__name', EventNameFilter, 'active',)
    search_fields = ('name', 'phone', 'email',)
    autocomplete_fields = ('event',)