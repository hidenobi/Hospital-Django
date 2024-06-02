from rest_framework import viewsets
from rest_framework.response import Response

from .models import Doctor, FullName, Address
from .serializers import DoctorSerializer, FullNameSerializer, AddressSerializer


class DoctorViewSet(viewsets.ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer

    def list(self, request, **kwargs):
        # Retrieve and serialize all doctors
        doctors = self.get_queryset()
        serializer = self.get_serializer(doctors, many=True)
        return Response(serializer.data)

    def create(self, request, **kwargs):
        # Extract and validate data for both Doctor, FullName, and Address
        full_name_data = request.data.pop('full_name')
        address_data = request.data.pop('address')

        full_name_serializer = FullNameSerializer(data=full_name_data)
        full_name_serializer.is_valid(raise_exception=True)
        full_name = full_name_serializer.save()

        address_serializer = AddressSerializer(data=address_data)
        address_serializer.is_valid(raise_exception=True)
        address = address_serializer.save()

        doctor_data = {
            'full_name': full_name.id,
            'address': address.id,
            'phone_number': request.data['phone_number'],
            'email': request.data['email'],
        }
        doctor_serializer = DoctorSerializer(data=doctor_data)
        doctor_serializer.is_valid(raise_exception=True)
        doctor = doctor_serializer.save()

        return Response(doctor_serializer.data)

    def update(self, request, pk, **kwargs):
        # Extract and validate data for both Doctor, FullName, and Address
        full_name_data = request.data.pop('full_name')
        address_data = request.data.pop('address')

        try:
            full_name = FullName.objects.get(pk=full_name_data['id'])
        except FullName.DoesNotExist:
            full_name = FullName.objects.create(**full_name_data)

        try:
            address = Address.objects.get(pk=address_data['id'])
        except Address.DoesNotExist:
            address = Address.objects.create(**address_data)

        doctor = Doctor.objects.get(pk=pk)
        doctor.full_name = full_name
        doctor.address = address
        doctor.phone_number = request.data['phone_number']
        doctor.email = request.data['email']
        doctor.save()

        doctor_serializer = DoctorSerializer(instance=doctor)
        return Response(doctor_serializer.data)
