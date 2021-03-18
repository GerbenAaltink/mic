from datetime import datetime

from django.db import models


class DeviceType(models.Model):
    wh = models.PositiveIntegerField()
    name = models.CharField(max_length=50, blank=False)

    def __str__(self):
        return self.name


class Building(models.Model):
    name = models.CharField(max_length=50, blank=False)

    def __str__(self):
        return self.name


class Location(models.Model):
    name = models.CharField(max_length=50, blank=False)
    building = models.ForeignKey(
        Building, on_delete=models.CASCADE, related_name="locations", blank=False
    )

    def __str__(self):
        return self.name


class Device(models.Model):
    name = models.CharField(max_length=50, blank=False)
    location = models.ForeignKey(
        Location, on_delete=models.CASCADE, related_name="devices", blank=False
    )
    type = models.ForeignKey(
        DeviceType, on_delete=models.CASCADE, related_name="devices", blank=False
    )
    uid = models.UUIDField(blank=False)

    def __str__(self):
        return self.name


class Registration(models.Model):
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    percentage_use = models.PositiveSmallIntegerField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.device} {self.percentage_use}"
