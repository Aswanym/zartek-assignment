from django.contrib import admin
from .models import Rides
# Register your models here.

@admin.register(Rides)
class RideAdmin(admin.ModelAdmin):
    """
    Representation in django admin panel
    """
    fields = (
        'id', 'pickup_location', 'drop_off_location', 'status',
        'driver', 'rider', 'current_location', 'status_details',
        'created_at', 'updated_at',
    )
    list_display = (
        'id', 'pickup_location', 'drop_off_location', 'status',
        'driver', 'rider',
        'created_at', 'updated_at',
    )
    list_filter = (
        'status',
    )
    readonly_fields = (
        'id', 'created_at', 'updated_at',
    )
