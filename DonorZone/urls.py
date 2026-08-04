from django.urls import path
from . import views

urlpatterns = [

    # ======================================
    # Dashboard
    # ======================================

    path(
        '',
        views.donor_dashboard,
        name='donor_dashboard'
    ),

    # ======================================
    # My Profile
    # ======================================

    path(
        'my-profile/',
        views.my_profile,
        name='my_profile'
    ),

    # ======================================
    # Donate Blood
    # ======================================

    path(
        'donate-blood/',
        views.donate_blood,
        name='donate_blood'
    ),

    # ======================================
    # Donation History
    # ======================================

    path(
        'donation-history/',
        views.donation_history,
        name='donation_history'
    ),

    # ======================================
    # Blood Requests
    # ======================================

    path(
        'blood-requests/',
        views.blood_requests,
        name='blood_requests'
    ),

    # ======================================
    # Blood Availability
    # ======================================

    path(
        'blood-availability/',
        views.blood_availability,
        name='donor_blood_availability'
    ),

    # ======================================
    # Notifications
    # ======================================

    path(
        'notifications/',
        views.notifications,
        name='donor_notifications'
    ),

    # ======================================
    # Settings
    # ======================================

    path(
        'settings/',
        views.settings,
        name='donor_settings'
    ),

    # ======================================
    # Help & Support
    # ======================================

    path(
        'help-support/',
        views.help_support,
        name='help_support'
    ),
    path('settings/', views.settings, name='settings'),

    # ======================================
    # Logout
    # ======================================

    path(
        'logout/',
        views.logout_view,
        name='donor_logout'
    ),

]