# Generated by Django 5.0.2 on 2024-05-23 03:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservations', '0022_alter_cite_photo1_alter_cite_photo2_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cite',
            name='photo1',
            field=models.FileField(blank=True, upload_to='photos'),
        ),
        migrations.AlterField(
            model_name='cite',
            name='photo2',
            field=models.FileField(blank=True, upload_to='photos'),
        ),
        migrations.AlterField(
            model_name='cite',
            name='photo3',
            field=models.FileField(blank=True, upload_to='photos'),
        ),
    ]
