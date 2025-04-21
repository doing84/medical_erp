from django.db import models
from django.core.exceptions import ObjectDoesNotExist
from .base import TimeStampedModel
from .treatment_medication import TreatmentMedication
from .medication import Medication
from .user import User
from .inventory import Inventory

class DispenseLog(TimeStampedModel):
    treatment_medication = models.ForeignKey(
        TreatmentMedication,
        on_delete=models.CASCADE,
        related_name='dispense_logs',
        verbose_name='처방약',
        db_index=False,
    )

    medication = models.ForeignKey(
        Medication,
        on_delete=models.PROTECT,
        related_name='dispense_logs',
        verbose_name='약품',
        db_index=False,
    )

    creator = models.ForeignKey(
    User,
    on_delete=models.SET_NULL,
    null=True,
    blank=True,
    related_name='creator_dispenselog_records',
    verbose_name='생성자',
    db_index=False,
    )

    quantity = models.PositiveIntegerField("수량")
    dispensed_dt = models.DateTimeField("출고일시")
    memo = models.TextField("메모", null=True, blank=True)

    def save(self, *args, **kwargs):
        if self._state.adding:
            try:
                inventory = Inventory.objects.get(medication=self.medication)
            except ObjectDoesNotExist:
                raise ValueError("해당 약품의 재고 정보가 없습니다.")
            if inventory.quantity < self.quantity:
                raise ValueError("재고가 부족합니다.")
            
            inventory.quantity -= self.quantity
            inventory.save()
            
        super().save(*args, **kwargs)

    class Meta:
        db_table = 'dispense_log'
        verbose_name = '약품 출고 기록'
        verbose_name_plural = '약품 출고 기록 목록'
        constraints = [
            models.UniqueConstraint(
                fields=['treatment_medication', 'medication'],
                name='unique_dispense_per_med'
            )
        ]
        ordering = ['-dispensed_dt']

        indexes = [
            models.Index(fields=['treatment_medication'], name='idx_disp_log_trtmnt_medic'),
            models.Index(fields=['medication'], name='idx_disp_log_medic'),            
        ]

    def __str__(self):
        med = self.medication.name if self.medication else "Unknown"
        return f"{med} - {self.quantity}개 출고 @ {self.dispensed_dt.strftime('%Y-%m-%d %H:%M')}"