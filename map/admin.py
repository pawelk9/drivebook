from django.contrib import admin
from django.contrib.gis import admin as geoadmin
from .models import SpeedCamera


class SpeedCameraAdmin(geoadmin.GeoModelAdmin):

    fieldsets = [
        ('Speed device', {'fields': ['type', 'address']}),
        ('Address',
         {'fields': ['road', 'city', 'country', 'postcode', 'state', 'house_number', 'county', 'suburb']}),
        ('Way', {'fields': ['ref', 'max_speed']}),
        ('Geography', {'fields': ['geometry', 'longtitude', 'lattitude']}),
        ('Open Street Map', {'fields': ['osm_url']}),
        ('Date', {'fields': ['created_date']}),
        ('Other', {'fields': ['note']}),
    ]

    list_display = ('type', 'geometry', 'city', 'road', 'ref', 'state', 'created_date')
    list_filter = ('created_date', 'type', 'city', 'state', 'ref')


geoadmin.site.register(SpeedCamera, SpeedCameraAdmin)
