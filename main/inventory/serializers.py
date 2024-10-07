from rest_framework import serializers
from .models import InventoryItem, Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']

class InventoryItemSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)  # Nested serializer for category
    category_id = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all(), write_only=True)

    class Meta:
        model = InventoryItem
        fields = ['id', 'name', 'description', 'quantity', 'price', 'category', 'category_id', 'date_added', 'last_updated']

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
        # Update each field with the validated data, or retain the current value if not provided
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.quantity = validated_data.get('quantity', instance.quantity)
        instance.price = validated_data.get('price', instance.price)
        
        # Update the category (if provided)
        instance.category = validated_data.get('category_id', instance.category)
        
        # Save the updated instance
        instance.save()
        return instance

