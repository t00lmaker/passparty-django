from django.db import models

class Event(models.Model):
  readonly_fields = ("created_at", "updated_at")
  name = models.CharField(max_length=40, null=False, blank=False)
  description = models.CharField(max_length=250)
  cover_image = models.CharField(max_length=250, null=True, blank=True)
  event_at = models.DateField(null=True)
  
  finished_at = models.DateField(null=True)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)


class Guest(models.Model):
  readonly_fields = ("created_at", "updated_at")
  name = models.CharField(max_length=40, null=False, blank=False)
  phone = models.CharField(max_length=40, null=False, blank=False)
  email = models.CharField(max_length=40)
  event = models.ForeignKey(Event,related_name='guests',  on_delete=models.CASCADE)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)


class Confirmation(models.Model):
  readonly_fields = ("created_at", "updated_at")
  details = models.CharField(max_length=500)
  event = models.ForeignKey(Event,related_name='confirmation',  on_delete=models.CASCADE)
  guest = models.OneToOneField(
    Guest,
    on_delete=models.CASCADE,
    primary_key=True,
  )
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)


