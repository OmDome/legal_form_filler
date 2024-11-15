from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class FormTemplate(models.Model):
    form_code = models.CharField(max_length=50, unique=True)
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title

class FormField(models.Model):
    TEXT = 'text'
    DATE = 'date'
    NUMBER = 'number'
    CHECKBOX = 'checkbox'
    MULTIPLE_CHECKBOX = 'multiple_checkbox'

    FIELD_TYPE_CHOICES = [
        (TEXT, 'Text'),
        (DATE, 'Date'),
        (NUMBER, 'Number'),
        (CHECKBOX, 'Checkbox'),
        (MULTIPLE_CHECKBOX, 'Multiple Checkbox'),
    ]

    form_template = models.ForeignKey(FormTemplate, on_delete=models.CASCADE, related_name="fields")
    field_name = models.CharField(max_length=50)
    label = models.CharField(max_length=200)
    field_type = models.CharField(max_length=50, choices=FIELD_TYPE_CHOICES)
    choices = models.TextField(blank=True, null=True, help_text="Comma-separated options for multiple checkboxes")  # New field for options
    step_number = models.IntegerField()

    def __str__(self):
        return f"{self.label} ({self.form_template.title})"

class UserResponse(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    form_template = models.ForeignKey(FormTemplate, on_delete=models.CASCADE)
    field_name = models.CharField(max_length=50)
    response = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Response for {self.field_name} by {self.user.username}"
