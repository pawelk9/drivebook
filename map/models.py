from django.db import models
from django.contrib.gis.db import models as gis_models
from django.utils import timezone
from geopy.geocoders import Nominatim
import xml.etree.ElementTree as ET
import requests


def osm_xml_parse(url, k):
    r = requests.get(url)

    if r.status_code == 200:
        root = ET.fromstring(r.text)
        for tag in root.iter('tag'):
            if tag.attrib['k'] == k:
                return tag.attrib['v']
    else:
        return None


class SpeedCamera(models.Model):
    TYPES = (
        ('FS', 'Fotoradar stacjonarny'),
        ('FP', 'Fotoradar przenosny')
    )
    type = gis_models.CharField(max_length=2, choices=TYPES, default='FS')
    address = gis_models.CharField(max_length=300, blank=True, null=True)
    city = gis_models.CharField(max_length=300, blank=True, null=True)
    road = gis_models.CharField(max_length=300, blank=True, null=True)
    ref = gis_models.CharField(max_length=300, blank=True, null=True)
    country = gis_models.CharField(max_length=300, blank=True, null=True)
    postcode = gis_models.CharField(max_length=300, blank=True, null=True)
    state = gis_models.CharField(max_length=300, blank=True, null=True)
    house_number = gis_models.CharField(max_length=300, blank=True, null=True)
    county = gis_models.CharField(max_length=300, blank=True, null=True)
    suburb = gis_models.CharField(max_length=300, blank=True, null=True)
    neighbourhood = gis_models.CharField(max_length=300, blank=True, null=True)
    city_district = gis_models.CharField(max_length=300, blank=True, null=True)

    osm_url = gis_models.URLField(max_length=300, blank=True, null=True)

    geometry = gis_models.PointField(srid=4326, geography=True, blank=True, null=True)
    longtitude = gis_models.CharField(max_length=50, blank=True, null=True)
    lattitude = gis_models.CharField(max_length=50, blank=True, null=True)

    max_speed = gis_models.CharField(max_length=10, blank=True, null=True)

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

        if 'neighbourhood' in location.raw['address']:
            self.neighbourhood = location.raw['address']['neighbourhood']

        if 'city_district' in location.raw['address']:
            self.city_district = location.raw['address']['city_district']

        if 'osm_id' in location.raw:
            self.ref = osm_xml_parse('http://www.openstreetmap.org/api/0.6/way/' + location.raw['osm_id'], 'ref')
            self.max_speed = osm_xml_parse('http://www.openstreetmap.org/api/0.6/way/' + location.raw['osm_id'],
                                           'maxspeed')
            self.osm_url = 'http://www.openstreetmap.org/api/0.6/way/' + location.raw['osm_id']

        self.lattitude = lat
        self.longtitude = lon

        super(SpeedCamera, self).save()
