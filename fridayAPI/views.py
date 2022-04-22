from rest_framework import viewsets
from rest_framework import permissions
from .models import Test
from .serializers import TestSerializer

class TestViewSet(viewsets.ModelViewSet):
    queryset = Test.objects.all()
    serializer_class = TestSerializer
    permission_classes = [permissions.IsAuthenticated]
    filterset_fields = [
        'id',
        'title',
        'created_at',
    ]
