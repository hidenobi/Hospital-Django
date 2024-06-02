from django.db import models


# Create your models here.
class Payment(models.Model):
    id = models.AutoField(primary_key=True)
    invoice_id = models.IntegerField()
    payment_amount = models.FloatField()
    status = models.IntegerField()

    class Meta:
        db_table = 'payment'
