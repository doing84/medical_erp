from django.db import models
from .patient import Patient
from .appointment import Appointment
from .base import TimeStampedModel
from .user import User

class TreatmentRecord(TimeStampedModel):
    id = models.BigAutoField(primary_key=True)

    patient = models.ForeignKey(
        Patient, 
        on_delete=models.SET_NULL,
        null=True,
        blank=True, 
        related_name='treatment_records',
        verbose_name='환자',
        db_index=False,
        )
    
    appointment = models.ForeignKey(
        Appointment, 
        on_delete=models.SET_NULL,
        null=True,
        blank=True, 
        related_name='treatment_records',
        verbose_name='예약',
        db_index=False,
        )
    
    creator = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='creator_treatment_records',
        verbose_name='생성자',
        db_index=False,
    )
    
    diagnosis = models.CharField("진단명", max_length=100)
    symptoms = models.TextField("증상", null=True, blank=True)
    memo = models.TextField("메모", null=True, blank=True)
    treatment_dt = models.DateTimeField("진료일시")

    class Meta:
        db_table = 'treatment_record'
        verbose_name = '진료 기록'
        verbose_name_plural = '진료 기록'
        ordering = ['-treatment_dt']

        indexes = [            
            models.Index(fields=['patient'], name="idx_trtmnt_record_patient"),
            models.Index(fields=['appointment'], name="idx_trtmnt_record_appmnt"),
        ]

    def __str__(self):
        patient_name = self.patient.name if self.patient else "Unknown"
        return f"{patient_name} - {self.treatment_dt.strftime('%Y-%m-%d %H:%M')}"