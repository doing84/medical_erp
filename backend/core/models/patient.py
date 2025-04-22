from django.db import models
from .base import TimeStampedModel

class Patient(TimeStampedModel):
    id = models.BigAutoField(primary_key=True)

    name = models.CharField(
        "이름", max_length=20,
        help_text="환자의 이름"
    )
    birthday = models.DateField(
        "생년월일",
        help_text="환자의 생년월일 (YYYY-MM-DD)"
    )

    gender_choices = [
        ('M', '남성'),
        ('F', '여성'), 
        ('O', '기타'),
    ]
    gender = models.CharField(
        "성별", max_length=1, choices=gender_choices,
        help_text="M: 남성, F: 여성, O: 기타 중 하나 선택"
    )

    phone = models.CharField(
        "전화번호", max_length=20,
        help_text="휴대폰 번호 또는 유선전화 번호"
    )
    address = models.CharField(
        "주소", max_length=100,
        help_text="거주지 주소 (도로명 주소 권장)"
    )

    