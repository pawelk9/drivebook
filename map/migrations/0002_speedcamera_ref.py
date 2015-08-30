# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='speedcamera',
            name='ref',
            field=models.CharField(null=True, max_length=300, blank=True),
        ),
    ]
