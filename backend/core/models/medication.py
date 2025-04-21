from django.db import models
from .base import TimeStampedModel

class Medication(TimeStampedModel):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField("약품명", max_length=50)
    code= models.CharField("약품코드", max_length=30, null=True, blank=True)
    unit = models.CharField("단위", max_length=10, null=True, blank=True)
    description = models.TextField("약품 설명", null=True, blank=True)

    class Meta:
        db_table = "medication"
        verbose_name = "약품"
        verbose_name_plural = "약품 목록"

    def __str__(self):
        return f"{self.name} ({self.code})"