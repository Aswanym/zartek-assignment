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
    View for requesting a ride.

    Methods:
    - PATCH : Accepts ride request data which will have rider and status of ride as "REQUESTED".
              This view require jwt authentication

    Serializer Used:
    - RideSerializer

    Example Usage:
    ```
    PATCH /request_ride/<int:id>/
    {
        "status":"REQUESTED",
        "rider":4
    }
    ```

    Response (Success):
    ```
    HTTP 200 ok
    ```
    """
    lookup_field = 'id'
    queryset = Rides.objects.all()
    serializer_class = RideSerializer

class UpdateRideStatusApiView(generics.UpdateAPIView):
    """
    View for updating status of a ride.

    Methods:
    - PATCH : Accepts ride request data which will have any of the status
              ["NOT_AVAILABLE", "STARTED", "COMPLETED", "CANCELLED", "AVAILABLE"]
              This view require jwt authentication

    Serializer Used:
    - RideSerializer

    Example Usage:
    ```
    PATCH /update_ride_status/<int:id>/
    {
        "status":"STARTED"
    }
    ```

    Response (Success):
    ```
    HTTP 200 ok
    ```
    """
    lookup_field = 'id'
    queryset = Rides.objects.all()
    serializer_class = RideSerializer

