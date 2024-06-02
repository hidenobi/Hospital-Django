from django.contrib import admin
from .models import Medication, MedicalRecord, MedicalRecordDetail

# Register your models here.
admin.site.register(Medication)
admin.site.register(MedicalRecord)
admin.site.register(MedicalRecordDetail)
