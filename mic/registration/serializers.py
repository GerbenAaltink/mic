from rest_framework import serializers

from .models import Registration, Building, Device, Location, DeviceType


class RegistrationSerializer(serializers.HyperlinkedModelSerializer):

    uid = serializers.UUIDField()

    def create(self, validated_data):
        device = Device.objects.get(uid=validated_data["uid"])
        return Registration.objects.create(
            device=device, percentage_use=validated_data["percentage_use"]
        )

    class Meta:
        model = Registration
        fields = ["percentage_use", "uid"]


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
        search_fields = ["name", "building_name", "pk"]


class DeviceTypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = DeviceType
        fields = ["pk", "name", "wh"]
