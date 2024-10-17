from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from inventory.models import InventoryItem, CustomUser, Category  # Import your models


class InventoryItemViewSetTestCase(APITestCase):
    def setUp(self):
        # Create a custom user to authenticate API requests
        self.user = CustomUser.objects.create_user(username='testuser', password='testpass')
        
        # Create a token for the user
        response = self.client.post(reverse('login'), {'username': 'testuser', 'password': 'testpass'})
        self.token = response.data['token']

        # Create a category for the inventory items
        self.category = Category.objects.create(name='Test Category')

        # Create some inventory items for testing
        self.item1 = InventoryItem.objects.create(name='Item 1', quantity=10, price=100, category=self.category)
        self.item2 = InventoryItem.objects.create(name='Item 2', quantity=20, price=200, category=self.category)

    def authenticate(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token)

    def test_inventory_list(self):
        """Test the inventory list view."""
        # Authenticate
        self.authenticate()

        # Send GET request to the inventory list endpoint
        url = reverse('inventory-list')
        response = self.client.get(url)

        # Check that the response is successful
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Check that the response contains the correct number of inventory items
        self.assertEqual(len(response.data), 2)

    def test_inventory_detail(self):
        """Test the inventory detail view."""
        # Authenticate
        self.authenticate()

        # Send GET request to the inventory detail endpoint for item1
        url = reverse('inventory-detail', kwargs={'pk': self.item1.pk})
        response = self.client.get(url)

        # Check that the response is successful
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Check that the response contains the correct item data
        self.assertEqual(response.data['name'], self.item1.name)
        self.assertEqual(response.data['quantity'], self.item1.quantity)
        self.assertEqual(response.data['price'], self.item1.price)

    def test_create_inventory_item(self):
        """Test the creation of an inventory item via the API."""
        # Authenticate
        self.authenticate()

        # Send POST request to create a new inventory item
        url = reverse('inventory-list')
        data = {'name': 'New Item', 'quantity': 30, 'price': 300, 'category': self.category.pk}
        response = self.client.post(url, data, format='json')

        # Check that the item was created successfully
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(InventoryItem.objects.count(), 3)  # There were 2 items before

    def test_update_inventory_item(self):
        """Test the update of an inventory item via the API."""
        # Authenticate
        self.authenticate()

        # Send PUT request to update item1
        url = reverse('inventory-detail', kwargs={'pk': self.item1.pk})
        data = {'name': 'Updated Item 1', 'quantity': 15, 'price': 150, 'category': self.category.pk}
        response = self.client.put(url, data, format='json')

        # Check that the item was updated successfully
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Check that the item was updated in the database
        self.item1.refresh_from_db()
        self.assertEqual(self.item1.name, 'Updated Item 1')
        self.assertEqual(self.item1.quantity, 15)
        self.assertEqual(self.item1.price, 150)
        self.assertEqual(self.item1.category, self.category)

    def test_delete_inventory_item(self):
        """Test the deletion of an inventory item via the API."""
        # Authenticate
        self.authenticate()

        # Send DELETE request to delete item1
        url = reverse('inventory-detail', kwargs={'pk': self.item1.pk})
        response = self.client.delete(url)

        # Check that the item was deleted successfully
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(InventoryItem.objects.count(), 1)  # 1 item remains after deletion