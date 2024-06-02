from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register('doctors', views.DoctorViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
