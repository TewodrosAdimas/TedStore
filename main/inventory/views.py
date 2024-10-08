from rest_framework import generics, permissions
from .models import InventoryItem, Category, CustomUser
from .serializers import InventoryItemSerializer, CategorySerializer, CustomUserSerializer, LoginSerializer, InventoryLevelSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from rest_framework import viewsets
from rest_framework.views import APIView
from django_filters import rest_framework as filters
from rest_framework import generics


class UserListCreateView(generics.ListCreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [permissions.AllowAny]  # Allow anyone to create a user


class InventoryItemViewSet(viewsets.ModelViewSet):
    queryset = InventoryItem.objects.all()
    serializer_class = InventoryItemSerializer
    permission_classes = [IsAuthenticated]  # Only authenticated users can access this

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)  # Associate inventory items with the user

class InventoryItemDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = InventoryItem.objects.all()
    serializer_class = InventoryItemSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Ensure users can only manage their own inventory items
        return self.queryset.filter(owner=self.request.user)

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Ensure users can only manage their own inventory items
        return self.queryset.filter(owner=self.request.user)

class CatagoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = InventoryItem.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Ensure users can only manage their own inventory items
        return self.queryset.filter(owner=self.request.user)



class RegisterUserView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [permissions.AllowAny]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=201)
class LoginUserView(generics.GenericAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = LoginSerializer  # Specify the serializer class

    def post(self, request, *args, **kwargs):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        
        if user is not None:
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            })
        else:
            return Response({'error': 'Invalid credentials'}, status=400)

class InventoryLevelView(APIView):
    permission_classes = [IsAuthenticated]  # Ensure only authenticated users can access this

    def get(self, request):
        inventory_items = InventoryItem.objects.all()  # Get all inventory items
        serializer = InventoryLevelSerializer(inventory_items, many=True)  # Serialize the data
        return Response(serializer.data)


class InventoryLevelFilter(filters.FilterSet):
    category = filters.ModelChoiceFilter(queryset=Category.objects.all())
    min_price = filters.NumberFilter(field_name='price', lookup_expr='gte')
    max_price = filters.NumberFilter(field_name='price', lookup_expr='lte')
    low_stock = filters.BooleanFilter(method='filter_low_stock')

    class Meta:
        model = InventoryItem
        fields = ['category', 'min_price', 'max_price']

    def filter_low_stock(self, queryset, name, value):
        if value:
            return queryset.filter(quantity__lt=10)  # Change the threshold as needed
        return queryset





class InventoryLevelFilter(filters.FilterSet):
    category = filters.ModelChoiceFilter(queryset=Category.objects.all())
    min_price = filters.NumberFilter(field_name='price', lookup_expr='gte')
    max_price = filters.NumberFilter(field_name='price', lookup_expr='lte')
    low_stock = filters.BooleanFilter(method='filter_low_stock')

    class Meta:
        model = InventoryItem
        fields = ['category', 'min_price', 'max_price']

    def filter_low_stock(self, queryset, name, value):
        if value:
            return queryset.filter(quantity__lt=10)  # Change the threshold as needed
        return queryset


class InventoryLevelView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]  # Ensure only authenticated users can access this
    serializer_class = InventoryLevelSerializer
    filterset_class = InventoryLevelFilter

    def get_queryset(self):
        queryset = InventoryItem.objects.all()
        
        # Filtering by the owner
        queryset = queryset.filter(owner=self.request.user)

        # Apply the filters if provided in the request
        return self.filterset_class(self.request.GET, queryset=queryset).qs
