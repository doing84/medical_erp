from django.db import models
from .base import TimeStampedModel
from .treatment_record import TreatmentRecord
from .medication import Medication

class TreatmentMedication(TimeStampedModel):
    id = models.BigAutoField(primary_key=True)

    treatment_record = models.ForeignKey(
        TreatmentRecord,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='treatment_medications',
        verbose_name='진료기록',
        db_index=False,
    )

    medication = models.ForeignKey(
        Medication,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='treatment_medications',
        verbose_name='약품',
        db_index=False,
    )

    dose = models.CharField("복용량", max_length=50)
    frequency = models.CharField("복용횟수", max_length=50)
    duration = models.CharField("복용기간", max_length=20)
    memo = models.TextField("메모", null=True, blank=True)

    class Meta:
        db_table = 'treatment_medication'
        verbose_name = '처방약'
        verbose_name_plural = '처방약 목록'
        constraints = [
            models.UniqueConstraint(fields=['treatment_record', 'medication'], 
            name='unique_treatment_med')
            ]
        indexes = [
            models.Index(fields=["treatment_record"], name="idx_trtmnt_medic_trtmnt_record"),
            models.Index(fields=["medication"], name="idx_trtmnt_medic_medic")
        ]
        ordering = ['-created_dt']
    
    def __str__(self):
        return f"{self.medication.name} - {self.dose} / {self.frequency} / {self.duration}"