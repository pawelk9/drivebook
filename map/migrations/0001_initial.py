# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
import django.contrib.gis.db.models.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SpeedCamera',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('type', models.CharField(default='FS', max_length=2, choices=[('FS', 'Fotoradar stacjonarny'), ('FP', 'Fotoradar przenosny')])),
                ('address', models.CharField(null=True, blank=True, max_length=300)),
                ('city', models.CharField(null=True, blank=True, max_length=300)),
                ('road', models.CharField(null=True, blank=True, max_length=300)),
                ('ref', models.CharField(null=True, blank=True, max_length=300)),
                ('country', models.CharField(null=True, blank=True, max_length=300)),
                ('postcode', models.CharField(null=True, blank=True, max_length=300)),
                ('state', models.CharField(null=True, blank=True, max_length=300)),
                ('house_number', models.CharField(null=True, blank=True, max_length=300)),
                ('county', models.CharField(null=True, blank=True, max_length=300)),
                ('suburb', models.CharField(null=True, blank=True, max_length=300)),
                ('neighbourhood', models.CharField(null=True, blank=True, max_length=300)),
                ('city_district', models.CharField(null=True, blank=True, max_length=300)),
                ('osm_url', models.URLField(null=True, blank=True, max_length=300)),
                ('geometry', django.contrib.gis.db.models.fields.PointField(geography=True, null=True, blank=True, srid=4326)),
                ('longtitude', models.CharField(null=True, blank=True, max_length=50)),
                ('lattitude', models.CharField(null=True, blank=True, max_length=50)),
                ('max_speed', models.CharField(null=True, blank=True, max_length=10)),
                ('note', models.TextField(default='', blank=True)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
