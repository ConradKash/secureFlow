# Generated by Django 5.0.4 on 2024-04-07 00:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('secureFlowMain', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='doctor_id',
            field=models.CharField(default='1', max_length=256),
        ),
    ]
