# Generated by Django 3.0.5 on 2024-06-02 20:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0037_auto_20240602_2309'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='hospitalId',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='appointment',
            name='hospitalName',
            field=models.CharField(max_length=40, null=True),
        ),
    ]
