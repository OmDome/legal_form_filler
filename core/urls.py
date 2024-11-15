from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserDataViewSet

# Create the router
router = DefaultRouter()
router.register(r'userdata', UserDataViewSet)

# Include the router's URLs
urlpatterns = [
    path('api/', include(router.urls)),  # Prefixes with /api/
]
