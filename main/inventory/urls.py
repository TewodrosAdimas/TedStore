from django.urls import path
from .views import InventoryItemListView, InventoryItemDetailView

urlpatterns = [
    path('inventory/', InventoryItemListView.as_view(), name='inventory-list'),   # For listing/creating inventory items
    path('inventory/<int:pk>/', InventoryItemDetailView.as_view(), name='inventory-detail'),   # For retrieving/updating/deleting an item
]
