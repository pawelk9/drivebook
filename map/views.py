from django.shortcuts import render
from .models import SpeedCamera


def index(request):
    speed_cameras = SpeedCamera.objects.all()
    return render(request, 'map/index.html', {'speed_cameras': speed_cameras})

