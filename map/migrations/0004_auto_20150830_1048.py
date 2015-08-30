# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0003_speedcamera_osm_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='speedcamera',
            name='osm_url',
            field=models.URLField(blank=True, max_length=300, null=True),
        ),
    ]
