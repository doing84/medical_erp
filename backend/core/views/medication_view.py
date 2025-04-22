from rest_framework import viewsets
from core.models import Medication
from core.serializers.medication import MedicationSerializer

class MedicationViewSet(viewsets.ModelViewSet):
    queryset = Medication.objects.all()
    serializer_class = MedicationSerializer
    
