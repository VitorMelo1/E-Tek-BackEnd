from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DeviceViewSet, AccessoryViewSet

router = DefaultRouter()
router.register(r'devices', DeviceViewSet)
router.register(r'accessories', AccessoryViewSet)

urlpatterns = [
    path('', include(router.urls)),
]