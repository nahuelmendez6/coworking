# Generated by Django 5.1.4 on 2024-12-26 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spaces', '0004_roomimage_room_images'),
    ]

    operations = [
        migrations.AddField(
            model_name='space',
            name='spaceImage',
            field=models.ManyToManyField(related_name='spaceImg', to='spaces.spaceimage'),
        ),
        migrations.AlterField(
            model_name='spaceimage',
            name='image',
            field=models.ImageField(upload_to='uploads/'),
        ),
    ]
