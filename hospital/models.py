from django.db import models
from django.contrib.auth.models import User



departments = [
    ('Cardiology', 'Cardiology'),
    ('Dermatology', 'Dermatology'),
    ('Emergency Medicine', 'Emergency Medicine'),
    ('Allergy and Immunology', 'Allergy and Immunology'),
    ('Endocrinology', 'Endocrinology'),
    ('Gastroenterology', 'Gastroenterology'),
    ('Hematology', 'Hematology'),
    ('Infectious Disease', 'Infectious Disease'),
    ('Nephrology', 'Nephrology'),
    ('Neurology', 'Neurology'),
    ('Oncology', 'Oncology'),
    ('Pediatrics', 'Pediatrics'),
    ('Psychiatry', 'Psychiatry'),
    ('Pulmonology', 'Pulmonology'),
    ('Rheumatology', 'Rheumatology')
]
appointment_status = [
    ('Scheduled' , 'Scheduled'), 
    ('Registered' , 'Registered'),
    ('Checked in' , 'Checked in'),
    ('Issued' , 'Issued'),
    ('Ready' , 'Ready'),
    ('Dispensed' , 'Dispensed'),
    ('Medication Active' , 'Medication Active'),
    ('Complete' , 'Completed')
]

treatment_plan = [
    ('SelectTreatmentPlan' , 'Select Treatment Plan'),
    ('Prescription' , 'Prescription'),
    ('lifestyleModification' , 'Lifestyle Modification'),
    ('physicalTherapy' , 'Physical Therapy'),
    ('others' , 'Others')    
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
    
class PharmacyInventory(models.Model):
    pharmacyId=models.PositiveIntegerField(null=True)
    medicineName=models.CharField(max_length=40)
    description=models.TextField(max_length=500)
    price=models.PositiveIntegerField(null=False)
    stock=models.PositiveIntegerField(null=False)
    status=models.BooleanField(default=False)
    def __str__(self):
        return self.medicineName

class AdminPharmacy(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)    
    pharmacyId=models.PositiveIntegerField(null=True)
    profile_pic= models.ImageField(upload_to='profile_pic/AdminPharmacyProfilePic/',null=True,blank=True)
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

class Appointment(models.Model):
    hospitalId=models.PositiveIntegerField(null=True)
    patientId=models.PositiveIntegerField(null=True)
    doctorId=models.PositiveIntegerField(null=True)
    hospitalName=models.CharField(max_length=40,null=True)
    patientName=models.CharField(max_length=40,null=True)
    doctorName=models.CharField(max_length=40,null=True)
    datestamp=models.DateTimeField(auto_now=True)
    appointmentDate=models.DateField(null=True, blank=True)
    description=models.TextField(max_length=500)
    status=models.BooleanField(default=False)
    def __str__(self):
        return self.description

class PatientDetailsAdmin(models.Model):
    patientId=models.PositiveIntegerField(null=True)
    appointmentId=models.PositiveIntegerField(null=True)
    doctorId=models.PositiveIntegerField(null=True)
    visitDate=models.DateField(auto_now=True)
    height=models.FloatField(null=True)
    weight=models.FloatField(null=True)
    temperature=models.FloatField(null=True)  
    medical_history=models.TextField(max_length=200, null=True)
    currentMedication= models.TextField(max_length=200, null=True)
    currentSymptoms=models.TextField(max_length=200, null=True)
    allergies=models.CharField(max_length=200, null=True)
    medicalConcerns=models.TextField(max_length=200, null=True)
    diagnosis=models.TextField(max_length=500, null=True)
    treatment=models.CharField(max_length=50,choices=treatment_plan,default='SelectTreatmentPlan')
    def __str__(self):
        return self.currentSymptoms

class PatientDetails(models.Model):
    patientID=models.PositiveIntegerField(null=True)
    appointmentId=models.PositiveIntegerField(null=True)
    visitDate=models.DateField(auto_now=True)
    height=models.FloatField(null=True)
    weight=models.FloatField(null=True)
    blood_sugar=models.FloatField(null=True)
    heart_rate=models.FloatField(null=True)
    temperature=models.FloatField(null=True)
    symptoms=models.TextField(max_length=500)
    diagnosis=models.TextField(max_length=500)
    treatment=models.TextField(max_length=500)
    def __str__(self):
        return self.symptoms 
    
class Prescription(models.Model):
    appointmentId=models.PositiveIntegerField(null=True)
    pharmacyId=models.PositiveIntegerField(null=True)
    doctorId=models.PositiveIntegerField(null=True)
    patientId=models.PositiveIntegerField(null=True)
    doctorName=models.CharField(max_length=40,null=True)
    patientName=models.CharField(max_length=40,null=True)
    pharmacyName=models.CharField(max_length=40)
    medicineName=models.CharField(max_length=40)
    #TODO: Conrad
    #add those new fields here 
    #dosageForm = models.CharField(max_length=40) eg tablet or liquid, this is just an example of what is put
    #dosageStrength = models.CharField(max_length=40)
    dosageInstruction=models.TextField(max_length=500, null=True)
    sideEffects=models.TextField(max_length=500, null=True)
    status=models.BooleanField(default=False)
    datestamp=models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.pharmacyName + ' - ' + self.medicineName


class Feedback(models.Model):
    userId=models.PositiveIntegerField(null=True)
    message=models.TextField(max_length=500, null=True)
    def __str__(self):
        return self.message



