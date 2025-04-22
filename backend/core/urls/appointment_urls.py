from rest_framework.routers import DefaultRouter
from core.views.appointment_view import AppointmentViewSet

routers = DefaultRouter()
routers.register(r'appointments', AppointmentViewSet, basename='appointments')

urlpatterns = routers.urls
