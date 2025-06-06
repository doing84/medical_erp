# Generated by Django 5.2 on 2025-04-21 14:42

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_remove_appointment_created_by_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='creator',
            field=models.ForeignKey(blank=True, db_index=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='creator_appointment_records', to=settings.AUTH_USER_MODEL, verbose_name='생성자'),
        ),
        migrations.AlterField(
            model_name='billing',
            name='creator',
            field=models.ForeignKey(blank=True, db_index=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='creator_billings', to=settings.AUTH_USER_MODEL, verbose_name='생성자'),
        ),
        migrations.AlterField(
            model_name='dispenselog',
            name='creator',
            field=models.ForeignKey(blank=True, db_index=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='creator_dispenselog_records', to=settings.AUTH_USER_MODEL, verbose_name='생성자'),
        ),
        migrations.AlterField(
            model_name='treatmentrecord',
            name='creator',
            field=models.ForeignKey(blank=True, db_index=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='creator_treatment_records', to=settings.AUTH_USER_MODEL, verbose_name='생성자'),
        ),
        migrations.AddIndex(
            model_name='appointment',
            index=models.Index(fields=['patient'], name='idx_appmnt_patient'),
        ),
        migrations.AddIndex(
            model_name='billing',
            index=models.Index(fields=['treatment_record'], name='idx_bill_trtmnt_record'),
        ),
        migrations.AddIndex(
            model_name='dispenselog',
            index=models.Index(fields=['treatment_medication'], name='idx_disp_log_trtmnt_medic'),
        ),
        migrations.AddIndex(
            model_name='dispenselog',
            index=models.Index(fields=['medication'], name='idx_disp_log_medic'),
        ),
        migrations.AddIndex(
            model_name='inventory',
            index=models.Index(fields=['medication'], name='idx_inven_medic'),
        ),
        migrations.AddIndex(
            model_name='treatmentmedication',
            index=models.Index(fields=['treatment_record'], name='idx_trtmnt_medic_trtmnt_record'),
        ),
        migrations.AddIndex(
            model_name='treatmentmedication',
            index=models.Index(fields=['medication'], name='idx_trtmnt_medic_medic'),
        ),
        migrations.AddIndex(
            model_name='treatmentrecord',
            index=models.Index(fields=['patient'], name='idx_trtmnt_record_patient'),
        ),
        migrations.AddIndex(
            model_name='treatmentrecord',
            index=models.Index(fields=['appointment'], name='idx_trtmnt_record_appmnt'),
        ),
    ]
