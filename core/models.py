from django.db import models

class UserData(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=250)
    date_of_birth = models.DateField()

    def __str__(self):
        return self.name

# Create your models here.
