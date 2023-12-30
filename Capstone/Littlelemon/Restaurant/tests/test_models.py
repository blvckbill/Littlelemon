from django.test import TestCase
from Restaurant.models import Menu

class MenuTest(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(Title='IceCream', Price=12, Inventory=2)
        self.assertEqual(str(item), "IceCream : 12")