from django.db import models
import uuid
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django.utils.translation import gettext as _
from django.core.validators import MinValueValidator
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
            else: 
                prefix='appointment_'# Default prefix
                number = 1
            setattr(model_instance, self.attname, f'{prefix}{number:04d}')  # Assuming the number is 4 digits

            return getattr(model_instance, self.attname)
        else:
            return super().pre_save(model_instance, add)


class Hospital(models.Model):
    hospital_id = models.CharField(max_length=200, blank=True, null=True)
    hospital_name = models.CharField(max_length=15, null=True,blank=False)
    address = models.CharField(max_length=256, null=True, blank=True)
    email = models.CharField(max_length=256, null=True, blank=True)
    license_number = models.CharField(max_length=50)
    contact_number = RegexValidator(regex=r'^[0-9]\d{9}$', message="Please enter valid mobile number.")
    employee_count = models.PositiveIntegerField()
    established_date = models.DateField()
    certification_expiry_date = models.DateField()
    is_certified = models.BooleanField(default=False)
    
    def save(self):
        if not self.hospital_id and self.pk is None:
            last_hospital = Hospital.objects.all().order_by("-pk").first()
            last_pk = 0
            if last_hospital:
                last_pk = last_hospital.pk
        
            self.hospital_id = "hospital-" + str(last_pk+1).zfill(3)

        super(Hospital, self).save()


class Pharmacy(models.Model):
    pharmacy_id = models.CharField(max_length=200, blank=True, null=True)
    pharmacy_name = models.CharField(max_length=15, null=True,blank=False)
    address = models.CharField(max_length=256, null=True, blank=True)
    email = models.CharField(max_length=256, null=True, blank=True)
    license_number = models.CharField(max_length=50)
    contact_number = RegexValidator(regex=r'^[0-9]\d{9}$', message="Please enter valid mobile number.")
    employee_count = models.PositiveIntegerField()
    established_date = models.DateField()
    certification_expiry_date = models.DateField()
    is_certified = models.BooleanField(default=False)

    
    def save(self):
        if not self.pharmacy_id and self.pk is None:
            last_pharmacy = Pharmacy.objects.all().order_by("-pk").first()
            last_pk = 0
            if last_pharmacy:
                last_pk = last_pharmacy.pk
        
            self.pharmacy_id = "pharmacy-" + str(last_pk+1).zfill(3)

        super(Pharmacy, self).save()
        
    def __str__(self):
        return self.name

# class MedicineInventory(models.Model):
#     drug_id = CustomPrimaryKeyField(prefix='drug_')
#     pharmacy = models.ForeignKey(Pharmacy, on_delete=models.CASCADE)
#     name = models.CharField(max_length=100)
#     description = models.TextField(blank=True)
#     quantity = models.PositiveIntegerField(validators=[MinValueValidator(0)])
#     price = models.DecimalField(max_digits=10, decimal_places=2)

#     def __str__(self):
#         return f"{self.name} ({self.pharmacy.name})"
    
# class Profile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     user_type = models.CharField(max_length=15, null=True,blank=False)
#     address = models.CharField(max_length=256, null=True, blank=True)
#     phone_regex = RegexValidator(regex=r'^[0-9]\d{9}$', message="Please enter valid mobile number.")
#     mobile = models.CharField(validators=[phone_regex], max_length=10, blank=True)
#     blood_group = models.IntegerField(choices=BLOOD_GROUP_CHOICE, default=1)
#     gender = models.IntegerField(choices=GENDER_CHOICE, default=1)
#     age = models.PositiveIntegerField(default=0)
#     department = models.CharField(max_length=50, null=True, blank=True)
#     profile_pic = models.ImageField(upload_to='profiles', blank=True)
#     is_approved = models.BooleanField(default=False)

#     def __str__(self):
#         return self.user.username
    
# class ProfilePatient(models.Model):
#     patient_id = CustomPrimaryKeyField(prefix='p_')
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     address = models.CharField(max_length=256, null=True, blank=True)
#     email_address = models.CharField(max_length=256, null=True, blank=True)
#     phone_regex = RegexValidator(regex=r'^[0-9]\d{9}$', message="Please enter valid mobile number.")
#     mobile = models.CharField(validators=[phone_regex], max_length=10, blank=True)
#     blood_group = models.IntegerField(choices=BLOOD_GROUP_CHOICE, default=1)
#     gender = models.IntegerField(choices=GENDER_CHOICE, default=1)
#     age = models.PositiveIntegerField(default=0)
#     profile_pic = models.ImageField(upload_to='profiles', blank=True)
#     is_approved = models.BooleanField(default=False)

#     def __str__(self):
#         return self.user.username
    
