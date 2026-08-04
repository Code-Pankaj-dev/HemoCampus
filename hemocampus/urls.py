from django.contrib import admin
from django.contrib.auth.views import LoginView
from django.urls import path, include

from AdminZone import views as ad
from Home import views


urlpatterns = [

    path('admin/', admin.site.urls),

    path('', include('Home.urls')),
    path('login/', views.login, name='login'),
    path('loginCode/',views.loginCode, name='loginCode'),

path('hospital_registration/',views.hospital_registration, name='hospital_registration'),

    # =========================
    # Admin Dashboard
    # =========================

    path('Admin_Dashboard/', ad.dashboard, name='dashboard'),

    path('Blood_Stock/', ad.blood_stock, name='blood_stock'),

    path('Manage_Request/', ad.manage_request, name='manage_request'),

    path('Manage_Donors/', ad.manage_donors, name='manage_donors'),

    path('Report_Analytics/', ad.reports_analytics, name='reports_analytics'),

    path('Setting/', views.settings, name='setting'),

    path('change_password/', ad.change_password, name='change_password'),



    path('register/', views.register, name='register'),

path('hospital-dashboard/', include('HospitalZone.urls')),

path('donor-dashboard/', include('DonorZone.urls')),
# path('donor-dashboard/', include('DonorZone.urls')),
    path('LogoutPage/',views.LogoutPage),

]