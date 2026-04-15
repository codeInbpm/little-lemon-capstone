from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import MenuItem

class MenuItemTest(TestCase):
    def test_menu_item_list(self):
        client = APIClient()
        response = client.get('/api/menu-items/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_booking_requires_auth(self):
        client = APIClient()
        response = client.get('/api/bookings/')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)