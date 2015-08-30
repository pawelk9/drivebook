from django.contrib import admin
from django.contrib.gis import admin as geoadmin
from .models import SpeedCamera


class SpeedCameraAdmin(geoadmin.GeoModelAdmin):
    list_display = ('type', 'geometry', 'city', 'road', 'ref', 'state', 'created_date')
    list_filter = ('created_date', 'type', 'city', 'state', 'ref')
    #search_fields = ['name']

geoadmin.site.register(SpeedCamera, SpeedCameraAdmin)



