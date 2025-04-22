from rest_framework.routers import DefaultRouter
from core.views.user_view import UserViewSet

routers = DefaultRouter()
routers.register(r'users', UserViewSet, basename='users')

urlpatterns = routers.urls