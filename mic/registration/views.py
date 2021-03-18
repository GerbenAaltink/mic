from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, permissions

from .models import Building, Location, Registration, Device, DeviceType
from .serializers import (
    BuildingSerializer,
    LocationSerializer,
    RegistrationSerializer,
    DeviceSerializer,
    DeviceTypeSerializer,
)


class BuildingViewSet(viewsets.ModelViewSet):
    queryset = Building.objects.all()
    serializer_class = BuildingSerializer


class LocationViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer


class RegistrationViewSet(viewsets.ModelViewSet):
    queryset = Registration.objects.all()
    serializer_class = RegistrationSerializer


class DeviceViewSet(viewsets.ModelViewSet):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer


class DeviceTypeViewSet(viewsets.ModelViewSet):
    queryset = DeviceType.objects.all()
    serializer_class = DeviceTypeSerializer

