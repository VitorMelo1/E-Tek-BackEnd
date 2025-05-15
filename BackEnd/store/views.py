from django.shortcuts import render
from rest_framework import viewsets
from .models import Device, Accessory
from .serializers import DeviceSerializer, AccessorySerializer
from django.http import JsonResponse
from .populate import run  # importa a função do populate

# ViewSets da API
class DeviceViewSet(viewsets.ModelViewSet):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer

class AccessoryViewSet(viewsets.ModelViewSet):
    queryset = Accessory.objects.all()
    serializer_class = AccessorySerializer

# View temporária para popular o banco
def populate_view(request):
    run()
    return JsonResponse({"status": "ok", "message": "Banco populado com sucesso!"})
