from django.urls import path, include
from rest_framework import routers

from .views import (
    BuildingViewSet,
    LocationViewSet,
    DeviceViewSet,
    DeviceTypeViewSet,
    RegistrationViewSet,
)

router = routers.DefaultRouter()
router.register(r"building", BuildingViewSet)
router.register(r"location", LocationViewSet)
router.register(r"device", DeviceViewSet)
router.register(r"device_type", DeviceTypeViewSet)
router.register(r"registration", RegistrationViewSet)

urlpatterns = [path("", include(router.urls))]
