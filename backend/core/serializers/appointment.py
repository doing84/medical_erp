from rest_framework import serializers
from core.models import Appointment
from django.utils import timezone

class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = '__all__'
        extra_kwargs = {
            'id': {'read_only': True},
            'created_dt': {'read_only': True},
            'updated_dt': {'read_only': True},
            'deleted_dt': {'read_only': True},
        }

    def validate_appointment_dt(self, value):   
        if value < timezone.now():
            raise serializers.ValidationError("예약 시간은 현재 시간 이후여야 합니다.")
        return value
