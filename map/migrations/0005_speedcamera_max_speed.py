# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0004_auto_20150830_1048'),
    ]

    operations = [
        migrations.AddField(
            model_name='speedcamera',
            name='max_speed',
            field=models.CharField(null=True, blank=True, max_length=10),
        ),
    ]
