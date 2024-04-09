from django.db import models
import uuid
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django.utils.translation import gettext as _
# Create your models here.

BLOOD_GROUP_CHOICE = (
    (1, _("A+")),
    (2, _("B+")),
    (3, _("O+")),
    (4, _("AB+")),
    (5, _("A-")),
    (6, _("B-")),
    (7, _("O-")),
    (8, _("AB-")),
)

GENDER_CHOICE = (
    (1, _("Male")),
    (2,_("Female")),
)

class CustomPrimaryKeyField(models.CharField):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault('primary_key', True)
        kwargs.setdefault('max_length', 10)  # Adjust the max length as per your requirement
        kwargs.setdefault('editable', False)
        super().__init__(*args, **kwargs)

    def pre_save(self, model_instance, add):
        if add and not getattr(model_instance, self.attname):
            # Generate the custom primary key
            last_object = model_instance.__class__.objects.order_by('-id').first()
            if last_object and last_object.id:
                last_id = last_object.id
                prefix = last_id[:2]
                number = int(last_id[2:]) + 1
            else:  # Default prefix
                number = 1
            setattr(model_instance, self.attname, f'{prefix}{number:04d}')  # Assuming the number is 4 digits

            return getattr(model_instance, self.attname)
        else:
            return super().pre_save(model_instance, add)


class Hospital(models.Model):
    hospital_id = CustomPrimaryKeyField(prefix='hospital_')
    name = models.CharField(max_length=15, null=True,blank=False)
    address = models.CharField(max_length=256, null=True, blank=True)
    license_number = models.CharField(max_length=50)
    contact_number = RegexValidator(regex=r'^[0-9]\d{9}$', message="Please enter valid mobile number.")
    employee_count = models.PositiveIntegerField()
    location = models.CharField(max_length=100)
    established_date = models.DateField()
    certification_expiry_date = models.DateField()
    is_certified = models.BooleanField(default=False)

class Pharmacy(models.Model):
    pharmacy_id = CustomPrimaryKeyField(prefix='pharmacy_')
    name = models.CharField(max_length=15, null=True,blank=False)
    address = models.CharField(max_length=256, null=True, blank=True)
    license_number = models.CharField(max_length=50)
    contact_number = RegexValidator(regex=r'^[0-9]\d{9}$', message="Please enter valid mobile number.")
    employee_count = models.PositiveIntegerField()
    location = models.CharField(max_length=100)
    established_date = models.DateField()
    certification_expiry_date = models.DateField()
    is_certified = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_type = models.CharField(max_length=15, null=True,blank=False)
    address = models.CharField(max_length=256, null=True, blank=True)
    phone_regex = RegexValidator(regex=r'^[0-9]\d{9}$', message="Please enter valid mobile number.")
    mobile = models.CharField(validators=[phone_regex], max_length=10, blank=True)
    blood_group = models.IntegerField(choices=BLOOD_GROUP_CHOICE, default=1)
    gender = models.IntegerField(choices=GENDER_CHOICE, default=1)
    age = models.PositiveIntegerField(default=0)
    department = models.CharField(max_length=50, null=True, blank=True)
    profile_pic = models.ImageField(upload_to='profiles', blank=True)
    is_approved = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username
    
class ProfilePatient(models.Model):
    patient_id = CustomPrimaryKeyField(prefix='p_')
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=256, null=True, blank=True)
    email_address = models.CharField(max_length=256, null=True, blank=True)
    phone_regex = RegexValidator(regex=r'^[0-9]\d{9}$', message="Please enter valid mobile number.")
    mobile = models.CharField(validators=[phone_regex], max_length=10, blank=True)
    blood_group = models.IntegerField(choices=BLOOD_GROUP_CHOICE, default=1)
    gender = models.IntegerField(choices=GENDER_CHOICE, default=1)
    age = models.PositiveIntegerField(default=0)
    profile_pic = models.ImageField(upload_to='profiles', blank=True)
    is_approved = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username
    
class ProfileDoctor(models.Model):
    doctor_id = CustomPrimaryKeyField(prefix='d_')
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    hospotal_id = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
    user_type = models.CharField(max_length=15, null=True,blank=False)
    address = models.CharField(max_length=256, null=True, blank=True)
    email_address = models.CharField(max_length=256, null=True, blank=True)
    specialization = models.CharField(max_length=100, null=True, blank=True)
    experience = models.PositiveIntegerField(default=0)
    phone_regex = RegexValidator(regex=r'^[0-9]\d{9}$', message="Please enter valid mobile number.")
    mobile = models.CharField(validators=[phone_regex], max_length=10, blank=True)
    blood_group = models.IntegerField(choices=BLOOD_GROUP_CHOICE, default=1)
    gender = models.IntegerField(choices=GENDER_CHOICE, default=1)
    age = models.PositiveIntegerField(default=0)
    department = models.CharField(max_length=50, null=True, blank=True)
    profile_pic = models.ImageField(upload_to='profiles', blank=True)
    certification_expiry_date = models.DateField()
    is_certified = models.BooleanField(default=False)    
    is_approved = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username
    
class ProfileReception(models.Model):
    doctor_id = CustomPrimaryKeyField(prefix='d_')
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    hospotal_id = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
    user_type = models.CharField(max_length=15, null=True,blank=False)
    address = models.CharField(max_length=256, null=True, blank=True)
    email_address = models.CharField(max_length=256, null=True, blank=True)
    phone_regex = RegexValidator(regex=r'^[0-9]\d{9}$', message="Please enter valid mobile number.")
    mobile = models.CharField(validators=[phone_regex], max_length=10, blank=True)
    blood_group = models.IntegerField(choices=BLOOD_GROUP_CHOICE, default=1)
    gender = models.IntegerField(choices=GENDER_CHOICE, default=1)
    age = models.PositiveIntegerField(default=0)
    department = models.CharField(max_length=50, null=True, blank=True)
    profile_pic = models.ImageField(upload_to='profiles', blank=True)
    is_approved = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username

class Appointment(models.Model):
    # id = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
    user = models.CharField(max_length=256, null=False, blank=False)
    full_name = models.CharField(max_length=256, null=False, blank=False, default='')
    mobile = models.CharField(max_length=10, null=False, blank=False, default='')
    app_date = models.DateField(null=False, blank=False)
    doctor_id = models.CharField(max_length=256, null=False, blank=False)
    book_date = models.DateField(null=False, blank=False, auto_now=True)
    doctor_name = models.CharField(max_length=256, null=False, blank=False)
    department = models.CharField(max_length=100, null=False, blank=False)
    fees = models.PositiveIntegerField(null=False, blank=False, default=500)
    is_pay = models.BooleanField(default=False)
    appointment_no = models.PositiveIntegerField(null=False, blank=False, default=0)
    appointment_status = models.BooleanField(default=False)

    def __str__(self):
        return self.user

class Medical_Record(models.Model):
    user = models.CharField(max_length=256, null=False, blank=False)
    doctor_name = models.CharField(max_length=256, null=False, blank=False)
    department = models.CharField(max_length=100, null=False, blank=False)
    date = models.DateField()
    prescription = models.CharField(max_length=1024, null=False, blank=False)
    days = models.PositiveIntegerField(default=3)

    def __str__(self):
        return self.user

class Prescription(models.Model):
    user = models.CharField(max_length=256, null=False, blank=False)