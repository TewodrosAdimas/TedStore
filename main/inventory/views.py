from rest_framework import generics
from .models import InventoryItem
from .serializers import InventoryItemSerializer

# List all inventory items
class InventoryItemListView(generics.ListCreateAPIView):
    queryset = InventoryItem.objects.all()
    serializer_class = InventoryItemSerializer

# Retrieve, update, or delete a single inventory item by ID
class InventoryItemDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = InventoryItem.objects.all()
    serializer_class = InventoryItemSerializer
