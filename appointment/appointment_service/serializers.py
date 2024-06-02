from rest_framework import serializers
from .models import Appointment, TimeSlot


class TimeSlotSerializer(serializers.ModelSerializer):
    class Meta:
        model = TimeSlot
        fields = '__all__'


class AppointmentSerializer(serializers.ModelSerializer):
    timeSlot = TimeSlotSerializer()

    class Meta:
        model = Appointment
        fields = '__all__'
