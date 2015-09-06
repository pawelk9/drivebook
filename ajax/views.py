from django.shortcuts import render
from django.core.serializers import serialize
from map.models import SpeedCamera
from django.http import HttpResponse


def index(request):
    json_data = serialize('json', SpeedCamera.objects.all())
    return HttpResponse(json_data, content_type='text/application/json')
