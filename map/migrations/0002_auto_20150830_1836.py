# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='speedcamera',
            name='lattitude',
        ),
        migrations.RemoveField(
            model_name='speedcamera',
            name='longtitude',
        ),
    ]
