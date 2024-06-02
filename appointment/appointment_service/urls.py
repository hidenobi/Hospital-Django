from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register('timeslots', views.TimeSlotViewSet)
router.register('appointments', views.AppointmentViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]