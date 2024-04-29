from rest_framework import generics
from .models import Rides
from .serializers import RideSerializer


class RideListApiView(generics.ListAPIView):
    """
    Api that gets all the available rides list.
    """
    queryset = Rides.objects.filter(status=Rides.Ride_Status.AVAILABLE)
    serializer_class = RideSerializer


class RideDetailApiView(generics.RetrieveAPIView):
    """
    Get ride details
    """
    lookup_field = 'id'
    queryset = Rides.objects.all()
    serializer_class = RideSerializer

class RideRequestApiView(generics.UpdateAPIView):
    """
        Request a ride
    """
    lookup_field = 'id'
    queryset = Rides.objects.all()
    serializer_class = RideSerializer

class UpdateRideStatusApiView(generics.UpdateAPIView):
    """
     Update status of a ride
    """
    lookup_field = 'id'
    queryset = Rides.objects.all()
    serializer_class = RideSerializer

