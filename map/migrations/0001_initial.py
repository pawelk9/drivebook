# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.contrib.gis.db.models.fields
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SpeedCamera',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('type', models.CharField(default='FS', choices=[('FS', 'Fotoradar stacjonarny'), ('FP', 'Fotoradar przenosny')], max_length=2)),
                ('address', models.CharField(blank=True, null=True, max_length=300)),
                ('city', models.CharField(blank=True, null=True, max_length=300)),
                ('road', models.CharField(blank=True, null=True, max_length=300)),
                ('country', models.CharField(blank=True, null=True, max_length=300)),
                ('postcode', models.CharField(blank=True, null=True, max_length=300)),
                ('state', models.CharField(blank=True, null=True, max_length=300)),
                ('house_number', models.CharField(blank=True, null=True, max_length=300)),
                ('county', models.CharField(blank=True, null=True, max_length=300)),
                ('suburb', models.CharField(blank=True, null=True, max_length=300)),
                ('geometry', django.contrib.gis.db.models.fields.PointField(geography=True, blank=True, srid=4326, null=True)),
                ('longtitude', models.CharField(blank=True, null=True, max_length=50)),
                ('lattitude', models.CharField(blank=True, null=True, max_length=50)),
                ('note', models.TextField(default='', blank=True)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
