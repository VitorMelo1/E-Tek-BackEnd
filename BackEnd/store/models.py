from django.db import models

# Create your models here.
class Device(models.Model):
    name = models.CharField(max_length= 50, unique = True, null= False)
    price = models.DecimalField(max_digits=12, decimal_places=2)
    description = models.CharField(max_length=255)
    image = models.ImageField(upload_to='device_images/', blank=True, null=True)

    def __str__(self):
        return self.name

class Accessory(models.Model):
    name = models.CharField(max_length=50,unique=True, null=False)
    price = models.DecimalField(max_digits= 12, decimal_places=2)
    description = models.CharField(max_length=255)
    image = models.ImageField(upload_to='accessory_images/', blank=True, null=True)
    devices = models.ManyToManyField(Device, related_name= 'accessories')

    def __str__(self):
        return self.name

