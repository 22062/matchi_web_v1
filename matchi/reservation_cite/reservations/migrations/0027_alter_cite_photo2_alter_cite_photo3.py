# Generated by Django 5.0.2 on 2024-05-23 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservations', '0026_alter_cite_photo1_alter_cite_photo2_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cite',
            name='photo2',
            field=models.ImageField(blank=True, upload_to='images'),
        ),
        migrations.AlterField(
            model_name='cite',
            name='photo3',
            field=models.ImageField(blank=True, upload_to='images'),
        ),
    ]
