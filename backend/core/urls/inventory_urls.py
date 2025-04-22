from rest_framework.routers import DefaultRouter
from core.views.inventory_view import InventoryViewSet

routers = DefaultRouter()
routers.register(r'inventory', InventoryViewSet, basename='inventory')

urlpatterns = routers.urls