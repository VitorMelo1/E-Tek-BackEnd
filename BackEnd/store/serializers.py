from rest_framework import serializers
from .models import Device, Accessory


class DeviceNestedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = ['id', 'name']

class AccessoryNestedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Accessory 
        fields = ['id', 'name']

class DeviceSerializer(serializers.ModelSerializer):
    accessories = AccessoryNestedSerializer(many = True, read_only = True)
    accessories_id = serializers.PrimaryKeyRelatedField(queryset = Accessory.objects.all(), many= True, write_only= True, required= False, source= 'accessories')
    image = serializers.ImageField(required= False)
   
    class Meta:
        model = Device
        fields = ['id', 'name', 'price', 'description', 'image', 'accessories', 'accessories_id']

class AccessorySerializer(serializers.ModelSerializer):
    devices = DeviceNestedSerializer(many =True, read_only =True, )
    devices_id = serializers.PrimaryKeyRelatedField(queryset =Device.objects.all(), many=True, write_only = True, source = 'devices')
    image = serializers.ImageField(required= False)
    class Meta:
        model= Accessory
        fields = ['id', 'name', 'price', 'description', 'image', 'devices', 'devices_id']



