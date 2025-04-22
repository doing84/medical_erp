from rest_framework.routers import DefaultRouter
from core.views.treatment_medication_view import TreatmentMedicationViewSet

routers = DefaultRouter()
routers.register(r'treatment-medications', TreatmentMedicationViewSet, basename='treatment-medications')    

urlpatterns = routers.urls