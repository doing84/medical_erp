from rest_framework import viewsets
from core.models import Billing
from core.serializers.billing import BillingSerializer

class BillingViewSet(viewsets.ModelViewSet):
    queryset = Billing.objects.all()
    serializer_class = BillingSerializer

    