from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import InventoryItem, Category

User = get_user_model()

class InventoryChangeLogTests(TestCase):

    def setUp(self):
        self.owner = User.objects.create_user(username='testuser', password='password')
        self.category = Category.objects.create(name='Test Category')
        self.item = InventoryItem.objects.create(
            name="Test Item",
            quantity=10,
            price=9.9,
            category=self.category,
            owner=self.owner
        )

    def test_inventory_change_log_creation(self):
        pass

    def test_inventory_change_log_not_created_on_no_change(self):
        pass

    def test_inventory_change_log_on_sale(self):
        pass

    def test_inventory_change_log_on_sale_removal(self):
        pass
