# Generated by Django 5.0.2 on 2024-05-21 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservations', '0004_rename_site_cite'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cite',
            name='photo1',
            field=models.ImageField(blank=True, upload_to='matchi_ap/reservation_cite/static/images'),
        ),
        migrations.AlterField(
            model_name='cite',
            name='photo2',
            field=models.ImageField(blank=True, upload_to='matchi_ap/reservation_cite/static/images'),
        ),
        migrations.AlterField(
            model_name='cite',
            name='photo3',
            field=models.ImageField(blank=True, upload_to='matchi_ap/reservation_cite/static/images'),
        ),
    ]
