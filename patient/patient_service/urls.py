from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views  # Nếu sử dụng viewsets

router = DefaultRouter()
router.register('patients', views.PatientViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('patients/', views.patient_list, name='patient_list.html'),
    path('patients/edit/<int:patient_id>/', views.edit_patient, name='edit_patient'),
]
