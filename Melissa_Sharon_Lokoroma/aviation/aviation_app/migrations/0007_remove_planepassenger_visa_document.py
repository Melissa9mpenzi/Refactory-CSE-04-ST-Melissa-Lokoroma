# Generated by Django 5.0.6 on 2024-09-13 12:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aviation_app', '0006_planepassenger_visa_document'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='planepassenger',
            name='visa_document',
        ),
    ]
