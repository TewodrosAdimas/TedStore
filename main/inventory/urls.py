from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    InventoryItemViewSet,
    CategoryViewSet,
    RegisterUserView,
    LoginUserView,
    InventoryLevelView
)

# Create a router and register your viewsets
router = DefaultRouter()
router.register(r'inventory', InventoryItemViewSet, basename='inventory')
router.register(r'categories', CategoryViewSet, basename='category')

urlpatterns = [
    path('', include(router.urls)),  # This will include the router paths
    path('register/', RegisterUserView.as_view(), name='register'),
    path('login/', LoginUserView.as_view(), name='login'),
    path('inventory-levels/', InventoryLevelView.as_view(), name='inventory-levels'),
]
