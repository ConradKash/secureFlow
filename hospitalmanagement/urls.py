from django.contrib import admin
from django.urls import path
from hospital import views
from hospital.feedback import views as feedback_views
from django.contrib.auth.views import LoginView,LogoutView


#-------------FOR ADMIN RELATED URLS
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home_view,name=''),


    path('aboutus', views.aboutus_view),
    path('contactus', views.contactus_view),


    path('adminclick', views.adminclick_view),
    path('admin_pharmacyclick', views.admin_pharmacyclick_view),
    path('doctorclick', views.doctorclick_view),
    path('patientclick', views.patientclick_view),

    path('adminsignup', views.admin_signup_view),
    path('admin_pharmacysignup', views.admin_pharmacy_signup_view),
    path('doctorsignup', views.doctor_signup_view,name='doctorsignup'),
    path('patientsignup', views.patient_signup_view),

    path('login', LoginView.as_view(template_name='hospital/patientlogin.html')),


    path('afterlogin', views.afterlogin_view,name='afterlogin'),
    path('logout', LogoutView.as_view(template_name='hospital/index.html'),name='logout'),


    path('admin-dashboard', views.admin_dashboard_view,name='admin-dashboard'),

    path('admin-doctor', views.admin_doctor_view,name='admin-doctor'),
    path('admin-view-doctor', views.admin_view_doctor_view,name='admin-view-doctor'),
    path('delete-doctor-from-hospital/<int:pk>', views.delete_doctor_from_hospital_view,name='delete-doctor-from-hospital'),
    path('update-doctor/<int:pk>', views.update_doctor_view,name='update-doctor'),
    path('admin-add-doctor', views.admin_add_doctor_view,name='admin-add-doctor'),
    path('admin-approve-doctor', views.admin_approve_doctor_view,name='admin-approve-doctor'),
    path('approve-doctor/<int:pk>', views.approve_doctor_view,name='approve-doctor'),
    path('reject-doctor/<int:pk>', views.reject_doctor_view,name='reject-doctor'),
    path('admin-view-doctor-specialisation',views.admin_view_doctor_specialisation_view,name='admin-view-doctor-specialisation'),

    path('admin-receptionist', views.admin_receptionist_view,name='admin-receptionist'),
    path('admin-view-receptionist', views.admin_view_receptionist_view,name='admin-view-receptionist'),
    path('delete-receptionist-from-hospital/<int:pk>', views.delete_receptionist_from_hospital_view,name='delete-receptionist-from-hospital'),
    path('update-receptionist/<int:pk>', views.update_receptionist_view,name='update-receptionist'),
    path('admin-add-receptionist', views.admin_add_receptionist_view,name='admin-add-receptionist'),
    path('admin-approve-receptionist', views.admin_approve_receptionist_view,name='admin-approve-receptionist'),
    path('approve-receptionist/<int:pk>', views.approve_receptionist_view,name='approve-receptionist'),
    path('reject-receptionist/<int:pk>', views.reject_receptionist_view,name='reject-receptionist'),

    path('admin-patient', views.admin_patient_view,name='admin-patient'),
    path('admin-view-patient', views.admin_view_patient_view,name='admin-view-patient'),
    path('delete-patient-from-hospital/<int:pk>', views.delete_patient_from_hospital_view,name='delete-patient-from-hospital'),
    path('update-patient/<int:pk>', views.update_patient_view,name='update-patient'),
    path('admin-add-patient', views.admin_add_patient_view,name='admin-add-patient'),
    
    path('admin-appointment', views.admin_appointment_view,name='admin-appointment'),
    path('admin-view-appointment', views.admin_view_appointment_view,name='admin-view-appointment'),
    path('admin-add-appointment', views.admin_add_appointment_view,name='admin-add-appointment'),
    path('admin-approve-appointment', views.admin_approve_appointment_view,name='admin-approve-appointment'),
    path('approve-appointment/<int:pk>', views.approve_appointment_view,name='approve-appointment'),
    path('reject-appointment/<int:pk>', views.reject_appointment_view,name='reject-appointment'),

 #---------FOR ADMIN - HOSPITAL RELATED URLS-------------------------------------
    path('admin-pharmacy', views.admin_pharmacy_view,name='admin-pharmacy'),
    path('admin-add-pharmacy', views.admin_add_pharmacy_view,name='admin-add-pharmacy'),
    path('admin-view-pharmacy', views.admin_view_pharmacy_view,name='admin-view-pharmacy'),
    path('delete-pharmacy-from-hospital/<int:pk>', views.delete_pharmacy_from_hospital_view,name='delete-pharmacy-from-hospital'),
    path('update-pharmacy/<int:pk>', views.update_pharmacy_view,name='update-pharmacy'),

 #---------FOR ADMIN - HOSPITAL RELATED URLS-------------------------------------
    path('admin-hospital', views.admin_hospital_view,name='admin-hospital'),
    path('admin-add-hospital', views.admin_add_hospital_view,name='admin-add-hospital'),
    path('admin-view-hospital', views.admin_view_hospital_view,name='admin-view-hospital'),
    path('delete-hospital-from-hospital/<int:pk>', views.delete_hospital_from_hospital_view,name='delete-hospital-from-hospital'),
    path('update-hospital/<int:pk>', views.update_hospital_view,name='update-hospital'),
]

 #---------FOR DOCTOR RELATED URLS-------------------------------------
