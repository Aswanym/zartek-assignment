from django.test import TestCase
from ride_app.models import Rides
from django.contrib.auth.models import User

class RideModelTest(TestCase):

    def setUp(self):
        # Define the data dictionary in the setUp method
        self.user_data = {
                    "username": "new_user",
                    "password": "1234",
                    "email": "example@gmail.com"
                }
        driver = User.objects.create_user(**self.user_data)

        self.ride_data = {
            "driver": driver,
            "pickup_location": "kollam",
            "drop_off_location": "kochi"
        }

    def test_create_ride(self):

        ride = Rides.objects.create(**self.ride_data)

        self.assertEqual(ride.driver, self.ride_data['driver'])
        self.assertEqual(ride.pickup_location, self.ride_data['pickup_location'])
        self.assertEqual(ride.drop_off_location, self.ride_data['drop_off_location'])
