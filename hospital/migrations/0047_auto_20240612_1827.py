# Generated by Django 3.0.5 on 2024-06-12 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0046_auto_20240612_1720'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patientdetailsadmin',
            name='sypmtoms',
        ),
        migrations.AddField(
            model_name='patientdetailsadmin',
            name='allergies',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='patientdetailsadmin',
            name='appointmentId',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='patientdetailsadmin',
            name='currentMedication',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='patientdetailsadmin',
            name='currentSymptoms',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='patientdetailsadmin',
            name='doctorId',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='patientdetailsadmin',
            name='medicalConcerns',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='patientdetailsadmin',
            name='medical_history',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='patientdetailsadmin',
            name='patientId',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='patientdetailsadmin',
            name='weight',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='patientdetailsadmin',
            name='diagnosis',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
