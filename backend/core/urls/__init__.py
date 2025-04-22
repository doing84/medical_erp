from django.urls import path, include

urlpatterns = [
    path('', include('core.urls.patient_urls')),
    path('', include('core.urls.appointment_urls')),
    path('', include('core.urls.billing_urls')),
    path('', include('core.urls.dispense_log_urls')),
    path('', include('core.urls.inventory_urls')),
    path('', include('core.urls.medication_urls')),
    path('', include('core.urls.treatment_medication_urls')),
    path('', include('core.urls.treatment_record_urls')),
    path('', include('core.urls.user_urls')),
]