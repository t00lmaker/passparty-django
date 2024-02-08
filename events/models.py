from django.db import models
from preferences.models import Client

class Event(models.Model):
  readonly_fields = ("created_at", "updated_at")
  name = models.CharField(max_length=40, null=False, blank=False)
  description = models.CharField(max_length=250)
  cover_image = models.CharField(max_length=250, null=True, blank=True)
  event_at = models.DateField(null=True)
  active = models.BooleanField(default=True)
  client = models.ForeignKey(Client, on_delete=models.CASCADE, null=True, blank=True, related_name='events')

  finished_at = models.DateField(null=True, blank=True)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  def __str__(self):
    return self.name


class Guest(models.Model):
  readonly_fields = ("created_at", "updated_at")
  name = models.CharField(max_length=40, null=False, blank=False)
  phone = models.CharField(max_length=40, null=False, blank=False)
  email = models.CharField(max_length=40)
  active = models.BooleanField(default=True)
  salt = models.CharField(max_length=40, null=True, blank=True)
  event = models.ForeignKey(Event,related_name='guests',  on_delete=models.CASCADE)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  def __str__(self):
    return self.name

class Confirmation(models.Model):
  readonly_fields = ("created_at", "updated_at")
  details = models.CharField(max_length=500,null=True, blank=True)
  event = models.ForeignKey(Event,related_name='confirmation',  on_delete=models.CASCADE)
  active = models.BooleanField(default=True)
  guest = models.OneToOneField(
    Guest,
    on_delete=models.CASCADE,
    primary_key=True,
    related_name='confirmation',
  )
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)


