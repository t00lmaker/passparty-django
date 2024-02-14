# Generated by Django 5.0.1 on 2024-02-08 00:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0004_confirmation_active_event_active_guest_active_and_more'),
        ('preferences', '0002_alter_user_options_alter_preferences_key_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='client',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='events', to='preferences.client'),
        ),
    ]