from django.shortcuts import render, redirect
from .models import UserRegister, Appointment, Hospitle_Billing, Report_doctor
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def mainpage(request):
    return render(request, 'mainpage.html')


@login_required(login_url='loginUser')
def doctor1(request):
    userdata = Appointment.objects.all()
    return render(request, 'doctor_accept_request.html', {'userdata': userdata})


@login_required(login_url='loginUser')
def deshbord(request):
    return render(request, 'deshbord.html')


def registarUser(request):
    if request.method == 'POST':
        name1 = request.POST.get('name')
        email1 = request.POST.get('email')
        password1 = request.POST.get('password')
        confirm_password1 = request.POST.get('confirm_password')
        if password1 == confirm_password1:
            UserRegister.objects.create(
                full_name=name1,
                email=email1,
                password=password1  # Adjust as per secure practices
            )
            messages.success(request, 'Registration successful!')
            return redirect('loginUser')
        else:
            messages.error(request, 'Passwords do not match')
    return render(request, 'registarUser.html')


@login_required(login_url='loginUser')
def user_appointment_booking(request):
    if request.method == 'POST':
        patient_name1 = request.POST.get('patient_name')
        doctorSelect1 = request.POST.get('doctorSelect')
        appointmentDate1 = request.POST.get('appointmentDate')
        appointmentTime1 = request.POST.get('appointmentTime')
        accept1 = 'accept' in request.POST
        cancel1 = 'cancel' in request.POST
        Appointment.objects.create(
            patient_name=patient_name1,
            doctorSelect=doctorSelect1,
            appointmentDate=appointmentDate1,
            appointmentTime=appointmentTime1,
            accept=accept1,
            cancel=cancel1,
        )
        messages.success(request, 'Appointment booked successfully')
    return render(request, 'User_appointment_booking.html')


@login_required(login_url='loginUser')
def user_data(request):
    userdata = Appointment.objects.all()
    return render(request, 'patiends.html', {'userdata': userdata})


@login_required(login_url='loginUser')
def hospitle_Billing(request):
    if request.method == 'POST':
        patientName1 = request.POST.get('patientName')
        patientID1 = request.POST.get('patientID')
        admissionDate1 = request.POST.get('admissionDate')
        dischargeDate1 = request.POST.get('dischargeDate')
        serviceDescription1 = request.POST.get('serviceDescription')
        totalAmount1 = request.POST.get('totalAmount')
        discount1 = request.POST.get('discount')
        netAmount1 = request.POST.get('netAmount')
        paymentMethod1 = request.POST.get('paymentMethod')
        transactionID1 = request.POST.get('transactionID')
        Hospitle_Billing.objects.create(
            patientName=patientName1,
            patientID=patientID1,
            admissionDate=admissionDate1,
            dischargeDate=dischargeDate1,
            serviceDescription=serviceDescription1,
            totalAmount=totalAmount1,
            discount=discount1,
            netAmount=netAmount1,
            paymentMethod=paymentMethod1,
            transactionID=transactionID1
        )
        messages.success(request, 'Billing information saved successfully')
    return render(request, 'Hospitle_Billing.html')


@login_required(login_url='loginUser')
def hospite_billing_print(request):
    hospite_billing_print1 = Hospitle_Billing.objects.all()
    return render(request, 'hospite_billing_print.html', {'hospite_billing_print1': hospite_billing_print1})


@login_required(login_url='loginUser')
def report(request):
    if request.method == "POST":
        if 'accept' in request.POST:
            messages.success(request, 'Report saved successfully!')
        elif 'cancel' in request.POST:
            messages.error(request, 'Action cancelled.')
        return redirect('report')

    report_doctor1 = Report_doctor.objects.first()
    return render(request, 'Report.html', {'report_doctor1': report_doctor1})


@login_required(login_url='loginUser')
def report_doctor(request):
    if request.method == 'POST':
        name1 = request.POST.get('name')
        age1 = request.POST.get('age')
        gender1 = request.POST.get('gender')
        admissionDate1 = request.POST.get('admissionDate')
        phone1 = request.POST.get('phone')
        email1 = request.POST.get('email')
        address1 = request.POST.get('address')
        diagnosis1 = request.POST.get('diagnosis')
        treatmentPlan1 = request.POST.get('treatmentPlan')
        Medication1 = request.POST.get('Medication')
        dosage1 = request.POST.get('dosage')
        frequency1 = request.POST.get('frequency')
        doctorNotes1 = request.POST.get('doctorNotes')
        Report_doctor.objects.create(
            name=name1,
            age=age1,
            gender=gender1,
            admissionDate=admissionDate1,
            phone=phone1,
            email=email1,
            address=address1,
            diagnosis=diagnosis1,
            treatmentPlan=treatmentPlan1,
            Medication=Medication1,
            dosage=dosage1,
            frequency=frequency1,
            doctorNotes=doctorNotes1,
        )
        messages.success(request, 'Doctor report saved successfully')
    return render(request, 'report_doctor.html')


def loginUser(request):
    if request.method == 'POST':  # Change to 'POST' to process the login form data correctly
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('deshbord')
        else:
            messages.error(request, 'Invalid username or password')

    return render(request, 'loginUser.html')


def logoutPage(request):
    logout(request)

    return render(request, 'mainpage.html')
