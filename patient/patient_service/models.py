from django.db import models


# Create your models here.
class Patient(models.Model):
    id = models.AutoField(primary_key=True)
    full_name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=15, unique=True)
    email = models.EmailField(max_length=254, unique=True)

    def __str__(self):
        return f"Patient: {self.full_name}"

    class Meta:
        db_table = 'patient'
