from rest_framework import serializers
from .models import InventoryItem, Category, InventoryChangeLog
from django.contrib.auth import get_user_model

User = get_user_model()

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']
        # extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User(
            username=validated_data['username'],
            email=validated_data['email']
        )
        user.set_password(validated_data['password'])  # Use set_password to hash the password
        user.save()
        return user

    def update(self, instance, validated_data):
        instance.username = validated_data.get('username', instance.username)
        instance.email = validated_data.get('email', instance.email)
        
        if 'password' in validated_data:
            instance.set_password(validated_data['password'])  # Hash the password

        instance.save()
        return instance


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'owner']
        read_only_fields = ['owner']

        def create(self, validated_data):
            validated_data['owner'] = self.context['request'].user
            return super().create(validated_data)
class InventoryItemSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)  # Nested serializer for category
    category_id = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all(), write_only=True)

    class Meta:
        model = InventoryItem
        fields = ['id', 'name', 'description', 'quantity', 'price', 'category', 'category_id', 'date_added', 'last_updated', 'owner']
        read_only_fields = ['owner']
    def create(self, validated_data):
        validated_data['owner'] = self.context['request'].user
        return super().create(validated_data)
    
    def validate_quantity(self, value):
        if value < 0:
            raise serializers.ValidationError('Quantity cannot be negative.')
        return value

    def validate_price(self, value):
        if value < 0:
            raise serializers.ValidationError('Price cannot be negative.')
        return value

    def create(self, validated_data):
        category = validated_data.pop('category_id')
        return InventoryItem.objects.create(category=category, **validated_data)

    def update(self, instance, validated_data):
        # Track changes for quantity
        old_quantity = instance.quantity

        # Update each field with the validated data, or retain the current value if not provided
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.price = validated_data.get('price', instance.price)
        
        # Update the category (if provided)
        instance.category = validated_data.get('category_id', instance.category)
        
        # Check if the quantity has changed, and log it if necessary
        new_quantity = validated_data.get('quantity', instance.quantity)
        if new_quantity != old_quantity:
            quantity_change = new_quantity - old_quantity
            InventoryChangeLog.objects.create(
                item=instance,
                quantity_changed=quantity_change,
                change_type='restock' if quantity_change > 0 else 'sale',
                changed_by=self.context['request'].user
            )

        # Save the updated instance
        instance.quantity = new_quantity
        instance.save()
        return instance



class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True)


class InventoryLevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = InventoryItem
        fields = ['id', 'name', 'quantity']  # Only include the fields you want to display

    
class InventoryChangeLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = InventoryChangeLog
        fields = ['id', 'item', 'quantity_changed', 'change_type', 'date_changed', 'changed_by']