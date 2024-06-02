from rest_framework import serializers
from .models import FullName, Address, Doctor


class FullNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = FullName
        fields = '__all__'


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'


class DoctorSerializer(serializers.ModelSerializer):
    full_name = FullNameSerializer()
    address = AddressSerializer()

    class Meta:
        model = Doctor
        fields = '__all__'
