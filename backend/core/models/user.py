from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    USER_ROLE_CHOICES = [
        ('doctor', '의사'),
        ('nurse', '간호사'),
        ('admin', '관리자'),
        ('staff', '기타 직원')
    ]

    role = models.CharField("역할", max_length=20, choices=USER_ROLE_CHOICES)
    phone = models.CharField("전화번호", max_length=20, null=True, blank=True)
    memo = models.TextField("메모", null=True, blank=True)

    class Meta:
        db_table = 'user'
        verbose_name = '사용자'
        verbose_name_plural = '사용자 목록'

    def __str__(self):
       return f"{self.username} ({self.get_role_display()})"