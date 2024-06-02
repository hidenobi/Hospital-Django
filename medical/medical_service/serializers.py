from rest_framework import serializers
from .models import Medication, MedicalRecord, MedicalRecordDetail


class MedicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medication
        fields = '__all__'


class MedicalRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicalRecord
        fields = '__all__'


class MedicalRecordDetailSerializer(serializers.ModelSerializer):
    medical = MedicationSerializer(read_only=True)  # Nested serializer for medication

    class Meta:
        model = MedicalRecordDetail
        fields = '__all__'
