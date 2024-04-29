from rest_framework import serializers
from .models import Rides

class RideSerializer(serializers.ModelSerializer):
    driver_name = serializers.CharField(source='driver.username')
    class Meta:
        model = Rides
        fields = ["id", "driver", "rider", "driver_name", "pickup_location", "drop_off_location", "status"]
