# Generated by Django 3.0.5 on 2024-06-12 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0048_auto_20240612_1837'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patientdetailsadmin',
            name='currentMedication',
            field=models.TextField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='patientdetailsadmin',
            name='currentSymptoms',
            field=models.TextField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='patientdetailsadmin',
            name='medicalConcerns',
            field=models.TextField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='patientdetailsadmin',
            name='medical_history',
            field=models.TextField(max_length=200, null=True),
        ),
    ]