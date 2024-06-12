# Generated by Django 3.0.5 on 2024-06-11 21:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0041_auto_20240608_2218'),
    ]

    operations = [
        migrations.AddField(
            model_name='prescription',
            name='doctorId',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='prescription',
            name='doctorName',
            field=models.CharField(max_length=40, null=True),
        ),
        migrations.AddField(
            model_name='prescription',
            name='patientId',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='prescription',
            name='patientName',
            field=models.CharField(max_length=40, null=True),
        ),
    ]