# class ProfileDoctor(models.Model):
#     doctor_id = CustomPrimaryKeyField(prefix='d_')
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     hospotal_id = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
#     user_type = models.CharField(max_length=15, null=True,blank=False)
#     address = models.CharField(max_length=256, null=True, blank=True)
#     email_address = models.CharField(max_length=256, null=True, blank=True)
#     specialization = models.CharField(max_length=100, null=True, blank=True)
#     experience = models.PositiveIntegerField(default=0)
#     phone_regex = RegexValidator(regex=r'^[0-9]\d{9}$', message="Please enter valid mobile number.")
#     mobile = models.CharField(validators=[phone_regex], max_length=10, blank=True)
#     blood_group = models.IntegerField(choices=BLOOD_GROUP_CHOICE, default=1)
#     gender = models.IntegerField(choices=GENDER_CHOICE, default=1)
#     age = models.PositiveIntegerField(default=0)
#     department = models.CharField(max_length=50, null=True, blank=True)
#     profile_pic = models.ImageField(upload_to='profiles', blank=True)
#     certification_expiry_date = models.DateField()
#     is_certified = models.BooleanField(default=False)    
#     is_approved = models.BooleanField(default=False)

#     def __str__(self):
#         return self.user.username
    
# class ProfileReception(models.Model):
#     doctor_id = CustomPrimaryKeyField(prefix='reception_')
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     hospotal_id = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
#     user_type = models.CharField(max_length=15, null=True,blank=False)
#     address = models.CharField(max_length=256, null=True, blank=True)
#     email_address = models.CharField(max_length=256, null=True, blank=True)
#     phone_regex = RegexValidator(regex=r'^[0-9]\d{9}$', message="Please enter valid mobile number.")
#     mobile = models.CharField(validators=[phone_regex], max_length=10, blank=True)
#     blood_group = models.IntegerField(choices=BLOOD_GROUP_CHOICE, default=1)
#     gender = models.IntegerField(choices=GENDER_CHOICE, default=1)
#     age = models.PositiveIntegerField(default=0)
#     department = models.CharField(max_length=50, null=True, blank=True)
#     profile_pic = models.ImageField(upload_to='profiles', blank=True)
#     is_approved = models.BooleanField(default=False)

#     def __str__(self):
#         return self.user.username

# class Appointment(models.Model):
#     # id = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
#     appointment_id = CustomPrimaryKeyField(prefix='appointment_')
#     user = models.CharField(max_length=256, null=False, blank=False)
#     full_name = models.CharField(max_length=256, null=False, blank=False, default='')
#     mobile = models.CharField(max_length=10, null=False, blank=False, default='')
#     app_date = models.DateField(null=False, blank=False)
#     doctor_id = models.CharField(max_length=256, null=False, blank=False)
#     book_date = models.DateField(null=False, blank=False, auto_now=True)
#     patient = models.ForeignKey(ProfilePatient, on_delete=models.CASCADE)
#     doctor = models.ForeignKey(ProfileDoctor, on_delete=models.CASCADE)
#     doctor_name = models.CharField(max_length=256, null=False, blank=False)
#     department = models.CharField(max_length=100, null=False, blank=False)
#     fees = models.PositiveIntegerField(null=False, blank=False, default=500)
#     is_pay = models.BooleanField(default=False)
#     appointment_no = models.PositiveIntegerField(null=False, blank=False, default=0)
#     appointment_status = models.BooleanField(default=False)

#     def __str__(self):
#         return self.user

# class Prescription(models.Model):
#     prescription_id = CustomPrimaryKeyField(prefix='prescription_')
#     pharmacy = models.ForeignKey(Pharmacy, on_delete=models.CASCADE)
#     patient = models.ForeignKey(ProfilePatient, on_delete=models.CASCADE)
#     doctor = models.ForeignKey(ProfileDoctor, on_delete=models.CASCADE)
#     drugs = models.ManyToManyField(MedicineInventory, through='PrescribedDrug')
#     total_length = models.PositiveIntegerField(help_text="Total length of prescription in days")

#     def __str__(self):
#         return f"Prescription for {self.pharmacy.name}"

# class PrescribedDrug(models.Model):
#     prescription = models.ForeignKey(Prescription, on_delete=models.CASCADE)
#     drug = models.ForeignKey(MedicineInventory, on_delete=models.CASCADE)
#     dosage = models.CharField(max_length=100)

#     def __str__(self):
#         return f"{self.drug.name} ({self.prescription.pharmacy.name})"
    
# class Medical_Record(models.Model):
#     medical_record_id = CustomPrimaryKeyField(prefix='md_')
#     prescription = models.ForeignKey(Prescription, on_delete=models.CASCADE)
#     user = models.CharField(max_length=256, null=False, blank=False)
#     doctor_name = models.CharField(max_length=256, null=False, blank=False)
#     department = models.CharField(max_length=100, null=False, blank=False)
#     date = models.DateField()
#     prescription = models.CharField(max_length=1024, null=False, blank=False)
#     days = models.PositiveIntegerField(default=3)