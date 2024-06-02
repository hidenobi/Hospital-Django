from django.db import models


# Create your models here.


class FullName(models.Model):
    id = models.AutoField(primary_key=True)
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.firstname} {self.lastname}"

    class Meta:
        db_table = 'fullname'


class Address(models.Model):
    id = models.AutoField(primary_key=True)
    house = models.CharField(max_length=255)
    district = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.house}, {self.district}, {self.city}, {self.country}"

    class Meta:
        db_table = 'address'


class Doctor(models.Model):
    id = models.AutoField(primary_key=True)
    full_name = models.ForeignKey(FullName, on_delete=models.CASCADE, null=True)
    address = models.ForeignKey(Address, on_delete=models.CASCADE, null=True)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField(max_length=254)

    def __str__(self):
        return f"Doctor: {self.full_name}"

    class Meta:
        db_table = 'doctor'
