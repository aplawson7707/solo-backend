from rest_framework import viewsets
from rest_framework import permissions
from .models import ShoppingListItems, Test
from .serializers import (
    TestSerializer,
    ShoppingListItemSerializer,
)


class TestViewSet(viewsets.ModelViewSet):
    queryset = Test.objects.all()
    serializer_class = TestSerializer
    permission_classes = [permissions.IsAuthenticated]
    filterset_fields = [
        'id',
        'title',
        'created_at',
    ]


class ShoppingListItemViewSet(viewsets.ModelViewSet):
    queryset = ShoppingListItems.objects.filter(active=True)
    serializer_class = ShoppingListItemSerializer
    filterset_fields = [
        'id',
        'item_name',
        'category',
        'approx_cost',
        'quantity',
        'active',
        'created_at',
    ]
