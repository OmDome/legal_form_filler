from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('core/', include('core.urls')),
    path('', views.home, name='home'),  # General homepage
    path('', include('accounts.urls')),  # Custom accounts and allauth routes
    path('accounts/', include('allauth.urls')),
    path('fill_form/<int:form_id>/', views.form_fill, name='form_fill'),
    path('fill_form/<str:form_code>/step/<int:step_number>/', views.fill_form_step, name='fill_form_step'),
]
