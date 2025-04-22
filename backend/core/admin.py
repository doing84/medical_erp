from rangefilter.filters import DateRangeFilter
from django.utils.translation import gettext_lazy as _
from django.contrib import admin
from core.models.patient import Patient
from core.models.appointment import Appointment
from core.models.billing import Billing
from core.models.dispense_log import DispenseLog
from core.models.treatment_record import TreatmentRecord
from core.models.treatment_medication import TreatmentMedication
from core.models.inventory import Inventory
from core.models.medication import Medication
from core.models.user import User
from django.contrib.auth.admin import UserAdmin


@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'gender', 'birthday', 'phone', 'address', 'created_dt')
    search_fields = ('name', 'phone')
    list_filter = ('gender',)
    ordering = ('-created_dt',)
    readonly_fields = ('created_dt', 'updated_dt', 'deleted_dt')


@admin.action(description="선택된 예약을 '완료'로 변경")
def mark_as_completed(modeladmin, request, queryset):
    updated = queryset.update(appointment_status='completed')
    modeladmin.message_user(request, f"{updated}건의 예약이 '완료' 상태로 변경되었습니다.")

@admin.action(description="선택된 예약을 '취소'로 변경")
def mark_as_canceled(modeladmin, request, queryset):
    updated = queryset.update(appointment_status='canceled')
    modeladmin.message_user(request, f"{updated}건의 예약이 '취소' 상태로 변경되었습니다.")

@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'patient', 'creator', 'appointment_dt', 'appointment_status', 'created_dt')
    search_fields = ('patient__name', 'patient__phone')
    list_filter = ('appointment_status', 'appointment_dt')
    ordering = ('-appointment_dt',)
    readonly_fields = ('created_dt', 'updated_dt', 'deleted_dt')    
    actions = [mark_as_completed, mark_as_canceled]


@admin.register(Billing)
class BillingAdmin(admin.ModelAdmin):
    list_display = ('id', 'treatment_record', 'creator', 'total_amount', 'paid_amount', 'payment_method', 'paid_dt')
    search_fields = ('treatment_record__patient__name',)
    list_filter = ('payment_method', 'paid_dt')
    ordering = ('-paid_dt',)
    readonly_fields = ('created_dt', 'updated_dt', 'deleted_dt')


@admin.register(DispenseLog)
class DispenseLogAdmin(admin.ModelAdmin):
    list_display = ('id', 'medication', 'treatment_medication', 'quantity', 'dispensed_dt', 'creator')
    search_fields = ('medication__name', 'patient__name')
    list_filter = ('dispensed_dt',)
    ordering = ('-dispensed_dt',)
    readonly_fields = ('created_dt', 'updated_dt', 'deleted_dt')


@admin.register(Inventory)
class InventoryAdmin(admin.ModelAdmin):
    list_display = ('medication', 'quantity', 'created_dt')
    search_fields = ('medication__name',)
    ordering = ('-created_dt',)
    readonly_fields = ('created_dt', 'updated_dt', 'deleted_dt')


@admin.register(Medication)
class MedicationAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'code', 'unit', 'created_dt')
    search_fields = ('name', 'code')
    ordering = ('-created_dt',)
    readonly_fields = ('created_dt', 'updated_dt', 'deleted_dt')


@admin.register(TreatmentMedication)
class TreatmentMedicationAdmin(admin.ModelAdmin):
    list_display = ('id', 'treatment_record', 'medication', 'dose', 'frequency', 'duration')
    search_fields = ('medication__name', 'treatment_record__patient__name')
    ordering = ('-created_dt',)
    readonly_fields = ('created_dt', 'updated_dt', 'deleted_dt')


class TreatmentMedicationInline(admin.StackedInline):
    model = TreatmentMedication
    extra = 0 
    min_num = 1
    class Media:
        css = {
            'all': ('custom_admin.css',) 
        }
    fields = ('medication', 'dose', 'frequency', 'duration', 'memo')
    autocomplete_fields = ('medication',)


@admin.register(TreatmentRecord)
class TreatmentRecordAdmin(admin.ModelAdmin):
    list_display = ('id', 'patient', 'appointment', 'creator', 'diagnosis', 'treatment_dt')
    search_fields = ('patient__name',)
    ordering = ('-treatment_dt',)
    inlines = [TreatmentMedicationInline]
    readonly_fields = ('created_dt', 'updated_dt', 'deleted_dt')


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ('username', 'email', 'role', 'phone', 'is_active', 'is_staff')
    search_fields = ('username', 'email', 'phone')
    list_filter = ('role', 'is_staff')
    readonly_fields = ('date_joined', 'last_login')

    fieldsets = UserAdmin.fieldsets + (
        (_('추가 정보'), {'fields': ('role', 'phone', 'memo')}),
    )

    add_fieldsets = UserAdmin.add_fieldsets + (
        (_('추가 정보'), {'fields': ('role', 'phone', 'memo')}),
    )