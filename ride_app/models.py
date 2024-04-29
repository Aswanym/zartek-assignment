from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
# Create your models here.

class Rides(models.Model):

    class Ride_Status (models.TextChoices):
        AVAILABLE = "AVAILABLE", _("Available")
        NOT_AVAILABLE = "NOT_AVAILABLE", _("Not available")
        REQUESTED = "REQUESTED", _("Requested")
        STARTED = "STARTED", _("Started")
        COMPLETED = "COMPLETED", _("Completed")
        CANCELLED = "CANCELLED", _("Cancelled")

    rider = models.ForeignKey(User, on_delete=models.CASCADE, related_name='drivers', null=True, blank=True)
    driver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='riders')
    pickup_location = models.CharField(max_length=225, null=True, blank=True)
    drop_off_location = models.CharField(max_length=225, null=True, blank=True)
    current_location = models.CharField(max_length=225, null=True, blank=True)
    status = models.CharField(max_length=30, choices=Ride_Status.choices, default=Ride_Status.AVAILABLE)
    status_details = models.CharField(max_length=225, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
