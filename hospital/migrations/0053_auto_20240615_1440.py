# Generated by Django 3.0.5 on 2024-06-15 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0052_remove_prescription_eth_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pharmacyinventory',
            name='pharmacyId',
            field=models.PositiveIntegerField(null=True),
        ),
    ]