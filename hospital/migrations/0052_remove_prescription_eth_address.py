# Generated by Django 3.0.5 on 2024-06-13 06:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0051_auto_20240613_0922'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='prescription',
            name='eth_address',
        ),
    ]
