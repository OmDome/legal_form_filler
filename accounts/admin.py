from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import FormTemplate, FormField, UserResponse

@admin.register(FormTemplate)
class FormTemplateAdmin(admin.ModelAdmin):
    list_display = ('form_code', 'title')

@admin.register(FormField)
class FormFieldAdmin(admin.ModelAdmin):
    list_display = ('label', 'form_template', 'step_number', 'field_type')

@admin.register(UserResponse)
class UserResponseAdmin(admin.ModelAdmin):
    list_display = ('user', 'form_template', 'field_name', 'response')
