from django.db import models
from .base import TimeStampedModel
from .patient import Patient
from .user import User

class Appointment(TimeStampedModel):
    id = models.BigAutoField(primary_key=True)         
    patient = models.ForeignKey(
        Patient, 
        on_delete=models.SET_NULL,
        null=True,
        blank=True,        
        related_name='appointments',
        verbose_name='환자',
        db_index=False,        
    )
    
    creator = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='creator_appointment_records',
        verbose_name='생성자',
        db_index=False,
    )

    doctor = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='doctor_appointment_records',
        verbose_name='담당의사',
        db_index=False,
    )

    appointment_dt = models.DateTimeField("예약일시")

    status_choices = [
        ('scheduled', '예약'),
        ('completed', '완료'),
        ('canceled', '취소'),
    ]

    appointment_status = models.CharField("예약상태", max_length=10, choices=status_choices, default='scheduled')

    memo = models.TextField("메모", blank=True, null=True)

    class Meta:
        db_table = 'appointment'
        verbose_name = '예약'
        verbose_name_plural = '예약 목록'
        ordering = ['-appointment_dt']

        indexes = [
            models.Index(fields=["patient"], name="idx_appmnt_patient"),            
        ]

    def __str__(self):
        patient_name = self.patient.name if self.patient else "Unknown"
        return f"{patient_name} - {self.appointment_dt.strftime('%Y-%m-%d %H:%M')}"