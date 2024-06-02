from django.contrib import admin
from .models import Address, FullName, Doctor

# Register your models here.
admin.site.register(Address)
admin.site.register(FullName)
admin.site.register(Doctor)
