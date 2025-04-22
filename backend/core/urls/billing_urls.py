from rest_framework.routers import DefaultRouter
from core.views.billing_view import BillingViewSet

routers = DefaultRouter()
routers.register(r'billings', BillingViewSet, basename='billings')

urlpatterns = routers.urls