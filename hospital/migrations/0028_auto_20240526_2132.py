# Generated by Django 3.0.5 on 2024-05-26 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0027_auto_20240526_2129'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='status',
            field=models.PositiveIntegerField(choices=[(1, 'Scheduled'), (2, 'Registered'), (3, 'Checked in'), (4, 'Issued'), (5, 'Ready'), (6, 'Dispensed'), (7, 'Medication Active'), (8, 'Completed')], default=1),
        ),
    ]
