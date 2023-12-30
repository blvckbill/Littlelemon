from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from Restaurant.models import Menu
from Restaurant.serializers import MenuItemSerializer
class MenuViewTest(TestCase):
    def setup(self):
        Menu.objects.create(Title='Plantain', Price=24, Inventory=4)

    def test_getall(self):
        url = reverse('menu_list')
        client = APIClient()
        response = client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        expected_data = MenuItemSerializer(Menu.objects.all(), many=True).data
        self.assertEqual(response.data, expected_data)