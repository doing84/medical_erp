from rest_framework import viewsets
from core.models import TreatmentRecord
from core.serializers.treatment_record import TreatmentRecordSerializer

class TreatmentRecordViewSet(viewsets.ModelViewSet):
    queryset = TreatmentRecord.objects.all()
    serializer_class = TreatmentRecordSerializer