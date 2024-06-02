from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register('invoices', views.InvoiceViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
