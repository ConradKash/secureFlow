# Generated by Django 3.0.5 on 2024-06-12 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0042_auto_20240612_0059'),
    ]

    operations = [
        migrations.CreateModel(
            name='PatientDetailsAdmin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patientID', models.PositiveIntegerField(null=True)),
                ('appointmentId', models.PositiveIntegerField(null=True)),
                ('visitDate', models.DateField(auto_now=True)),
                ('height', models.FloatField(null=True)),
                ('temperature', models.FloatField(null=True)),
                ('sypmtoms', models.CharField(max_length=40)),
                ('diagnosis', models.CharField(max_length=20, null=True)),
                ('treatment', models.CharField(choices=[('SelectTreatmentPlan', 'Select Treatment Plan'), ('Prescription', 'Prescription'), ('lifestyleModification', 'Lifestyle Modification'), ('physicalTherapy', 'Physical Therapy'), ('others', 'Others')], default='SelectTreatmentPlan', max_length=50)),
            ],
        ),
        migrations.RemoveField(
            model_name='patientdetails',
            name='blood_pressure',
        ),
        migrations.RemoveField(
            model_name='patientdetails',
            name='cholesterol',
        ),
    ]
