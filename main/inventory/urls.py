from django.urls import path
from .views import InventoryItemListView, InventoryItemDetailView, CategoryListCreateView, CatagoryDetailView, RegisterUserView, LoginUserView


urlpatterns = [
    path('inventory/', InventoryItemListView.as_view(), name='inventory-list'),   # For listing/creating inventory items
    path('inventory/<int:pk>/', InventoryItemDetailView.as_view(), name='inventory-detail'), 
    path('categories/', CategoryListCreateView.as_view(), name='category-list-create'),
    path('categories/<int:pk>/', CatagoryDetailView.as_view(), name='category-detail'), 
    path('register/', RegisterUserView.as_view(), name='register'),
    path('login/', LoginUserView.as_view(), name='login'),

]
