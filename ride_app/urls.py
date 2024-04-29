from django.urls import path
from .views import (
    RideListApiView, RideDetailApiView, RideRequestApiView, UpdateRideStatusApiView
)

urlpatterns = [
    path("ride_list/", RideListApiView.as_view(), name="ride-list"),
    path("ride_detail/<int:id>/", RideDetailApiView.as_view(), name="ride-detail"),
    path("request_ride/<int:id>/", RideRequestApiView.as_view(), name="ride-request"),
    path("update_ride_status/<int:id>/", UpdateRideStatusApiView.as_view(), name="ride-status"),
    ]
