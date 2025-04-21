from django.db import models
from .base import TimeStampedModel
from .medication import Medication

class Inventory(TimeStampedModel):
    medication = models.OneToOneField(
        Medication,
        primary_key=True,
        on_delete=models.CASCADE,
        related_name='inventory',
        verbose_name='약품',
        db_index=False,
    )

    quantity = models.PositiveIntegerField("수량")
    
    class Meta:
        db_table = 'inventory'
        verbose_name = '재고'
        verbose_name_plural = '재고 목록'

        indexes = [
            models.Index(fields=['medication'], name='idx_inven_medic'),
        ]

    def __str__(self):
        med = self.medication.name if self.medication else "Unknown"
        return f"{med} - 재고: {self.quantity}"
