from django.db import models
from .base import TimeStampedModel
from .treatment_record import TreatmentRecord
from .user import User


class Billing(TimeStampedModel):
    id = models.BigAutoField(primary_key=True)

    treatment_record = models.OneToOneField(
        TreatmentRecord,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='billings',
        verbose_name='진료기록',
        db_index=False,
    )

    creator = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='creator_billings',
        verbose_name='생성자',
        db_index=False,
    )

    PAYMENT_METHOD_CHOICES = [
        ('cash', '현금'),
        ('card', '카드'),
        ('transfer', '계좌이체'),
    ]

    total_amount = models.PositiveIntegerField("총 금액")
    paid_amount = models.PositiveIntegerField("결제 금액", default=0)
    payment_method = models.CharField("결제 수단", max_length=20, choices=PAYMENT_METHOD_CHOICES)
    paid_dt = models.DateTimeField("결제 일시")
    memo = models.TextField("메모", null=True, blank=True)

    class Meta:
        db_table = 'billing'
        verbose_name = '수납'
        verbose_name_plural = '수납 목록'
        ordering = ['-paid_dt']

        indexes = [
            models.Index(fields=['treatment_record'], name='idx_bill_trtmnt_record'),         
        ]

    def __str__(self):
        patient_name = self.treatment_record.patient.name if self.treatment_record and self.treatment_record.patient else "Unknown"
        return f"{patient_name} - {self.total_amount}원 결제 ({self.paid_dt.strftime('%Y-%m-%d')})"
