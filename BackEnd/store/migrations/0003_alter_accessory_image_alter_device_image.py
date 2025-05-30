# Generated by Django 5.2.1 on 2025-05-12 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_accessory_image_device_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accessory',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='accessory_images/'),
        ),
        migrations.AlterField(
            model_name='device',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='device_images/'),
        ),
    ]
