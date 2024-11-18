from django.db import models
from django.core.exceptions import ValidationError


class UserRegister(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    password = models.CharField(max_length=128)  # 128 is recommended for hashed passwords
    confirm_password = models.CharField(max_length=128)

    def save(self, *args, **kwargs):
        if self.password != self.confirm_password:
            raise ValidationError("Passwords do not match.")
        # Hash the password
        self.set_password(self.password)
        super(UserRegister, self).save(*args, **kwargs)

    def set_password(self, raw_password):
        # Hashes the password using Django's `make_password`
        from django.contrib.auth.hashers import make_password
        self.password = make_password(raw_password)

    def __str__(self):
        return self.email


class Appointment(models.Model):
    patient_name = models.CharField(max_length=100)
    doctorSelect = models.CharField(max_length=100)
    appointmentDate = models.DateField()
    appointmentTime = models.TimeField()
    accept = models.BooleanField(default=False)
    cancel = models.BooleanField(default=False)


class Hospitle_Billing(models.Model):
    patientName = models.CharField(max_length=100)
    patientID = models.BigIntegerField()
    admissionDate = models.DateField()
    dischargeDate = models.DateField()
    serviceDescription = models.CharField(max_length=100)
    totalAmount = models.BigIntegerField()
    discount = models.BigIntegerField()
    netAmount = models.BigIntegerField()
    paymentMethod = models.CharField(max_length=10000)
    transactionID = models.BigIntegerField()


class Report_doctor(models.Model):
    name = models.CharField(max_length=100)
    age = models.BigIntegerField()
    gender = models.CharField(max_length=100)
    admissionDate = models.DateField()
    phone = models.BigIntegerField()
    email = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    diagnosis = models.CharField(max_length=100)
    treatmentPlan = models.CharField(max_length=100)
    Medication = models.CharField(max_length=100)
    dosage = models.CharField(max_length=100)
    frequency = models.CharField(max_length=100)
    doctorNotes = models.CharField(max_length=200)
