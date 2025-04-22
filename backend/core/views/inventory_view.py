from rest_framework import viewsets
from core.models import Inventory
from core.serializers.inventory import InventorySerializer

class InventoryViewSet(viewsets.ModelViewSet):
    queryset = Inventory.objects.all()
    serializer_class = InventorySerializer
    