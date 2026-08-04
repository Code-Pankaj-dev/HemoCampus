from django.urls import path
from . import views

urlpatterns = [

    # ==========================
    # Dashboard
    # ==========================
    path(
        '',
        views.hospital_dashboard,
        name='hospital_dashboard'
    ),

    # ==========================
    # Blood Request
    # ==========================
    path(
        'request-blood/',
        views.request_blood,
        name='request_blood'
    ),

    # ==========================
    # Emergency Blood Request
    # ==========================
    path(
        'emergency-request/',
        views.emergency_request,
        name='emergency_request'
    ),

    # ==========================
    # Blood Availability
    # ==========================
    path(
        'blood-availability/',
        views.blood_availability,
        name='hospital_blood_availability'
    ),

    # ==========================
    # My Requests
    # ==========================
    path(
        'my-requests/',
        views.my_requests,
        name='my_requests'
    ),

    # ==========================
    # Request History
    # ==========================
    path(
        'request-history/',
        views.request_history,
        name='request_history'
    ),

    # ==========================
    # Notifications
    # ==========================
    path(
        'notifications/',
        views.notifications,
        name='hospital_notifications'
    ),

    # ==========================
    # Hospital Profile
    # ==========================
    path(
        'profile/',
        views.hospital_profile,
        name='hospital_profile'
    ),

    # ==========================
    # Settings
    # ==========================
    path(
        'settings/',
        views.settings,
        name='hospital_settings'
    ),

    # ==========================
    # Download Report
    # ==========================
    path(
        'download-report/',
        views.download_report,
        name='download_report'
    ),

    # ==========================
    # Logout
    # ==========================
    path(
        'logout/',
        views.logout_view,
        name='hospital_logout'
    ),

]