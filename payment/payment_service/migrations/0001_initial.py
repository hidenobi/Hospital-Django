# Generated by Django 4.0.1 on 2024-06-02 02:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('invoice_id', models.IntegerField()),
                ('payment_amount', models.FloatField()),
                ('status', models.IntegerField()),
            ],
            options={
                'db_table': 'payment',
            },
        ),
    ]
