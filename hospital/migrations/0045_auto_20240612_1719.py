# Generated by Django 3.0.5 on 2024-06-12 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0044_auto_20240612_1716'),
    ]

    operations = [
        migrations.AddField(
            model_name='patientdetailsadmin',
            name='appointmentId',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='patientdetailsadmin',
            name='patientID',
            field=models.PositiveIntegerField(null=True),
        ),
    ]
