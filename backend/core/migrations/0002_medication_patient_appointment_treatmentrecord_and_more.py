# Generated by Django 5.2 on 2025-04-21 14:09

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Medication',
            fields=[
                ('created_dt', models.DateTimeField(auto_now_add=True)),
                ('updated_dt', models.DateTimeField(auto_now=True)),
                ('deleted_dt', models.DateTimeField(blank=True, null=True)),
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50, verbose_name='약품명')),
                ('code', models.CharField(blank=True, max_length=30, null=True, verbose_name='약품코드')),
                ('unit', models.CharField(blank=True, max_length=10, null=True, verbose_name='단위')),
                ('description', models.TextField(blank=True, null=True, verbose_name='약품 설명')),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(class)s_created_by', to=settings.AUTH_USER_MODEL)),
                ('deleted_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(class)s_deleted_by', to=settings.AUTH_USER_MODEL)),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(class)s_updated_by', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '약품',
                'verbose_name_plural': '약품 목록',
                'db_table': 'medication',
            },
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('created_dt', models.DateTimeField(auto_now_add=True)),
                ('updated_dt', models.DateTimeField(auto_now=True)),
                ('deleted_dt', models.DateTimeField(blank=True, null=True)),
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20, verbose_name='이름')),
                ('bitrhday', models.DateField(verbose_name='생년월일')),
                ('gender', models.CharField(choices=[('M', '남성'), ('F', '여성'), ('O', '기타')], max_length=1, verbose_name='성별')),
                ('phone', models.CharField(max_length=20, verbose_name='전화번호')),
                ('address', models.CharField(max_length=100, verbose_name='주소')),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(class)s_created_by', to=settings.AUTH_USER_MODEL)),
                ('deleted_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(class)s_deleted_by', to=settings.AUTH_USER_MODEL)),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(class)s_updated_by', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '환자',
                'verbose_name_plural': '환자 목록',
                'db_table': 'patient',
            },
        ),
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('created_dt', models.DateTimeField(auto_now_add=True)),
                ('updated_dt', models.DateTimeField(auto_now=True)),
                ('deleted_dt', models.DateTimeField(blank=True, null=True)),
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('appointment_dt', models.DateTimeField(verbose_name='예약일시')),
                ('appointment_status', models.CharField(choices=[('scheduled', '예약'), ('completed', '완료'), ('canceled', '취소')], default='scheduled', max_length=10, verbose_name='예약상태')),
                ('memo', models.TextField(blank=True, null=True, verbose_name='메모')),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(class)s_created_by', to=settings.AUTH_USER_MODEL)),
                ('creator', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='creator_appointment_records', to=settings.AUTH_USER_MODEL, verbose_name='생성자')),
                ('deleted_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(class)s_deleted_by', to=settings.AUTH_USER_MODEL)),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(class)s_updated_by', to=settings.AUTH_USER_MODEL)),
                ('patient', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='appointments', to='core.patient', verbose_name='환자')),
            ],
            options={
                'verbose_name': '예약',
                'verbose_name_plural': '예약 목록',
                'db_table': 'appointment',
                'ordering': ['-appointment_dt'],
            },
        ),
        migrations.CreateModel(
            name='TreatmentRecord',
            fields=[
                ('created_dt', models.DateTimeField(auto_now_add=True)),
                ('updated_dt', models.DateTimeField(auto_now=True)),
                ('deleted_dt', models.DateTimeField(blank=True, null=True)),
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('diagnosis', models.CharField(max_length=100, verbose_name='진단명')),
                ('symptoms', models.TextField(blank=True, null=True, verbose_name='증상')),
                ('memo', models.TextField(blank=True, null=True, verbose_name='메모')),
                ('treatment_dt', models.DateTimeField(verbose_name='진료일시')),
                ('appointment', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='treatment_records', to='core.appointment', verbose_name='예약')),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(class)s_created_by', to=settings.AUTH_USER_MODEL)),
                ('creator', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='creator_treatment_records', to=settings.AUTH_USER_MODEL, verbose_name='생성자')),
                ('deleted_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(class)s_deleted_by', to=settings.AUTH_USER_MODEL)),
                ('patient', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='treatment_records', to='core.patient', verbose_name='환자')),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(class)s_updated_by', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '진료 기록',
                'verbose_name_plural': '진료 기록',
                'db_table': 'treatment_record',
                'ordering': ['-treatment_dt'],
            },
        ),
        migrations.CreateModel(
            name='TreatmentMedication',
            fields=[
                ('created_dt', models.DateTimeField(auto_now_add=True)),
                ('updated_dt', models.DateTimeField(auto_now=True)),
                ('deleted_dt', models.DateTimeField(blank=True, null=True)),
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('dose', models.CharField(max_length=50, verbose_name='복용량')),
                ('frequency', models.CharField(max_length=50, verbose_name='복용횟수')),
                ('duration', models.CharField(max_length=20, verbose_name='복용기간')),
                ('memo', models.TextField(blank=True, null=True, verbose_name='메모')),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(class)s_created_by', to=settings.AUTH_USER_MODEL)),
                ('deleted_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(class)s_deleted_by', to=settings.AUTH_USER_MODEL)),
                ('medication', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='treatment_medications', to='core.medication', verbose_name='약품')),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(class)s_updated_by', to=settings.AUTH_USER_MODEL)),
                ('treatment_record', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='treatment_medications', to='core.treatmentrecord', verbose_name='진료기록')),
            ],
            options={
                'verbose_name': '처방약',
                'verbose_name_plural': '처방약 목록',
                'db_table': 'treatment_medication',
                'ordering': ['-created_dt'],
            },
        ),
        migrations.CreateModel(
            name='Billing',
            fields=[
                ('created_dt', models.DateTimeField(auto_now_add=True)),
                ('updated_dt', models.DateTimeField(auto_now=True)),
                ('deleted_dt', models.DateTimeField(blank=True, null=True)),
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('total_amount', models.PositiveIntegerField(verbose_name='총 금액')),
                ('paid_amount', models.PositiveIntegerField(default=0, verbose_name='결제 금액')),
                ('payment_method', models.CharField(choices=[('cash', '현금'), ('card', '카드'), ('transfer', '계좌이체')], max_length=20, verbose_name='결제 수단')),
                ('paid_dt', models.DateTimeField(verbose_name='결제 일시')),
                ('memo', models.TextField(blank=True, null=True, verbose_name='메모')),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(class)s_created_by', to=settings.AUTH_USER_MODEL)),
                ('creator', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='creator_billings', to=settings.AUTH_USER_MODEL, verbose_name='생성자')),
                ('deleted_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(class)s_deleted_by', to=settings.AUTH_USER_MODEL)),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(class)s_updated_by', to=settings.AUTH_USER_MODEL)),
                ('treatment_record', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='billings', to='core.treatmentrecord', verbose_name='진료기록')),
            ],
            options={
                'verbose_name': '수납',
                'verbose_name_plural': '수납 목록',
                'db_table': 'billing',
                'ordering': ['-paid_dt'],
            },
        ),
        migrations.CreateModel(
            name='Inventory',
            fields=[
                ('created_dt', models.DateTimeField(auto_now_add=True)),
                ('updated_dt', models.DateTimeField(auto_now=True)),
                ('deleted_dt', models.DateTimeField(blank=True, null=True)),
                ('medication', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='inventory', serialize=False, to='core.medication', verbose_name='약품')),
                ('quantity', models.PositiveIntegerField(verbose_name='수량')),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(class)s_created_by', to=settings.AUTH_USER_MODEL)),
                ('deleted_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(class)s_deleted_by', to=settings.AUTH_USER_MODEL)),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(class)s_updated_by', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '재고',
                'verbose_name_plural': '재고 목록',
                'db_table': 'inventory',
            },
        ),
        migrations.CreateModel(
            name='DispenseLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_dt', models.DateTimeField(auto_now_add=True)),
                ('updated_dt', models.DateTimeField(auto_now=True)),
                ('deleted_dt', models.DateTimeField(blank=True, null=True)),
                ('quantity', models.PositiveIntegerField(verbose_name='수량')),
                ('dispensed_dt', models.DateTimeField(verbose_name='출고일시')),
                ('memo', models.TextField(blank=True, null=True, verbose_name='메모')),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(class)s_created_by', to=settings.AUTH_USER_MODEL)),
                ('creator', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='creator_dispenselog_records', to=settings.AUTH_USER_MODEL, verbose_name='생성자')),
                ('deleted_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(class)s_deleted_by', to=settings.AUTH_USER_MODEL)),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(class)s_updated_by', to=settings.AUTH_USER_MODEL)),
                ('medication', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='dispense_logs', to='core.medication', verbose_name='약품')),
                ('treatment_medication', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dispense_logs', to='core.treatmentmedication', verbose_name='처방약')),
            ],
            options={
                'verbose_name': '약품 출고 기록',
                'verbose_name_plural': '약품 출고 기록 목록',
                'db_table': 'dispense_log',
                'ordering': ['-dispensed_dt'],
                'constraints': [models.UniqueConstraint(fields=('treatment_medication', 'medication'), name='unique_dispense_per_med')],
            },
        ),
        migrations.AddConstraint(
            model_name='treatmentmedication',
            constraint=models.UniqueConstraint(fields=('treatment_record', 'medication'), name='unique_treatment_med'),
        ),
    ]