urlpatterns +=[
    
    path('doctor-dashboard', views.doctor_dashboard_view,name='doctor-dashboard'),
    path('doctor-patient', views.doctor_patient_view,name='doctor-patient'),
    path('doctor-view-patient', views.doctor_view_patient_view,name='doctor-view-patient'),
    path('doctor-appointment', views.doctor_appointment_view,name='doctor-appointment'),
    path('doctor-view-appointment', views.doctor_view_appointment_view,name='doctor-view-appointment'),
    path('doctor-delete-appointment',views.doctor_delete_appointment_view,name='doctor-delete-appointment'),
    path('delete-appointment/<int:pk>', views.delete_appointment_view,name='delete-appointment'),
    path('doctor-view-patient-detail',views.doctor_patientDetail_view,name='doctor-view-patient-detail'),
    path('create-patient-details/<int:pk>', views.create_patientdetail_view,name='create-patient-details'),
    path('patient-details', views.admin_add_patientDetail_view,name='patient-details'),
    path('doctor-patient-details', views.doctor_add_patientDetail_view,name='doctor-patient-details'),
    path('doctor-add-prescription', views.doctor_add_prescription_view,name='doctor-add-prescription'),
]




#---------FOR PATIENT RELATED URLS-------------------------------------
urlpatterns +=[

    path('patient-dashboard', views.patient_dashboard_view,name='patient-dashboard'),
    path('patient-appointment', views.patient_appointment_view,name='patient-appointment'),
    path('patient-book-appointment', views.doctor_add_appointment_view,name='patient-book-appointment'),
    path('patient-view-appointment', views.patient_view_appointment_view,name='patient-view-appointment'),

]

urlpatterns +=[
    path('admin-pharmacy-dashboard', views.admin_pharmacy_dashboard_view,name='admin-pharmacy-dashboard'),
    # path('admin-pharmacy-prescription', views.admin_pharmacy_presciption,name='admin-pharmacy-prescription'),
    path('admin-pharmacy-inventory_view', views.admin_pharmacy_inventory_view,name='admin-pharmacy-inventory_view'),
    path('admin-pharmacy-invetory-add', views.admin_add_pharmacy_inventory_view,name='admin-pharmacy-invetory-add'),
    path('admin-prescription-prescribe/<int:pk>', views.approve_prescription_view, name='admin-prescription-prescribe'),
    path('admin-pharmacy-prescriptions/', views.get_all_prescriptions, name='admin-pharmacy-prescriptions')
]


