# Generated by Django 5.0.2 on 2024-05-22 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservations', '0009_alter_cite_photo1_alter_cite_photo2_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cite',
            name='photo1',
            field=models.ImageField(blank=True, upload_to='Matchiapp/static/assets/img'),
        ),
        migrations.AlterField(
            model_name='cite',
            name='photo2',
            field=models.ImageField(blank=True, upload_to='Matchiapp/static/assets/img'),
        ),
        migrations.AlterField(
            model_name='cite',
            name='photo3',
            field=models.ImageField(blank=True, upload_to='Matchiapp/static/assets/img'),
        ),
    ]
