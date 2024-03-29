# Generated by Django 5.0.1 on 2024-02-07 23:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_alter_confirmation_details'),
    ]

    operations = [
        migrations.AddField(
            model_name='confirmation',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='event',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='guest',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='guest',
            name='salt',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='finished_at',
            field=models.DateField(blank=True, null=True),
        ),
    ]
