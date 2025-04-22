from rest_framework.routers import DefaultRouter
from core.views.treatment_record_view import TreatmentRecordViewSet

routers = DefaultRouter()
routers.register(r'treatment_records', TreatmentRecordViewSet, basename='treatment_records')

urlpatterns = routers.urls
