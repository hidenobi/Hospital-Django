from rest_framework import viewsets, status
from rest_framework.response import Response

from .models import Patient
from .serializers import PatientSerializer

from django.shortcuts import render, redirect
from .models import Patient
import requests


class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer

    # Hàm để lấy toàn bộ danh sách bệnh nhân
    def list(self, request, *args, **kwargs):
        patients = self.get_queryset()
        serializer = self.get_serializer(patients, many=True)
        return Response(serializer.data)

    # Hàm để lấy thông tin chi tiết của bệnh nhân theo ID
    def retrieve(self, request, pk=None, *args, **kwargs):
        try:
            patient = self.get_object()
            serializer = self.get_serializer(patient)
            return Response(serializer.data)
        except Patient.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    # Hàm để tạo mới bệnh nhân
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Hàm để cập nhật thông tin bệnh nhân
    def update(self, request, pk=None, *args, **kwargs):
        try:
            patient = self.get_object()
            serializer = self.get_serializer(patient, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Patient.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    # Hàm để xóa bệnh nhân
    def destroy(self, request, pk=None, *args, **kwargs):
        try:
            patient = self.get_object()
            patient.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Patient.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)


def patient_list(request):
    if request.method == 'POST':
        # Create patient
        data = {
            "full_name": request.POST['full_name'],
            "address": request.POST['address'],
            "phone_number": request.POST['phone_number'],
            "email": request.POST['email'],
        }
        response = requests.post('http://127.0.0.1:8000/api/patients', data=data)
        if response.status_code == 201:
            return redirect('patient_list')
        else:
            pass

    # Fetch patient data from API
    response = requests.get('http://127.0.0.1:8000/api/patients')
    patients = response.json()

    context = {
        'patients': patients,
    }
    return render(request, 'patient_list.html', context)


def edit_patient(request, patient_id):
    if request.method == 'POST':
        # Update patient
        data = {
            "full_name": request.POST['full_name'],
            "address": request.POST['address'],
            "phone_number": request.POST['phone_number'],
            "email": request.POST['email'],
        }
        response = requests.put(f'http://127.0.0.1:8000/api/patients/{patient_id}', data=data)
        if response.status_code == 200:
            return redirect('patient_list')
        else:
            pass

    # Fetch patient data from API
    response = requests.get(f'http://127.0.0.1:8000/api/patients/{patient_id}')
    patient = response.json()

    context = {
        'patient': patient,
    }
    return render(request, 'edit_patient.html', context)
