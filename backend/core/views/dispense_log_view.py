from rest_framework import viewsets
from core.models import DispenseLog
from core.serializers.dispense_log import DispenseLogSerializer

class DispenseLogViewSet(viewsets.ModelViewSet):
    queryset = DispenseLog.objects.all()
    serializer_class = DispenseLogSerializer

    