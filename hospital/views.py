from django.shortcuts import render,redirect,reverse
from . import forms,models
from django.db.models import Sum
from django.contrib.auth.models import Group
from django.http import HttpResponseRedirect
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required,user_passes_test
from datetime import datetime,timedelta,date
from django.conf import settings

# Create your views here.
def home_view(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('afterlogin')
    return render(request,'hospital/index.html')


#for showing signup/login button for admin(by sumit)
def adminclick_view(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('afterlogin')
    return render(request,'hospital/adminclick.html')

def admin_pharmacyclick_view(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('afterlogin')
    return render(request,'hospital/admin_pharmacyclick.html')

#for showing signup/login button for doctor(by sumit)
def doctorclick_view(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('afterlogin')
    return render(request,'hospital/doctorclick.html')

#for showing signup/login button for doctor(by sumit)
def receptionistclick_view(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('afterlogin')
    return render(request,'hospital/receptionistclick.html')


#for showing signup/login button for patient(by sumit)
def patientclick_view(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('afterlogin')
    return render(request,'hospital/patientclick.html')

def admin_signup_view(request):
    userForm=forms.AdminUserForm()
    adminForm=forms.AdminForm()
    mydict={'userForm':userForm,'adminForm':adminForm}
    if request.method=='POST':
        userForm=forms.AdminUserForm(request.POST)
        adminForm=forms.AdminForm(request.POST, request.FILES)
        if userForm.is_valid() and adminForm.is_valid():
            user=userForm.save()
            user.set_password(user.password)
            user.save()
            
            admin=adminForm.save(commit=False)
            admin.user=user
            admin.hospitalId=request.POST.get('hospitalId')
            admin.status=False
            admin.save()

            my_admin_group = Group.objects.get_or_create(name='ADMIN')
            my_admin_group[0].user_set.add(user)
        return HttpResponseRedirect('adminlogin')
    return render(request,'hospital/adminsignup.html',context=mydict)

def admin_pharmacy_signup_view(request):
    userForm=forms.AdminUserForm()
    adminForm=forms.AdminPharmacyForm()
    mydict={'userForm':userForm,'adminForm':adminForm}
    if request.method=='POST':
        userForm=forms.AdminUserForm(request.POST)
        adminForm=forms.AdminPharmacyForm(request.POST, request.FILES)
        if userForm.is_valid() and adminForm.is_valid():
            user=userForm.save()
            user.set_password(user.password)
            user.save()
            
            admin=adminForm.save(commit=False)
            admin.user=user
            admin.pharmacyId=request.POST.get('pharmacyId')
            admin.status=False
            admin.save()

            my_admin_group = Group.objects.get_or_create(name='ADMINPHARMACY')
            my_admin_group[0].user_set.add(user)
        return HttpResponseRedirect('adminPharmacylogin')
    return render(request,'hospital/admin_pharmacysignup.html',context=mydict)

def doctor_signup_view(request):
    userForm=forms.DoctorUserForm()
    doctorForm=forms.DoctorForm()
    mydict={'userForm':userForm,'doctorForm':doctorForm}
    if request.method=='POST':
        userForm=forms.DoctorUserForm(request.POST)
        doctorForm=forms.DoctorForm(request.POST, request.FILES)

        if userForm.is_valid() and doctorForm.is_valid():
            user=userForm.save()
            user.set_password(user.password)
            user.save()
            
            doctor=doctorForm.save(commit=False)
            doctor.user=user
            doctor.hospitalId=request.POST.get('hospitalId')
            doctor.status=False
            doctor.save()
            
            my_doctor_group = Group.objects.get_or_create(name='DOCTOR')
            my_doctor_group[0].user_set.add(user)
        return HttpResponseRedirect('doctorlogin')
    return render(request,'hospital/doctorsignup.html',context=mydict)

def patient_signup_view(request):
    userForm=forms.PatientUserForm()
    patientForm=forms.PatientForm()
    mydict={'userForm':userForm,'patientForm':patientForm}
    if request.method=='POST':
        userForm=forms.PatientUserForm(request.POST)
        patientForm=forms.PatientForm(request.POST,request.FILES)
        if userForm.is_valid() and patientForm.is_valid():
            user=userForm.save()
            user.set_password(user.password)
            user.save()
            patient=patientForm.save(commit=False)
            patient.user=user
            patient=patient.save()
            my_patient_group = Group.objects.get_or_create(name='PATIENT')
            my_patient_group[0].user_set.add(user)
        return HttpResponseRedirect('patientlogin')
    return render(request,'hospital/patientsignup.html',context=mydict)






#-----------for checking user is doctor , patient or admin(by sumit)
def is_admin(user):
    return user.groups.filter(name='ADMIN').exists()
def is_admin_pharmacy(user):
    return user.groups.filter(name='ADMINPHARMACY').exists()
def is_doctor(user):
    return user.groups.filter(name='DOCTOR').exists()
def is_receptionist(user):
    return user.groups.filter(name='RECEPTIONIST').exists()
def is_patient(user):
    return user.groups.filter(name='PATIENT').exists()


#---------AFTER ENTERING CREDENTIALS WE CHECK WHETHER USERNAME AND PASSWORD IS OF ADMIN,DOCTOR OR PATIENT
def afterlogin_view(request):
    if is_admin(request.user):
        accountapproval=models.Admin.objects.all().filter(user_id=request.user.id,status=True)
        if accountapproval:
            return redirect('admin-dashboard')
        else:
            return render(request,'hospital/admin_wait_for_approval.html')
    elif is_admin_pharmacy(request.user):
        accountapproval=models.AdminPharmacy.objects.all().filter(user_id=request.user.id,status=True)
        if accountapproval:
            return redirect('admin-pharmacy-dashboard')
        else:
            return render(request,'hospital/admin_wait_for_approval.html')
    elif is_doctor(request.user):
        accountapproval=models.Doctor.objects.all().filter(user_id=request.user.id,status=True)
        if accountapproval:
            return redirect('doctor-dashboard')
        else:
            return render(request,'hospital/doctor_wait_for_approval.html')
    elif is_receptionist(request.user):
        accountapproval=models.Receptionist.objects.all().filter(user_id=request.user.id,status=True)
        if accountapproval:
            return redirect('receptionist-dashboard')
        else:
            return render(request,'hospital/receptionist_wait_for_approval.html')
    elif is_patient(request.user):
        return redirect('patient-dashboard')
    
#---------------------------------------------------------------------------------
#------------------------ ADMIN RELATED VIEWS START ------------------------------
#---------------------------------------------------------------------------------
@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def admin_dashboard_view(request):
    #for both table in admin dashboard
    doctors=models.Doctor.objects.all().order_by('-id')
    patients=models.Patient.objects.all().order_by('-id')
    #for three cards
    doctorcount=models.Doctor.objects.all().filter(status=True).count()
    pendingdoctorcount=models.Doctor.objects.all().count()

    patientcount=models.Patient.objects.all().count()
    pendingpatientcount=models.Patient.objects.all().count()

    appointmentcount=models.Appointment.objects.all().filter(status=True).count()
    pendingappointmentcount=models.Appointment.objects.all().filter(status=False).count()
    mydict={
    'doctors':doctors,
    'patients':patients,
    'doctorcount':doctorcount,
    'pendingdoctorcount':pendingdoctorcount,
    'patientcount':patientcount,
    'pendingpatientcount':pendingpatientcount,
    'appointmentcount':appointmentcount,
    'pendingappointmentcount':pendingappointmentcount,
    }
    return render(request,'hospital/admin_dashboard.html',context=mydict)


# this view for sidebar click on admin page
@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def admin_doctor_view(request):
    return render(request,'hospital/admin_doctor.html')



@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def admin_view_doctor_view(request):
    doctors=models.Doctor.objects.all().filter(status=True)
    return render(request,'hospital/admin_view_doctor.html',{'doctors':doctors})



@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def delete_doctor_from_hospital_view(request,pk):
    doctor=models.Doctor.objects.get(id=pk)
    user=models.User.objects.get(id=doctor.user_id)
    user.delete()
    doctor.delete()
    return redirect('admin-view-doctor')



@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def update_doctor_view(request,pk):
    doctor=models.Doctor.objects.get(id=pk)
    user=models.User.objects.get(id=doctor.user_id)

    userForm=forms.DoctorUserForm(instance=user)
    doctorForm=forms.DoctorForm(request.FILES,instance=doctor)
    mydict={'userForm':userForm,'doctorForm':doctorForm}
    if request.method=='POST':
        userForm=forms.DoctorUserForm(request.POST,instance=user)
        doctorForm=forms.DoctorForm(request.POST,request.FILES,instance=doctor)
        if userForm.is_valid() and doctorForm.is_valid():
            user=userForm.save()
            user.set_password(user.password)
            user.save()
            doctor=doctorForm.save(commit=False)
            doctor.status=True
            doctor.save()
            return redirect('admin-view-doctor')
    return render(request,'hospital/admin_update_doctor.html',context=mydict)




@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def admin_add_doctor_view(request):
    userForm=forms.DoctorUserForm()
    doctorForm=forms.DoctorForm()
    mydict={'userForm':userForm,'doctorForm':doctorForm}
    if request.method=='POST':
        userForm=forms.DoctorUserForm(request.POST)
        doctorForm=forms.DoctorForm(request.POST, request.FILES)
        if userForm.is_valid() and doctorForm.is_valid():
            user=userForm.save()
            user.set_password(user.password)
            user.save()

            doctor=doctorForm.save(commit=False)
            doctor.user=user
            doctor.hospitalId=request.POST.get('hospitalId')
            doctor.status=True
            doctor.save()

            my_doctor_group = Group.objects.get_or_create(name='DOCTOR')
            my_doctor_group[0].user_set.add(user)

        return HttpResponseRedirect('admin-view-doctor')
    return render(request,'hospital/admin_add_doctor.html',context=mydict)




@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def admin_approve_doctor_view(request):
    #those whose approval are needed
    doctors=models.Doctor.objects.all().filter(status=False)
    return render(request,'hospital/admin_approve_doctor.html',{'doctors':doctors})


@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def approve_doctor_view(request,pk):
    doctor=models.Doctor.objects.get(id=pk)
    doctor.status=True
    doctor.save()
    return redirect(reverse('admin-approve-doctor'))


@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def reject_doctor_view(request,pk):
    doctor=models.Doctor.objects.get(id=pk)
    user=models.User.objects.get(id=doctor.user_id)
    user.delete()
    doctor.delete()
    return redirect('admin-approve-doctor')



@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def admin_view_doctor_specialisation_view(request):
    doctors=models.Doctor.objects.all().filter(status=True)
    return render(request,'hospital/admin_view_doctor_specialisation.html',{'doctors':doctors})



@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def admin_patient_view(request):
    return render(request,'hospital/admin_patient.html')



@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def admin_view_patient_view(request):
    patients=models.Patient.objects.all()
    return render(request,'hospital/admin_view_patient.html',{'patients':patients})



@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def delete_patient_from_hospital_view(request,pk):
    patient=models.Patient.objects.get(id=pk)
    user=models.User.objects.get(id=patient.user_id)
    user.delete()
    patient.delete()
    return redirect('admin-view-patient')



@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def update_patient_view(request,pk):
    patient=models.Patient.objects.get(id=pk)
    user=models.User.objects.get(id=patient.user_id)

    userForm=forms.PatientUserForm(instance=user)
    patientForm=forms.PatientForm(request.FILES,instance=patient)
    mydict={'userForm':userForm,'patientForm':patientForm}
    if request.method=='POST':
        userForm=forms.PatientUserForm(request.POST,instance=user)
        patientForm=forms.PatientForm(request.POST,request.FILES,instance=patient)
        if userForm.is_valid() and patientForm.is_valid():
            user=userForm.save()
            user.set_password(user.password)
            user.save()
            
            patient=patientForm.save(commit=False)
            patient.save()
            return redirect('admin-view-patient')
    return render(request,'hospital/admin_update_patient.html',context=mydict)

#------------------FOR HOSPITAL BY ADMIN----------------------

@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def admin_hospital_view(request):
    return render(request,'hospital/admin_hospital.html')

@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def admin_add_hospital_view(request):
    hospitalForm=forms.HospitalForm()
    mydict={'hospitalForm':hospitalForm}
    if request.method=='POST':
        hospitalForm = forms.HospitalForm(request.POST)
        if hospitalForm.is_valid():
            hospital =hospitalForm.save(commit=False)
            hospital.name=request.POST.get('name')
            hospital.address=request.POST.get('address')
            hospital.contact=request.POST.get('contact')
            hospital.email=request.POST.get('email')
            hospital.logo=request.POST.get('logo')
            hospital.is_approved=True
            hospital.save()
        return HttpResponseRedirect('admin-add-hospital')
    return render(request,'hospital/admin_add_hospital.html',context=mydict)

@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def admin_view_hospital_view(request):
    hospital=models.Hospital.objects.all().filter(is_approved=True)
    return render(request,'hospital/admin_view_hospital.html',{'hospital':hospital})

@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def update_hospital_view(request,pk):
    hospital=models.Hospital.objects.get(id=pk)    
    hospitalForm=forms.HospitalForm(request.FILES, instance=hospital)
    mydict={'hospitalForm':hospitalForm}
    if request.method=='POST':
        hospitalForm=forms.HospitalForm(request.POST,request.FILES,instance=hospital)
        if hospitalForm.is_valid():
            hospital=hospitalForm.save(commit=False)
            hospital.status=True
            hospital.save()
            return redirect('admin-view-hospital')
    return render(request,'hospital/admin_update_hospital.html',context=mydict)

@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def delete_hospital_from_hospital_view(request, pk):
    hospital=models.Hospital.objects.get(id=pk)
    hospital.delete()
    return redirect('admin-view-hospital')

#------------------FOR HOSPITAL BY ADMIN----------------------

@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def admin_pharmacy_view(request):
    return render(request,'hospital/admin_pharmacy.html')

@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def admin_add_pharmacy_view(request):
    pharmacyForm=forms.PharmacyForm()
    mydict={'pharmacyForm':pharmacyForm}
    if request.method=='POST':
        pharmacyForm = forms.PharmacyForm(request.POST)
        if pharmacyForm.is_valid():
            pharmacy =pharmacyForm.save(commit=False)
            pharmacy.name=request.POST.get('name')
            pharmacy.address=request.POST.get('address')
            pharmacy.contact=request.POST.get('contact')
            pharmacy.email=request.POST.get('email')
            pharmacy.logo=request.POST.get('logo')
            pharmacy.is_approved=True
            pharmacy.save()
        return HttpResponseRedirect('admin-add-pharmacy')
    return render(request,'hospital/admin_add_pharmacy.html',context=mydict)

@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def admin_add_patientDetail_view(request):
    patientDetailsAdminForm=forms.PatientDetailsAdminForm()
    mydict={'patientDetailsAdminForm':patientDetailsAdminForm}
    if request.method=='POST':
        patientDetailsAdminForm = forms.PatientDetailsAdminForm(request.POST)
        if patientDetailsAdminForm.is_valid():
            patientDetailsAdmin =patientDetailsAdminForm.save(commit=False)
            patientDetailsAdmin.patientId=request.POST.get('patientId')
            patientDetailsAdmin.appointmentId=request.POST.get('appointmentId')
            patientDetailsAdmin.doctorId=request.POST.get('doctorId')
            patientDetailsAdmin.height=request.POST.get('height')
            patientDetailsAdmin.weight=request.POST.get('weight')
            patientDetailsAdmin.temperature=request.POST.get('temperature')
            patientDetailsAdmin.medical_history=request.POST.get('medical_history')
            patientDetailsAdmin.currentMedication=request.POST.get('currentMedication')
            patientDetailsAdmin.currentSymptoms=request.POST.get('currentSymptoms')
            patientDetailsAdmin.allergies=request.POST.get('allergies')
            patientDetailsAdmin.medicalConcerns=request.POST.get('medicalConcerns')
            patientDetailsAdmin.diagnosis=request.POST.get('diagnosis')
            patientDetailsAdmin.treatment=request.POST.get('treatment')
            patientDetailsAdmin.save()
        return HttpResponseRedirect('admin-view-doctor')
    return render(request,'hospital/admin_add_patient_details.html',context=mydict)


@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def admin_view_pharmacy_view(request):
    pharmacy=models.Pharmacy.objects.all().filter(is_approved=True)
    return render(request,'hospital/admin_view_pharmacy.html',{'pharmacy':pharmacy})

@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def update_pharmacy_view(request,pk):
    pharmacy=models.Pharmacy.objects.get(id=pk) 
    pharmacyForm=forms.PharmacyForm(request.FILES, instance=pharmacy)
    mydict={'pharmacyForm':pharmacyForm}
    if request.method=='POST':
        pharmacyForm=forms.PharmacyForm(request.POST,request.FILES,instance=pharmacy)
        if pharmacyForm.is_valid():
            pharmacy=pharmacyForm.save(commit=False)
            pharmacy.status=True
            pharmacy.save()
            return redirect('admin-view-pharmacy')
    return render(request,'hospital/admin_update_pharmacy.html',context=mydict)

@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def delete_pharmacy_from_hospital_view(request, pk):
    pharmacy=models.Pharmacy.objects.get(id=pk)
    pharmacy.delete()
    return redirect('admin-view-pharmacy')

#------------------FOR ADDING PATIENT BY ADMIN----------------------
@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def admin_add_patient_view(request):
    userForm=forms.PatientUserForm()
    patientForm=forms.PatientForm()
    mydict={'userForm':userForm,'patientForm':patientForm}
    if request.method=='POST':
        userForm=forms.PatientUserForm(request.POST)
        patientForm=forms.PatientForm(request.POST,request.FILES)
        if userForm.is_valid() and patientForm.is_valid():
            user=userForm.save()
            user.set_password(user.password)
            user.save()

            patient=patientForm.save(commit=False)
            patient.user=user
            patient.save()

            my_patient_group = Group.objects.get_or_create(name='PATIENT')
            my_patient_group[0].user_set.add(user)

        return HttpResponseRedirect('admin-view-patient')
    return render(request,'hospital/admin_add_patient.html',context=mydict)


# ------------------FOR APPROVING RECEPTIONIST BY ADMIN----------------------

@login_required(login_url='receptionistlogin')
@user_passes_test(is_admin)
def admin_receptionist_view(request):
    return render(request,'hospital/admin_receptionist.html')



@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def admin_view_receptionist_view(request):
    receptionists=models.Receptionist.objects.all().filter(status=True)
    return render(request,'hospital/admin_view_receptionist.html',{'receptionists':receptionists})



@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def delete_receptionist_from_hospital_view(request,pk):
    receptionist=models.Receptionist.objects.get(id=pk)
    user=models.User.objects.get(id=receptionist.user_id)
    user.delete()
    receptionist.delete()
    return redirect('admin-view-receptionist')



@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def update_receptionist_view(request,pk):
    receptionist=models.Receptionist.objects.get(id=pk)
    user=models.User.objects.get(id=receptionist.user_id)

    userForm=forms.ReceptionistUserForm(instance=user)
    receptionistForm=forms.ReceptionistForm(request.FILES,instance=receptionist)
    mydict={'userForm':userForm,'receptionistForm':receptionistForm}
    if request.method=='POST':
        userForm=forms.ReceptionistUserForm(request.POST,instance=user)
        receptionistForm=forms.ReceptionistForm(request.POST,request.FILES,instance=receptionist)
        if userForm.is_valid() and receptionistForm.is_valid():
            user=userForm.save()
            user.set_password(user.password)
            user.save()
            receptionist=receptionistForm.save(commit=False)
            receptionist.status=True
            receptionist.save()
            return redirect('admin-view-receptionist')
    return render(request,'hospital/admin_update_receptionist.html',context=mydict)


@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def admin_add_receptionist_view(request):
    userForm=forms.ReceptionistUserForm()
    receptionistForm=forms.ReceptionistForm()
    mydict={'userForm':userForm,'receptionistForm':receptionistForm}
    if request.method=='POST':
        userForm=forms.ReceptionistUserForm(request.POST)
        receptionistForm=forms.ReceptionistForm(request.POST, request.FILES)
        if userForm.is_valid() and receptionistForm.is_valid():
            user=userForm.save()
            user.set_password(user.password)
            user.save()
            
            receptionist=receptionistForm.save(commit=False)
            receptionist.user=user
            receptionist.hospitalId=request.POST.get('hospitalId')
            receptionist.status=True
            receptionist.save()

            my_receptionist_group = Group.objects.get_or_create(name='RECECPTIONIST')
            my_receptionist_group[0].user_set.add(user)

        return HttpResponseRedirect('admin-view-receptionist')
    return render(request,'hospital/admin_add_receptionist.html',context=mydict)




@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def admin_approve_receptionist_view(request):
    #those whose approval are needed
    receptionists=models.Receptionist.objects.all().filter(status=False)
    return render(request,'hospital/admin_approve_receptionist.html',{'receptionists':receptionists})


@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def approve_receptionist_view(request,pk):
    receptionist=models.Receptionist.objects.get(id=pk)
    receptionist.status=True
    receptionist.save()
    return redirect(reverse('admin-approve-receptionist'))


@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def reject_receptionist_view(request,pk):
    receptionist=models.Receptionist.objects.get(id=pk)
    user=models.User.objects.get(id=receptionist.user_id)
    user.delete()
    receptionist.delete()
    return redirect('admin-approve-receptionist')

#-----------------APPOINTMENT START--------------------------------------------------------------------
@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def admin_appointment_view(request):
    return render(request,'hospital/admin_appointment.html')



@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def admin_view_appointment_view(request):
    appointments=models.Appointment.objects.all().filter(status=True)
    return render(request,'hospital/admin_view_appointment.html',{'appointments':appointments})



@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def admin_add_appointment_view(request):
    appointmentForm=forms.AppointmentForm()
    mydict={'appointmentForm':appointmentForm,}
    if request.method=='POST':
        appointmentForm=forms.AppointmentForm(request.POST)
        if appointmentForm.is_valid():
            appointment=appointmentForm.save(commit=False)
            appointment.doctorId=request.POST.get('doctorId')
            appointment.hospitalId=request.POST.get('hospitalId')
            appointment.patientId=request.POST.get('patientId')
            appointment.doctorName=models.User.objects.get(id=request.POST.get('doctorId')).first_name
            appointment.hospitalName=models.Hospital.objects.get(id=request.POST.get('hospitalId')).name
            appointment.patientName=models.User.objects.get(id=request.POST.get('patientId')).first_name
            appointment.status=True
            appointment.save()
        return HttpResponseRedirect('admin-view-appointment')
    return render(request,'hospital/admin_add_appointment.html',context=mydict)



@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def admin_approve_appointment_view(request):
    #those whose approval are needed
    appointments=models.Appointment.objects.all()
    return render(request,'hospital/admin_approve_appointment.html',{'appointments':appointments})



@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def approve_appointment_view(request,pk):
    appointment=models.Appointment.objects.get(id=pk)
    appointmentForm=forms.AppointmentDoctorForm(instance=appointment)
    mydict={'appointmentForm':appointmentForm,}
    if request.method=='POST':
        appointmentForm=forms.AppointmentDoctorForm(request.POST, instance=appointment)
        if appointmentForm.is_valid():
            appointment=appointmentForm.save(commit=False)
            appointment.doctorId=request.POST.get('doctorId')
            appointment.doctorName=models.User.objects.get(id=request.POST.get('doctorId')).first_name
            appointment.save()
            appointments=models.Appointment.objects.all()
        return render(request,'hospital/admin_approve_appointment.html',{'appointments':appointments})
    return render(request,'hospital/admin_update_appointment.html',context=mydict)



@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def reject_appointment_view(request,pk):
    appointment=models.Appointment.objects.get(id=pk)
    appointment.delete()
    return redirect('admin-approve-appointment')
#---------------------------------------------------------------------------------
#------------------------ ADMIN RELATED VIEWS END ------------------------------
#---------------------------------------------------------------------------------

#---------------------------------------------------------------------------------
#------------------------ RECEPTIONIST RELATED VIEWS START ------------------------------
#---------------------------------------------------------------------------------







#---------------------------------------------------------------------------------
#------------------------ DOCTOR RELATED VIEWS END ------------------------------
#---------------------------------------------------------------------------------


#---------------------------------------------------------------------------------
#------------------------ DOCTOR RELATED VIEWS START ------------------------------
#---------------------------------------------------------------------------------
@login_required(login_url='doctorlogin')
@user_passes_test(is_doctor)
def doctor_dashboard_view(request):
    #for three cards
    patientcount=models.Pharmacy.objects.all().count()
    appointmentcount=models.Appointment.objects.all().filter(status=True,doctorId=request.user.id).count()
    patientdischarged=models.Prescription.objects.all().distinct().filter(doctorId=request.user.id).count()

    #for  table in doctor dashboard
    appointments=models.Appointment.objects.all().filter(status=True,doctorId=request.user.id).order_by('-id')
    patientid=[]
    for a in appointments:
        patientid.append(a.patientId)
    patients=models.Patient.objects.all().filter(user_id__in=patientid).order_by('-id')
    appointments=zip(appointments,patients)
    mydict={
    'patientcount':patientcount,
    'appointmentcount':appointmentcount,
    'patientdischarged':patientdischarged,
    'appointments':appointments,
    'doctor':models.Doctor.objects.get(user_id=request.user.id), #for profile picture of doctor in sidebar
    }
    return render(request,'hospital/doctor_dashboard.html',context=mydict)



@login_required(login_url='doctorlogin')
@user_passes_test(is_doctor)
def doctor_patient_view(request):
    mydict={
    'doctor':models.Doctor.objects.get(user_id=request.user.id), #for profile picture of doctor in sidebar
    }
    return render(request,'hospital/doctor_patient.html',context=mydict)



@login_required(login_url='doctorlogin')
@user_passes_test(is_doctor)
def doctor_view_patient_view(request):
    # patients=models.Patient.objects.all().filter(status=True,assignedDoctorId=request.user.id)
    patients=models.Patient.objects.all()
    doctor=models.Doctor.objects.get(user_id=request.user.id) #for profile picture of doctor in sidebar
    return render(request,'hospital/doctor_view_patient.html',{'patients':patients,'doctor':doctor})

@login_required(login_url='doctorlogin')
@user_passes_test(is_doctor)
def doctor_appointment_view(request):
    doctor=models.Doctor.objects.get(user_id=request.user.id) #for profile picture of doctor in sidebar
    return render(request,'hospital/doctor_appointment.html',{'doctor':doctor})



@login_required(login_url='doctorlogin')
@user_passes_test(is_doctor)
def doctor_view_appointment_view(request):
    doctor=models.Doctor.objects.get(user_id=request.user.id) #for profile picture of doctor in sidebar
    appointments=models.Appointment.objects.all().filter(doctorId=request.user.id)
    patientid=[]
    for a in appointments:
        patientid.append(a.patientId)
    patients=models.Patient.objects.all().filter(user_id__in=patientid)
    appointments=zip(appointments,patients)
    return render(request,'hospital/doctor_view_appointment.html',{'appointments':appointments,'doctor':doctor})



@login_required(login_url='doctorlogin')
@user_passes_test(is_doctor)
def doctor_delete_appointment_view(request):
    doctor=models.Doctor.objects.get(user_id=request.user.id) #for profile picture of doctor in sidebar
    appointments=models.Appointment.objects.all().filter(doctorId=request.user.id)
    patientid=[]
    for a in appointments:
        patientid.append(a.patientId)
    patients=models.Patient.objects.all().filter(user_id__in=patientid)
    appointments=zip(appointments,patients)
    return render(request,'hospital/doctor_delete_appointment.html',{'appointments':appointments,'doctor':doctor})



@login_required(login_url='doctorlogin')
@user_passes_test(is_doctor)
def delete_appointment_view(request,pk):
    appointment=models.Appointment.objects.get(id=pk)
    appointment.delete()
    doctor=models.Doctor.objects.get(user_id=request.user.id) #for profile picture of doctor in sidebar
    appointments=models.Appointment.objects.all().filter(status=True,doctorId=request.user.id)
    patientid=[]
    for a in appointments:
        patientid.append(a.patientId)
    patients=models.Patient.objects.all().filter(status=True,user_id__in=patientid)
    appointments=zip(appointments,patients)
    return render(request,'hospital/doctor_delete_appointment.html',{'appointments':appointments,'doctor':doctor})

@login_required(login_url='doctorlogin')
@user_passes_test(is_doctor)
def doctor_add_patientDetail_view(request):
    patientDetailsAdminForm=forms.PatientDetailsAdminForm()
    mydict={'patientDetailsAdminForm':patientDetailsAdminForm}
    if request.method=='POST':
        patientDetailsAdminForm = forms.PatientDetailsAdminForm(request.POST)
        if patientDetailsAdminForm.is_valid():
            patientDetailsAdmin=patientDetailsAdminForm.save(commit=False)
            patientDetailsAdmin.patientId=request.POST.get('patientId')
            patientDetailsAdmin.appointmentId=request.POST.get('appointmentId')
            patientDetailsAdmin.doctorId=request.POST.get('doctorId')
            patientDetailsAdmin.height=request.POST.get('height')
            patientDetailsAdmin.weight=request.POST.get('weight')
            patientDetailsAdmin.temperature=request.POST.get('temperature')
            patientDetailsAdmin.medical_history=request.POST.get('medical_history')
            patientDetailsAdmin.currentMedication=request.POST.get('currentMedication')
            patientDetailsAdmin.currentSymptoms=request.POST.get('currentSymptoms')
            patientDetailsAdmin.allergies=request.POST.get('allergies')
            patientDetailsAdmin.medicalConcerns=request.POST.get('medicalConcerns')
            patientDetailsAdmin.diagnosis=request.POST.get('diagnosis')
            patientDetailsAdmin.treatment=request.POST.get('treatment')
            patientDetailsAdmin.save()
            if patientDetailsAdmin.treatment=='Prescription':
                return redirect('doctor-add-prescription')
            
        return HttpResponseRedirect('doctor-view-patient-detail')
    return render(request,'hospital/doctor_add_patientdetails.html',context=mydict)

@login_required(login_url='doctorlogin')
@user_passes_test(is_doctor)
def doctor_patientDetail_view(request):
    patientDetails=models.PatientDetailsAdmin.objects.all()
    # .filter(doctorId=request.user.id)#for profile picture of doctor in sidebar
    return render(request,'hospital/doctor_view_patient_details.html',{'patientDetails':patientDetails})

@login_required(login_url='doctorlogin')
@user_passes_test(is_doctor)
def create_patientdetail_view(request,pk):    
    appointment=models.Appointment.objects.get(id=pk)    
    patientDetailForm=forms.PatientDetailsForm()
    if request.method=='POST':
        patientDetailForm=forms.PatientDetailsForm(request.POST)
        if patientDetailForm.is_valid():
            patientDetail=patientDetailForm.save(commit=False)
            patientDetail.appointmentId=pk
            patientDetail.patientId=appointment.patientId
            patientDetail.doctorId=appointment.doctorId
            patientDetail.save()
            return redirect('doctor-view-patient-detail')
    return render(request,'hospital/doctor_add_patient_details.html',{'patientDetailForm':patientDetailForm})

@login_required(login_url='doctorlogin')
@user_passes_test(is_doctor)
def doctor_add_prescription_view(request):
    prescriptionForm=forms.PrescriptionForm()
    mydict={'prescriptionForm':prescriptionForm,}
    if request.method=='POST':
        appointmentForm=forms.PrescriptionForm(request.POST)
        if appointmentForm.is_valid():
            appointment=appointmentForm.save(commit=False)
            appointment.doctorId=request.POST.get('doctorId')
            appointment.pharmacyId=request.POST.get('pharmacyId')
            appointment.patientId=request.POST.get('patientId')
            appointment.appointmentId=request.POST.get('appointmentId')
            appointment.doctorName=models.User.objects.get(id=request.POST.get('doctorId')).first_name
            appointment.pharmacyName=models.Pharmacy.objects.get(id=request.POST.get('pharmacyId')).name
            appointment.patientName=models.User.objects.get(id=request.POST.get('patientId')).first_name
            appointment.medicineName=request.POST.get('medicineName')
            appointment.dosageInstruction=request.POST.get('dosageInstruction')
            appointment.sideEffects=request.POST.get('sideEffects')
            appointment.status=False
            appointment.save()
        return HttpResponseRedirect('doctor-view-patient-detail')
    return render(request,'hospital/doctor_add_prescription.html',context=mydict)


#---------------------------------------------------------------------------------
#------------------------ DOCTOR RELATED VIEWS END ------------------------------
#---------------------------------------------------------------------------------






#---------------------------------------------------------------------------------
#------------------------ PATIENT RELATED VIEWS START ------------------------------
#---------------------------------------------------------------------------------
@login_required(login_url='patientlogin')
@user_passes_test(is_patient)
def patient_dashboard_view(request):
    patient=models.Patient.objects.get(user_id=request.user.id)
    # doctor=models.Doctor.objects.get(user_id=patient.assignedDoctorId)
    mydict={
    'symptoms':patient.address,
    'admitDate':patient.mobile,
    }
    return render(request,'hospital/patient_dashboard.html',context=mydict)



@login_required(login_url='patientlogin')
@user_passes_test(is_patient)
def patient_appointment_view(request):
    patient=models.Patient.objects.get(user_id=request.user.id) #for profile picture of patient in sidebar
    return render(request,'hospital/patient_appointment.html',{'patient':patient})



@login_required(login_url='patientlogin')
@user_passes_test(is_patient)
def patient_book_appointment_view(request):
    appointmentForm=forms.PatientAppointmentForm()
    patient=models.Patient.objects.get(user_id=request.user.id) #for profile picture of patient in sidebar
    message=None
    mydict={'appointmentForm':appointmentForm,'patient':patient,'message':message}
    if request.method=='POST':
        appointmentForm=forms.PatientAppointmentForm(request.POST)
        if appointmentForm.is_valid():
            print(request.POST.get('doctorId'))
            desc=request.POST.get('description')

            doctor=models.Doctor.objects.get(user_id=request.POST.get('doctorId'))
            
            if doctor.department == 'Cardiologist':
                if 'heart' in desc:
                    pass
                else:
                    print('else')
                    message="Please Choose Doctor According To Disease"
                    return render(request,'hospital/patient_book_appointment.html',{'appointmentForm':appointmentForm,'patient':patient,'message':message})


            if doctor.department == 'Dermatologists':
                if 'skin' in desc:
                    pass
                else:
                    print('else')
                    message="Please Choose Doctor According To Disease"
                    return render(request,'hospital/patient_book_appointment.html',{'appointmentForm':appointmentForm,'patient':patient,'message':message})

            if doctor.department == 'Emergency Medicine Specialists':
                if 'fever' in desc:
                    pass
                else:
                    print('else')
                    message="Please Choose Doctor According To Disease"
                    return render(request,'hospital/patient_book_appointment.html',{'appointmentForm':appointmentForm,'patient':patient,'message':message})

            if doctor.department == 'Allergists/Immunologists':
                if 'allergy' in desc:
                    pass
                else:
                    print('else')
                    message="Please Choose Doctor According To Disease"
                    return render(request,'hospital/patient_book_appointment.html',{'appointmentForm':appointmentForm,'patient':patient,'message':message})

            if doctor.department == 'Anesthesiologists':
                if 'surgery' in desc:
                    pass
                else:
                    print('else')
                    message="Please Choose Doctor According To Disease"
                    return render(request,'hospital/patient_book_appointment.html',{'appointmentForm':appointmentForm,'patient':patient,'message':message})

            if doctor.department == 'Colon and Rectal Surgeons':
                if 'cancer' in desc:
                    pass
                else:
                    print('else')
                    message="Please Choose Doctor According To Disease"
                    return render(request,'hospital/patient_book_appointment.html',{'appointmentForm':appointmentForm,'patient':patient,'message':message})





            appointment=appointmentForm.save(commit=False)
            appointment.doctorId=request.POST.get('doctorId')
            appointment.patientId=request.user.id #----user can choose any patient but only their info will be stored
            appointment.doctorName=models.User.objects.get(id=request.POST.get('doctorId')).first_name
            appointment.patientName=request.user.first_name #----user can choose any patient but only their info will be stored
            appointment.status=False
            appointment.save()
        return HttpResponseRedirect('patient-view-appointment')
    return render(request,'hospital/patient_book_appointment.html',context=mydict)





@login_required(login_url='patientlogin')
@user_passes_test(is_patient)
def patient_view_appointment_view(request):
    patient=models.Patient.objects.get(user_id=request.user.id) #for profile picture of patient in sidebar
    appointments=models.Appointment.objects.all().filter(patientId=request.user.id)
    return render(request,'hospital/patient_view_appointment.html',{'appointments':appointments,'patient':patient})


#------------------------ PATIENT RELATED VIEWS END ------------------------------
#---------------------------------------------------------------------------------








#---------------------------------------------------------------------------------
#------------------------ ABOUT US AND CONTACT US VIEWS START ------------------------------
#---------------------------------------------------------------------------------
def aboutus_view(request):
    return render(request,'hospital/aboutus.html')

def contactus_view(request):
    sub = forms.ContactusForm()
    if request.method == 'POST':
        sub = forms.ContactusForm(request.POST)
        if sub.is_valid():
            email = sub.cleaned_data['Email']
            name=sub.cleaned_data['Name']
            message = sub.cleaned_data['Message']
            send_mail(str(name)+' || '+str(email),message,settings.EMAIL_HOST_USER, settings.EMAIL_RECEIVING_USER, fail_silently = False)
            return render(request, 'hospital/contactussuccess.html')
    return render(request, 'hospital/contactus.html', {'form':sub})


#---------------------------------------------------------------------------------
#------------------------ ADMIN RELATED VIEWS END ------------------------------
#---------------------------------------------------------------------------------


#---------------------------------------------------------------------------------
#------------------------ PHARMACY ADMIN RELATED VIEWS START ------------------------------
#---------------------------------------------------------------------------------
@login_required(login_url='admin_pharmacylogin')
@user_passes_test(is_admin_pharmacy)
def admin_pharmacy_dashboard_view(request):
    #for both table in admin dashboard
    admin_pharmacy = models.AdminPharmacy.objects.get(user_id=request.user.id)
    pharmacyInvetory=models.PharmacyInventory.objects.all().filter(pharmacyId=admin_pharmacy.pharmacyId, status=True).order_by('-id')
    prescriptions=models.Prescription.objects.all().filter(pharmacyId=admin_pharmacy.pharmacyId).order_by('-id')
    #for three cards
    pharmacyInvetorycount=models.PharmacyInventory.objects.all().filter(pharmacyId=admin_pharmacy.pharmacyId).count()

    prescriptionscount=models.Prescription.objects.all().filter(pharmacyId=admin_pharmacy.pharmacyId).count()

    pendingadmin_pharmacycount=models.AdminPharmacy.objects.all().filter(pharmacyId=admin_pharmacy.pharmacyId, status=False).count()
    mydict={
    'pharmacyInvetory':pharmacyInvetory,
    'prescriptions':prescriptions,
    'pharmacyInvetorycount':pharmacyInvetorycount,
    'prescriptionscount':prescriptionscount,
    'pendingadmin_pharmacycount':pendingadmin_pharmacycount,
    }
    return render(request,'hospital/admin_pharmacy_dashboard.html',context=mydict)

@login_required(login_url='admin_pharmacylogin')
@user_passes_test(is_admin_pharmacy)
def admin_pharmacy_presciption(request):
    #for both table in admin dashboard
    admin_pharmacy = models.AdminPharmacy.objects.get(user_id=request.user.id)
    prescriptions=models.Prescription.objects.all().filter(pharmacyId=admin_pharmacy.pharmacyId).order_by('-id')

    mydict={
    'prescriptions':prescriptions,
    }
    return render(request,'admin_pharmacy_prescription_view.html',context=mydict)

@login_required(login_url='admin_pharmacylogin')
@user_passes_test(is_admin_pharmacy)
def admin_pharmacy_inventory_view(request):
    #for both table in admin dashboard
    admin_pharmacy = models.AdminPharmacy.objects.get(user_id=request.user.id)
    pharmacyInvetory=models.PharmacyInventory.objects.all().filter(pharmacyId=admin_pharmacy.pharmacyId, status=True).order_by('-id')

    mydict={
    'pharmacyInvetory':pharmacyInvetory
    }
    return render(request,'hospital/admin_pharmacy_inventory_view.html',context=mydict)

@login_required(login_url='admin_pharmacylogin')
@user_passes_test(is_admin_pharmacy)
def admin_add_pharmacy_inventory_view(request):
    pharmacyInventoryForm=forms.PharmacyInventoryForm()
    mydict={'pharmacyInventoryForm':pharmacyInventoryForm}
    if request.method=='POST':
        pharmacyInventoryForm=forms.PharmacyInventoryForm(request.POST)
        if pharmacyInventoryForm.is_valid():
            pharmacyInventoryForm=pharmacyInventoryForm.save(commit=False)
            pharmacyInventoryForm.status=True
            # appointment.doctorId=request.POST.get('doctorId')
            pharmacyInventoryForm.pharmacyId=request.POST.get('pharmacyId')
            # appointment.patientId=request.POST.get('patientId')
            # appointment.appointmentId=request.POST.get('appointmentId')
            # appointment.doctorName=models.User.objects.get(id=request.POST.get('doctorId')).first_name
            # appointment.pharmacyName=models.Pharmacy.objects.get(id=request.POST.get('pharmacyId')).name
            # appointment.patientName=models.User.objects.get(id=request.POST.get('patientId')).first_name
            # appointment.medicineName=request.POST.get('medicineName')
            # appointment.dosageInstruction=request.POST.get('dosageInstruction')
            # appointment.sideEffects=request.POST.get('sideEffects')
            # appointment.status=False
            pharmacyInventoryForm.save()
        return HttpResponseRedirect('admin-pharmacy-dashboard')
    return render(request,'hospital/doctor_add_prescription.html',context=mydict)

@login_required(login_url='admin_pharmacylogin')
@user_passes_test(is_admin_pharmacy)
def approve_prescription_view(request,pk):
    prescription=models.Prescription.objects.get(id=pk)
    prescription.status=True
    prescription.save()
    return redirect('admin-pharmacy-prescription')
#---------------------------------------------------------------------------------
#------------------------ PHARMACY ADMIN RELATED VIEWS END ------------------------------
#---------------------------------------------------------------------------------

