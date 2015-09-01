from django.shortcuts import render
from django.core.serializers import serialize
from map.models import SpeedCamera
from django.http import HttpResponse


def index(request):
    xml_data = serialize('xml', SpeedCamera.objects.all())
    return HttpResponse(xml_data, content_type='text/xml')
