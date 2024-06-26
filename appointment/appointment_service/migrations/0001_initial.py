# Generated by Django 4.0.1 on 2024-06-02 02:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('patientId', models.IntegerField()),
                ('doctorId', models.IntegerField()),
                ('roomId', models.IntegerField()),
                ('description', models.TextField()),
                ('timeSlotId', models.IntegerField()),
                ('status', models.TextField()),
            ],
            options={
                'db_table': 'appointment',
            },
        ),
        migrations.CreateModel(
            name='TimeSlot',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.DateField()),
                ('startTime', models.TimeField()),
                ('status', models.TextField()),
                ('doctorId', models.IntegerField()),
            ],
            options={
                'db_table': 'timeslot',
            },
        ),
    ]
