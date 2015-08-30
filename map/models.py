from django.db import models
from django.contrib.gis.db import models as gis_models
from django.utils import timezone
from geopy.geocoders import Nominatim


class SpeedCamera(models.Model):


    TYPES = (
        ('FS', 'Fotoradar stacjonarny'),
        ('FP', 'Fotoradar przenosny')
    )
    type = gis_models.CharField(max_length=2, choices=TYPES, default='FS')
    address = gis_models.CharField(max_length=300, blank=True, null=True)
    city = gis_models.CharField(max_length=300, blank=True, null=True)
    road = gis_models.CharField(max_length=300, blank=True, null=True)
    country = gis_models.CharField(max_length=300, blank=True, null=True)
    postcode = gis_models.CharField(max_length=300, blank=True, null=True)
    state = gis_models.CharField(max_length=300, blank=True, null=True)
    house_number = gis_models.CharField(max_length=300, blank=True, null=True)
    county = gis_models.CharField(max_length=300, blank=True, null=True)
    suburb = gis_models.CharField(max_length=300, blank=True, null=True)

    geometry = gis_models.PointField(srid=4326, geography=True, blank=True, null=True)
    longtitude = gis_models.CharField(max_length=50, blank=True, null=True)
    lattitude = gis_models.CharField(max_length=50, blank=True, null=True)

    note = gis_models.TextField(blank=True, default='')
    created_date = gis_models.DateTimeField(default=timezone.now)


    gis = gis_models.GeoManager()
    objects = models.Manager()

    def __str__(self):
        return self.address

    def save(self, **kwargs):

        geolocator = Nominatim()

        lon = str(self.geometry.x)
        lat = str(self.geometry.y)

        location = geolocator.reverse(lat + ', ' + lon)
        self.address = location.address

        if 'city' in location.raw['address']:
            self.city = location.raw['address']['city']

        if 'road' in location.raw['address']:
            self.road = location.raw['address']['road']

        if 'country' in location.raw['address']:
            self.country = location.raw['address']['country']

        if 'postcode' in location.raw['address']:
            self.postcode = location.raw['address']['postcode']

        if 'state' in location.raw['address']:
            self.state = location.raw['address']['state']

        if 'house_number' in location.raw['address']:
            self.house_number = location.raw['address']['house_number']

        if 'county' in location.raw['address']:
            self.county = location.raw['address']['county']

        if 'suburb' in location.raw['address']:
            self.suburb = location.raw['address']['suburb']

        self.lattitude = lat
        self.longtitude = lon


        super(SpeedCamera, self).save()

'''
{'address': {'county': 'Cook County', 'state': 'Illinois', 'suburb': 'Near North Side',
 'city': 'Chicago', 'country_code': 'us', 'postcode': '60661', 'country': 'United States of America',
  'neighbourhood': 'Greektown', 'house_number': '703', 'road': 'West Monroe Street'},
   'place_id': '91429157', 'osm_type': 'way', 'lon': '-87.6443740745258', 'lat': '41.8803483',
    'licence': 'Data \xa9 OpenStreetMap contributors, ODbL 1.0. http://www.openstreetmap.org/copyright',
     'display_name': '703, West Monroe Street, Greektown, Near North Side, Chicago, Cook County, Illinois,
      60661, United States of America', 'osm_id': '156356430'}
'''