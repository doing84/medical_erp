from rest_framework import viewsets, filters, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema

from core.models import Appointment
from core.serializers.appointment import AppointmentSerializer

class AppointmentViewSet(viewsets.ModelViewSet):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer

    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['appointment_dt']
    ordering = ['appointment_dt']
    