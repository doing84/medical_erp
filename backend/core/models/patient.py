from django.db import models
from .base import TimeStampedModel

class Patient(TimeStampedModel):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField("이름", max_length=20)
    birthday  = models.DateField("생년월일")

    gender_choices = [
        ('M', '남성'),
        ('F', '여성'), 
        ('O', '기타'),
    ]
    gender = models.CharField("성별", max_length=1, choices=gender_choices)
    phone = models.CharField("전화번호", max_length=20)
    address = models.CharField("주소", max_length=100)    

    class Meta:
        db_table = "patient"
        verbose_name = "환자"
        verbose_name_plural = "환자 목록"
    
    def __str__(self):
        return f"{self.name} ({self.birthday})"
    