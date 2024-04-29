from ride_app.models import Rides
from django.contrib.auth.models import User
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from django.urls import reverse

class RideListViewTestCase(APITestCase):

    def setUp(self):
        self.rider = User.objects.create_user(username='test_rider', password='testpwd')
        self.client.force_authenticate(user=self.rider)

        self.driver = User.objects.create_user(username='test_driver', password='testpwd')
        ride_data = {"driver": self.driver,
                     "pickup_location": "kollam",
                     "drop_off_location": "kochi"
                     }
        self.ride = Rides.objects.create(**ride_data)

    def test_get_ride_list(self):
        url = reverse('ride-list')
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]["status"], Rides.Ride_Status.AVAILABLE)
        self.assertEqual(len(response.data), 1)


class RideDetailViewTestCase(APITestCase):
    def setUp(self):
        self.rider = User.objects.create_user(username='test_rider', password='testpwd')
        self.client.force_authenticate(user=self.rider)

        self.driver = User.objects.create_user(username='test_driver', password='testpwd')
        ride_data = {"driver": self.driver,
                     "pickup_location": "kollam",
                     "drop_off_location": "kochi"
                     }
        self.ride = Rides.objects.create(**ride_data)

    def test_get_ride_details(self):
        url = reverse('ride-detail', kwargs={'id': self.ride.id})
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['pickup_location'], self.ride.pickup_location)
        self.assertEqual(response.data['drop_off_location'], self.ride.drop_off_location)


class RideRequestViewTestCase(APITestCase):
    def setUp(self):
        self.rider = User.objects.create_user(username='test_rider', password='testpwd')
        self.client.force_authenticate(user=self.rider)

        self.driver = User.objects.create_user(username='test_driver', password='testpwd')
        ride_data = {"driver": self.driver,
                     "pickup_location": "kollam",
                     "drop_off_location": "kochi"
                     }
        self.ride = Rides.objects.create(**ride_data)

    def test_request_ride(self):
        url = reverse('ride-request', kwargs={'id': self.ride.id})
        update_data = {
            "rider": self.rider.id,
            "status": Rides.Ride_Status.REQUESTED
        }
        response = self.client.patch(url, update_data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['rider'], self.rider.id)
        self.assertEqual(response.data['status'], Rides.Ride_Status.REQUESTED)


class UpdateRideStatusViewTestCase(APITestCase):
    def setUp(self):
        self.rider = User.objects.create_user(username='test_rider', password='testpwd')
        self.client.force_authenticate(user=self.rider)

        self.driver = User.objects.create_user(username='test_driver', password='testpwd')
        ride_data = {"driver": self.driver,
                     "pickup_location": "kollam",
                     "drop_off_location": "kochi"
                     }
        self.ride = Rides.objects.create(**ride_data)

    def test_update_ride_status_to_started(self):
        url = reverse('ride-request', kwargs={'id': self.ride.id})
        update_data = {
            "status": Rides.Ride_Status.STARTED
        }
        response = self.client.patch(url, update_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['status'], Rides.Ride_Status.STARTED)
