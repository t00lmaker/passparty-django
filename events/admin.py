# In myapp/admin.py
from django.contrib import admin
from .models import Event, Guest

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'event_at', 'finished_at', 'created_at', 'updated_at',)
    readonly_fields = ('created_at', 'updated_at',)


@admin.register(Guest)
class GuestAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'email', 'created_at', 'updated_at',)
    readonly_fields = ('created_at', 'updated_at',)