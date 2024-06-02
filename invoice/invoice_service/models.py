from django.db import models


# Create your models here.
class Invoice(models.Model):
    id = models.AutoField(primary_key=True)
    patient_id = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    appointment_id = models.IntegerField()
    status = models.CharField(max_length=50)
    description = models.CharField(max_length=255, null=True)

    def __str__(self):
        return f"Invoice {self.id} for Appointment {self.appointment_id}"

    class Meta:
        db_table = 'invoice'
