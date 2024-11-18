from django import forms
from .models import Appointment


class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['patient_name', 'doctorSelect', 'appointmentDate', 'appointmentTime']

        widgets = {
            'appointmentDate': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'appointmentTime': forms.TimeInput(attrs={'type': 'time', 'class': 'form-control'}),
            'patient_name': forms.TextInput(attrs={'class': 'form-control'}),
            'doctorSelect': forms.Select(attrs={'class': 'form-control'}),
        }

        labels = {
            'patient_name': 'Patient Name',
            'doctorSelect': 'Select Doctor',
            'appointmentDate': 'Date of Appointment',
            'appointmentTime': 'Time of Appointment',
        }

        help_texts = {
            'appointmentDate': 'Select a preferred date for the appointment.',
            'appointmentTime': 'Select a preferred time for the appointment.',
        }
