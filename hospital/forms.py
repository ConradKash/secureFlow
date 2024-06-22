from django import forms
from django.contrib.auth.models import User
from django.contrib.admin.widgets import AdminDateWidget
from . import models



#for admin signup
class AdminUserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','username','password']
        widgets = {
        'password': forms.PasswordInput()
        }

class AdminForm(forms.ModelForm):
    hospitalId=forms.ModelChoiceField(queryset=models.Hospital.objects.all().filter(is_approved=True),empty_label="Hospital Name", to_field_name="id")
    class Meta:
        model=models.Admin
        fields=['address','mobile','status','profile_pic']

class AdminPharmacyForm(forms.ModelForm):
    
    pharmacyId=forms.ModelChoiceField(queryset=models.Pharmacy.objects.all().filter(is_approved=True),empty_label="Pharmacy Name", to_field_name="id")
    class Meta:
        model=models.AdminPharmacy
        fields=['address','mobile','status','profile_pic']

class HospitalForm(forms.ModelForm):
    class Meta:
        model=models.Hospital
        fields=['name', 'address', 'contact', 'email', 'logo']

class PharmacyForm(forms.ModelForm):
    class Meta:
        model=models.Pharmacy
        fields=['name', 'address', 'contact', 'email', 'logo', 'is_approved']      
        
#for student related form
class DoctorUserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','username','password']
        widgets = {
        'password': forms.PasswordInput()
        }
class DoctorForm(forms.ModelForm):
    hospitalId=forms.ModelChoiceField(queryset=models.Hospital.objects.all().filter(is_approved=True),empty_label="Hospital Name", to_field_name="id")
    class Meta:
        model=models.Doctor
        fields=['address','mobile','department','status','profile_pic']

class ReceptionistUserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','username','password']
        widgets = {
        'password': forms.PasswordInput()
        }
class ReceptionistForm(forms.ModelForm):
    
    hospitalId=forms.ModelChoiceField(queryset=models.Hospital.objects.all().filter(is_approved=True),empty_label="Hospital Name", to_field_name="id")
    class Meta:
        model=models.Receptionist
        fields=['address','mobile','status','profile_pic']
#for teacher related form
class PatientUserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','username','password']
        widgets = {
        'password': forms.PasswordInput()
        }
class PatientForm(forms.ModelForm):
    #this is the extrafield for linking patient and their assigend doctor
    #this will show dropdown __str__ method doctor model is shown on html so override it
    #to_field_name this will fetch corresponding value  user_id present in Doctor model and return it
    class Meta:
        model=models.Patient
        fields=['address','mobile','profile_pic']



class AppointmentForm(forms.ModelForm):
    doctorId = forms.ModelChoiceField(queryset=models.Doctor.objects.all().filter(status=True), empty_label="Doctor Name and Department", to_field_name="user_id")
    hospitalId = forms.ModelChoiceField(queryset=models.Hospital.objects.all().filter(is_approved=True), empty_label="Choose a hospital", to_field_name="id")
    patientId = forms.ModelChoiceField(queryset=models.Patient.objects.all(), empty_label="Patient Name and Symptoms", to_field_name="user_id")

    class Meta:
        model = models.Appointment
        fields = ['description', 'status', 'appointmentDate']
        widgets = {
            "appointmentDate": AdminDateWidget(),
        }

class AppointmentDoctorForm(forms.ModelForm):
    doctorId = forms.ModelChoiceField(queryset=models.Doctor.objects.all().filter(status=True), empty_label="Doctor Name and Department", to_field_name="user_id")

    class Meta:
        model = models.Appointment
        fields = ['description', 'appointmentDate']
        widgets = {
            "appointmentDate": AdminDateWidget(),
        }

class PatientDetailsAdminForm(forms.ModelForm):
    patientId = forms.ModelChoiceField(queryset=models.Patient.objects.all(), empty_label="Patient Name and Symptoms", to_field_name="user_id")
    appointmentId = forms.ModelChoiceField(queryset=models.Appointment.objects.all().filter(status=True), empty_label="Choose a hospital", to_field_name="id")
    doctorId = forms.ModelChoiceField(queryset=models.Doctor.objects.all().filter(status=True), empty_label="Doctor Name and Department", to_field_name="user_id")
    class Meta:
        model = models.PatientDetailsAdmin
        fields = [
            'height',
            'weight',
            'temperature',
            'medical_history',
            'currentMedication',
            'currentSymptoms',
            'allergies',
            'medicalConcerns',
            'diagnosis',
            'treatment'   
        ]
        
    

class PatientDetailsForm(forms.ModelForm):
    class Meta:
        model = models.PatientDetails
        fields = ['height', 'weight', 'blood_sugar', 'heart_rate', 'temperature', 'symptoms','diagnosis', 'treatment']

class PrescriptionForm(forms.ModelForm):
    doctorId = forms.ModelChoiceField(queryset=models.Doctor.objects.all().filter(status=True), empty_label="Doctor Name and Department", to_field_name="user_id")
    patientId = forms.ModelChoiceField(queryset=models.Patient.objects.all(), empty_label="Patient Name and Symptoms", to_field_name="user_id")
    pharmacyId = forms.ModelChoiceField(queryset=models.Pharmacy.objects.all().filter(is_approved=True), empty_label="Pharmacy Name", to_field_name="id")
    appointmentId = forms.ModelChoiceField(queryset=models.Appointment.objects.all().filter(status=True), empty_label="Choose a hospital", to_field_name="id")

    class Meta:
        model = models.Prescription
        fields = ['medicineName',
                  'dosageInstruction',
                  'sideEffects',
                  'status',             
                  ]

class PharmacyInventoryForm(forms.ModelForm):
    class Meta:
        model = models.PharmacyInventory
        fields = [
                  'medicineName',
                  'description',
                  'price',
                  'stock',]
        exclude =[ 'pharmacyId', 'status']

#for contact us page

   
# class ContactusForm(forms.Form):
#     Name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Your Name', 'class': 'form-control'}))
#     Email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Your Email', 'class': 'form-control'}))
#     Message = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Your Message', 'rows': 4, 'class': 'form-control'}))
class ContactusForm(forms.Form):
    name = forms.CharField(label='Name', max_length=100)
    email = forms.EmailField(label='Email')
    message = forms.CharField(label='Message', widget=forms.Textarea)

