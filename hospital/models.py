from django.db import models
from django.contrib.auth.models import User



departments=[('Cardiologist','Cardiologist'),
             ('Cardiologist','Cardiologist'),
            ('Dermatologists','Dermatologists'),
            ('Emergency Medicine Specialists','Emergency Medicine Specialists'),
            ('Allergists/Immunologists','Allergists/Immunologists'),
            ('Anesthesiologists','Anesthesiologists'),
        ('Colon and Rectal Surgeons','Colon and Rectal Surgeons')
]
appointment_status = [
    (1 , 'Scheduled'), 
    (2 , 'Registered'),
    (3 , 'Checked in'),
    (4 , 'Issued'),
    (5 , 'Ready'),
    (6 , 'Dispensed'),
    (7 , 'Medication Active'),
    (8 , 'Completed')
]


class Hospital(models.Model):
    name=models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    contact=models.CharField(max_length=20)
    email=models.EmailField(max_length=50)
    logo=models.ImageField(upload_to='profile_pic/HospitalLogo/',null=True,blank=True)
    is_approved=models.BooleanField(default=False)
    def __str__(self):
        return self.name

class Doctor(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    hospitalId=models.PositiveIntegerField(null=True)
    profile_pic= models.ImageField(upload_to='profile_pic/DoctorProfilePic/',null=True,blank=True)
    address = models.CharField(max_length=40)
    mobile = models.CharField(max_length=20,null=True)
    department= models.CharField(max_length=50,choices=departments,default='Cardiologist')
    status=models.BooleanField(default=False)
    @property
    def get_name(self):
        return self.user.first_name+" "+self.user.last_name
    @property
    def get_id(self):
        return self.user.id
    def __str__(self):
        return "{} ({})".format(self.user.first_name,self.department)

class Admin(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)    
    hospitalId=models.PositiveIntegerField(null=True)
    profile_pic= models.ImageField(upload_to='profile_pic/AdminProfilePic/',null=True,blank=True)
    address = models.CharField(max_length=40)
    mobile = models.CharField(max_length=20,null=True)
    status=models.BooleanField(default=False)
    @property
    def get_name(self):
        return self.user.first_name+" "+self.user.last_name
    @property
    def get_id(self):
        return self.user.id
    def __str__(self):
        return self.user.first_name

class Receptionist(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)    
    hospitalId=models.PositiveIntegerField(null=True)
    profile_pic= models.ImageField(upload_to='profile_pic/ReceptionistProfilePic/',null=True,blank=True)
    address = models.CharField(max_length=40)
    mobile = models.CharField(max_length=20,null=True)
    status=models.BooleanField(default=False)
    @property
    def get_name(self):
        return self.user.first_name+" "+self.user.last_name
    @property
    def get_id(self):
        return self.user.id
    def __str__(self):
        return self.user.first_name

class Patient(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    profile_pic= models.ImageField(upload_to='profile_pic/PatientProfilePic/',null=True,blank=True)
    address = models.CharField(max_length=40)
    mobile = models.CharField(max_length=20,null=False)
    admitDate=models.DateField(null=False)
    status=models.BooleanField(default=False)
    @property
    def get_name(self):
        return self.user.first_name+" "+self.user.last_name
    @property
    def get_id(self):
        return self.user.id
    def __str__(self):
        return self.user.first_name

class Pharmacy(models.Model):
    name=models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    contact=models.CharField(max_length=20)
    email=models.EmailField(max_length=50)
    logo=models.ImageField(upload_to='profile_pic/PharmacyLogo/',null=True,blank=True)
    is_approved=models.BooleanField(default=False)
    def __str__(self):
        return self.name

class Prescription(models.Model):
    appointment=models.OneToOneField('Appointment',on_delete=models.CASCADE)
    pharmacyId=models.PositiveIntegerField(null=True)
    pharmacyName=models.CharField(max_length=40)
    medicineName=models.CharField(max_length=40)
    description=models.TextField(max_length=500)
    status=models.BooleanField(default=False)

class Appointment(models.Model):
    patientId=models.PositiveIntegerField(null=True)
    doctorId=models.PositiveIntegerField(null=True)
    hospitalId=models.PositiveIntegerField(null=True)
    hospitalname=models.CharField(max_length=40,null=True)
    patientName=models.CharField(max_length=40,null=True)
    doctorName=models.CharField(max_length=40,null=True)
    appointmentDate=models.DateField(auto_now=True)
    description=models.TextField(max_length=500)
    status=models.PositiveIntegerField(choices=appointment_status ,default=1)


class PatientDischargeDetails(models.Model):
    patientId=models.PositiveIntegerField(null=True)
    appointmentId=models.PositiveIntegerField(null=True)
    patientName=models.CharField(max_length=40)
    address = models.CharField(max_length=40)
    mobile = models.CharField(max_length=20,null=True)
    admitDate=models.DateField(null=False)
    releaseDate=models.DateField(null=False)
    medicineCost=models.PositiveIntegerField(null=False)
    doctorFee=models.PositiveIntegerField(null=False)
    OtherCharge=models.PositiveIntegerField(null=False)
    total=models.PositiveIntegerField(null=False)



