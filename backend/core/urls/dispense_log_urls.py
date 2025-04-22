from rest_framework.routers import DefaultRouter
from core.views.dispense_log_view import DispenseLogViewSet

routers = DefaultRouter()
routers.register(r'dispense_logs', DispenseLogViewSet, basename='dispense_logs')

urlpatterns = routers.urls
