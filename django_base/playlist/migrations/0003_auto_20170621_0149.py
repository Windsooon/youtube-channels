# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-21 01:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('playlist', '0002_playlist_last_update_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='playlist',
            name='inner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='playlist', to='inner.Inner'),
        ),
    ]
