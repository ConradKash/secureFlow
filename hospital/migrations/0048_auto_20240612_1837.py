# Generated by Django 3.0.5 on 2024-06-12 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0047_auto_20240612_1827'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patientdetailsadmin',
            name='diagnosis',
            field=models.TextField(max_length=500, null=True),
        ),
    ]