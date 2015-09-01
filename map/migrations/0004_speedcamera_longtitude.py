# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0003_speedcamera_lattitude'),
    ]

    operations = [
        migrations.AddField(
            model_name='speedcamera',
            name='longtitude',
            field=models.CharField(max_length=50, null=True, blank=True),
        ),
    ]
