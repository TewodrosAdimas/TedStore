from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    InventoryItemViewSet,
    CategoryViewSet,
    RegisterUserView,
    LoginUserView,
    InventoryLevelView,
    InventoryChangeLogView
)

# Create a router and register your viewsets
router = DefaultRouter()
router.register(r'inventory', InventoryItemViewSet, basename='inventory')
router.register(r'categories', CategoryViewSet, basename='category')

urlpatterns = [
    # Include router paths
    path('', include(router.urls)),  # Ensure this includes the router

    # Authentication endpoints
    path('register/', RegisterUserView.as_view(), name='register'),
    path('login/', LoginUserView.as_view(), name='login'),

    # Inventory-specific endpoints
    path('inventory-levels/', InventoryLevelView.as_view(), name='inventory-levels'),
    path('inventory/<int:item_id>/change-logs/', InventoryChangeLogView.as_view(), name='inventory-change-logs'),
]
