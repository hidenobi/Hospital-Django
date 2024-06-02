from django.db import models


# Create your models here.

class TimeSlot(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateField()
    startTime = models.TimeField()
    status = models.TextField()
    doctorId = models.IntegerField()

    def __str__(self):
        return f"TimeSlot: {self.startTime}, {self.date}"

    class Meta:
        db_table = 'timeslot'


class Appointment(models.Model):
    id = models.AutoField(primary_key=True)
    patientId = models.IntegerField()
    doctorId = models.IntegerField()
    roomId = models.IntegerField()
    description = models.TextField()
    timeSlot = models.ForeignKey(TimeSlot, on_delete=models.CASCADE, null=True)
    status = models.TextField()

    def __str__(self):
        return f"Appointment: {self.id}"

    class Meta:
        db_table = 'appointment'
