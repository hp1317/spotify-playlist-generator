# Generated by Django 3.1 on 2020-12-03 16:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tracks', '0002_playlist'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Playlist',
        ),
    ]
