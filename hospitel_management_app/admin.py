from django.contrib import admin
from .models import Hospitle_Billing, Report_doctor


class HospitleBillingAdmin(admin.ModelAdmin):
    list_display = ('patientName', 'patientID', 'admissionDate', 'dischargeDate',
                    'serviceDescription', 'totalAmount', 'discount', 'netAmount',
                    'paymentMethod', 'transactionID')


class ReportDoctorAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'gender', 'admissionDate', 'phone', 'email',
                    'address', 'diagnosis', 'treatmentPlan', 'Medication',
                    'dosage', 'frequency', 'doctorNotes')


# Registering both models with their respective admin classes
admin.site.register(Hospitle_Billing, HospitleBillingAdmin)
admin.site.register(Report_doctor, ReportDoctorAdmin)
