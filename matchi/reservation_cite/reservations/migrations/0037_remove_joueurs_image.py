# Generated by Django 2.2.22 on 2024-08-16 18:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reservations', '0036_auto_20240816_1800'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='joueurs',
            name='image',
        ),
    ]