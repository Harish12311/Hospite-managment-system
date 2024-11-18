"""
URL configuration for hospitel_management project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from hospitel_management_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.mainpage, name='mainpage'),
    path('mainpage/', views.mainpage, name='mainpage'),
    path('doctor1/', views.doctor1, name='doctor1'),
    path('deshbord/', views.deshbord, name='deshbord'),
    path('loginUser/', views.loginUser, name='loginUser'),  # Ensure this view does not require login
    path('registarUser/', views.registarUser, name='registarUser'),
    path('user_appointment_booking/', views.user_appointment_booking, name='user_appointment_booking'),
    path('user_data/', views.user_data, name='user_data'),
    path('hospitle_Billing/', views.hospitle_Billing, name='hospitle_Billing'),
    path('hospite_billing_print/', views.hospite_billing_print, name='hospite_billing_print'),
    path('report/', views.report, name='report'),
    path('report_doctor/', views.report_doctor, name='report_doctor'),
    path('logoutPage',views.logoutPage,name='logoutPage'),

]
