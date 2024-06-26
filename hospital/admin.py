from django.contrib import admin
from .models import Doctor,Patient,Appointment, Admin, Hospital, Receptionist, Pharmacy, Prescription, AdminPharmacy, PharmacyInventory, PatientDetails
# Register your models here.
class DoctorAdmin(admin.ModelAdmin):
    pass
admin.site.register(Doctor, DoctorAdmin)

class AdminAdmin(admin.ModelAdmin):
    pass
admin.site.register(Admin, AdminAdmin)

class HospitalAdmin(admin.ModelAdmin):
    pass
admin.site.register(Hospital, HospitalAdmin)

class PharmacyAdmin(admin.ModelAdmin):
    pass
admin.site.register(Pharmacy, PharmacyAdmin)

class ReceptionistAdmin(admin.ModelAdmin):
    pass
admin.site.register(Receptionist, ReceptionistAdmin)

class PrescriptionAdmin(admin.ModelAdmin):
    pass
admin.site.register(Prescription, PrescriptionAdmin)

class PatientAdmin(admin.ModelAdmin):
    pass
admin.site.register(Patient, PatientAdmin)

class AppointmentAdmin(admin.ModelAdmin):
    pass
admin.site.register(Appointment, AppointmentAdmin)

class AdminPharmacyAdmin(admin.ModelAdmin):
    pass
admin.site.register(AdminPharmacy, AdminPharmacyAdmin)

class PharmacyInventoryAdmin(admin.ModelAdmin):
    pass
admin.site.register(PharmacyInventory, PharmacyInventoryAdmin)

class PatientDetailsAdmin(admin.ModelAdmin):
    pass
admin.site.register(PatientDetails, PatientDetailsAdmin)
