from rest_framework import viewsets
from core.models import TreatmentMedication
from core.serializers.treatment_medication import TreatmentMedicationSerializer

class TreatmentMedicationViewSet(viewsets.ModelViewSet):
    queryset = TreatmentMedication.objects.all()
    serializer_class = TreatmentMedicationSerializer
    