# Generated by Django 5.0.4 on 2024-04-06 13:29

import django.core.validators
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=256)),
                ('full_name', models.CharField(default='', max_length=256)),
                ('mobile', models.CharField(default='', max_length=10)),
                ('app_date', models.DateField()),
                ('book_date', models.DateField(auto_now=True)),
                ('doctor_name', models.CharField(max_length=256)),
                ('department', models.CharField(max_length=100)),
                ('fees', models.PositiveIntegerField(default=500)),
                ('is_pay', models.BooleanField(default=False)),
                ('appointment_no', models.PositiveIntegerField(default=0)),
                ('appointment_status', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Medical_Record',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=256)),
                ('doctor_name', models.CharField(max_length=256)),
                ('department', models.CharField(max_length=100)),
                ('date', models.DateField()),
                ('prescription', models.CharField(max_length=1024)),
                ('days', models.PositiveIntegerField(default=3)),
            ],
        ),
        migrations.CreateModel(
            name='Prescription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_type', models.CharField(max_length=15, null=True)),
                ('address', models.CharField(blank=True, max_length=256, null=True)),
                ('mobile', models.CharField(blank=True, max_length=10, validators=[django.core.validators.RegexValidator(message='Please enter valid mobile number.', regex='^[0-9]\\d{9}$')])),
                ('blood_group', models.IntegerField(choices=[(1, 'A+'), (2, 'B+'), (3, 'O+'), (4, 'AB+'), (5, 'A-'), (6, 'B-'), (7, 'O-'), (8, 'AB-')], default=1)),
                ('gender', models.IntegerField(choices=[(1, 'Male'), (2, 'Female')], default=1)),
                ('age', models.PositiveIntegerField(default=0)),
                ('department', models.CharField(blank=True, max_length=50, null=True)),
                ('profile_pic', models.ImageField(blank=True, upload_to='profiles')),
                ('is_approved', models.BooleanField(default=False)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
