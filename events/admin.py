# In myapp/admin.py
from django.contrib import admin
from .models import Event

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'event_at', 'finished_at', 'created_at', 'updated_at')
    readonly_fields = ('created_at', 'updated_at',)
