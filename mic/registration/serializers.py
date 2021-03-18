from rest_framework import serializers

from .models import Registration, Building, Device, Location, DeviceType


class RegistrationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Registration
        fields = ["percentage_use", "device"]


class BuildingSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Building
        fields = ["pk", "name"]


class DeviceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Device
        fields = ["pk", "uid", "name", "location", "type"]
        search_fields = [
            "building__name",
            "location__name",
            "type__pk",
            "type",
            "name",
            "pk",
        ]


class LocationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Location
        fields = ["pk", "name", "building"]
        search_fields = ["name", "building__name", "pk"]


class DeviceTypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = DeviceType
        fields = ["pk", "name", "wh"]
        search_fields = ["name", "wh"]
