from django.shortcuts import render
from rest_framework import viewsets
from .models import Device, Accessory
from .serializers import DeviceSerializer, AccessorySerializer

# Create your views here.
class DeviceViewSet(viewsets.ModelViewSet):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer

class AccessoryViewSet(viewsets.ModelViewSet):
    queryset = Accessory.objects.all()
    serializer_class = AccessorySerializer