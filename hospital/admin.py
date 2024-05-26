from django.contrib import admin
from .models import Doctor,Patient,Appointment,PatientDischargeDetails, Admin, Hospital, Receptionist, Pharmacy
# Register your models here.
class DoctorAdmin(admin.ModelAdmin):
    pass
admin.site.register(Doctor, DoctorAdmin)

class PatientAdmin(admin.ModelAdmin):
    pass
admin.site.register(Patient, PatientAdmin)

class AppointmentAdmin(admin.ModelAdmin):
    pass
admin.site.register(Appointment, AppointmentAdmin)

class PatientDischargeDetailsAdmin(admin.ModelAdmin):
    pass
admin.site.register(PatientDischargeDetails, PatientDischargeDetailsAdmin)

class AdminAdmin(admin.ModelAdmin):
    pass    
admin.site.register(Admin, AdminAdmin)

class HospitalAdmin(admin.ModelAdmin):
    pass
admin.site.register(Hospital, HospitalAdmin)

class ReceptionistAdmin(admin.ModelAdmin):
    pass
admin.site.register(Receptionist, ReceptionistAdmin)

class PharmacyAdmin(admin.ModelAdmin):
    pass
admin.site.register(Pharmacy, PharmacyAdmin)
