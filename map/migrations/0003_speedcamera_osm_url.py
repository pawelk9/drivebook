# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0002_speedcamera_ref'),
    ]

    operations = [
        migrations.AddField(
            model_name='speedcamera',
            name='osm_url',
            field=models.CharField(max_length=300, blank=True, null=True),
        ),
    ]
