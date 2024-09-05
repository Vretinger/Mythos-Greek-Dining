# Generated by Django 5.1 on 2024-09-05 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0005_alter_booking_confirmed'),
    ]

    operations = [
        migrations.AddField(
            model_name='table',
            name='buffer_after',
            field=models.DurationField(default='01:00:00'),
        ),
        migrations.AddField(
            model_name='table',
            name='buffer_before',
            field=models.DurationField(default='01:00:00'),
        ),
    ]
