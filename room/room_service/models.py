from django.db import models


# Create your models here.
class Room(models.Model):
    id = models.AutoField(primary_key=True)
    room_number = models.CharField(max_length=10, unique=True)
    room_type = models.CharField(max_length=50)
    capacity = models.IntegerField()
    patient_id = models.IntegerField(null=True, blank=True)
    assign_date = models.DateField(null=True, blank=True)
    discharge_date = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=20)
    doctor_id = models.IntegerField(null=False, blank=False)

    def __str__(self):
        return f"Room: {self.room_number}"

    class Meta:
        db_table = 'room'
