from rest_framework.routers import DefaultRouter
from core.views.medication_view import MedicationViewSet

routers = DefaultRouter()
routers.register(r'medications', MedicationViewSet, basename='medications')

urlpatterns = routers.urls