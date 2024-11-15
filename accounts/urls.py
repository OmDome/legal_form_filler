from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('core/', include('core.urls')),
    #path('', include('accounts.urls')),
    path('accounts/', include('allauth.urls')),
    # Add the manual social login route
]
