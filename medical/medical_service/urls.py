from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register('medications', views.MedicationViewSet)
router.register('medical_records', views.MedicalRecordViewSet)
router.register('medical_record_details', views.MedicalRecordDetailViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
