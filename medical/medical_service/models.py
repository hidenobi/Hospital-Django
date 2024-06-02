from django.db import models

# Create your models here.

from django.db import models
from django.utils import timezone


class Medication(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    indication = models.CharField(max_length=100)
    price = models.FloatField()


class MedicalRecord(models.Model):
    patient_id = models.IntegerField()
    doctor_id = models.IntegerField()
    created_at = models.DateTimeField(default=timezone.now)
    paid_at = models.DateTimeField(null=True)
    diagnosis = models.TextField(null=True)

    class Meta:
        db_table = 'medical_record'
        ordering = ['-created_at']


class MedicalRecordDetail(models.Model):
    medicalRecord = models.ForeignKey(MedicalRecord, on_delete=models.CASCADE, related_name='details')
    price = models.DecimalField(max_digits=20, decimal_places=0)
    treatment = models.TextField()
    amount = models.IntegerField()
    medical = models.ForeignKey(Medication, on_delete=models.CASCADE, null=True)

    class Meta:
        db_table = 'medical_record_detail'
