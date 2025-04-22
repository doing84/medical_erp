from rest_framework.routers import DefaultRouter
from core.views.patient_view import PatientViewSet

routers = DefaultRouter()
routers.register(r'patients', PatientViewSet, basename='patients')

urlpatterns = routers.urls