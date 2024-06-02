from rest_framework import viewsets
from .models import Medication, MedicalRecord, MedicalRecordDetail
from .serializers import MedicationSerializer, MedicalRecordSerializer, MedicalRecordDetailSerializer


class MedicationViewSet(viewsets.ModelViewSet):
    queryset = Medication.objects.all()
    serializer_class = MedicationSerializer


class MedicalRecordViewSet(viewsets.ModelViewSet):
    queryset = MedicalRecord.objects.all()
    serializer_class = MedicalRecordSerializer


class MedicalRecordDetailViewSet(viewsets.ModelViewSet):
    queryset = MedicalRecordDetail.objects.all()
    serializer_class = MedicalRecordDetailSerializer
