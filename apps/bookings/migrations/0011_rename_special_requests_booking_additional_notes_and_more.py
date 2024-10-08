# Generated by Django 5.1.1 on 2024-10-04 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0010_booking_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='booking',
            old_name='special_requests',
            new_name='additional_notes',
        ),
        migrations.AddField(
            model_name='booking',
            name='allergies',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='booking',
            name='dietary_preferences',
            field=models.TextField(blank=True, null=True),
        ),
    ]
