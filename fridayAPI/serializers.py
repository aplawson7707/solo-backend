from rest_framework import serializers
from .models import (
    Test,
    ShoppingListItems,
)


class TestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Test
        fields = '__all__'


class ShoppingListItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShoppingListItems
        fields = '__all__'