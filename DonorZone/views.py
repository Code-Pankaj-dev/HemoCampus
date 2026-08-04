from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import logout
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages

from .models import (
    Donor,
    DonationHistory,
    DonorBloodRequest,
    DonorNotification
)
# =========Donor Dashboard==========#

def donor_dashboard(request):
    if request.session.has_key('aid'):
        donor = Donor.objects.first()
        donations = DonationHistory.objects.all().order_by('-created_at')
        blood_requests = DonorBloodRequest.objects.all().order_by('-created_at')
        notifications = DonorNotification.objects.all().order_by('-created_at')[:5]
        context = {
            "donor": donor,
            "today": timezone.now(),
            "donations": donations,
            "blood_requests": blood_requests,
            "notifications": notifications,
            "total_donations": donations.count(),
            "approved_donations": donations.filter(status="Approved").count(),
            "pending_donations": donations.filter(status="Pending").count(),
            "rejected_donations": donations.filter(status="Rejected").count(),
            "reward_points": donor.reward_points if donor else 0,
        }
        return render(
            request,
            "DonorPages/Donor_dashboard.html",
            context
        )
    else:
        return HttpResponse(
            "<script>alert('First Login');window.location.href='/login'</script>"
        )


# ==========================================
# My Profile
# ==========================================

def my_profile(request):

    donor = Donor.objects.first()

    return render(request, "DonorPages/profile.html",{"donor": donor})


# ==========================================
# Donate Blood
# ==========================================

def donate_blood(request):

    donor = Donor.objects.first()

    return render(
        request,
        "DonorPages/donate_blood.html",
        {
            "donor": donor
        }
    )


# ==========================================
# Donation History
# ==========================================

def donation_history(request):

    donations = DonationHistory.objects.all().order_by('-created_at')

    return render(
        request,
        "DonorPages/donation_history.html",
        {
            "donations": donations
        }
    )


# ==========================================
# Blood Requests
# ==========================================

def blood_requests(request):

    requests = DonorBloodRequest.objects.all().order_by('-created_at')

    return render(
        request,
        "DonorPages/blood_requests.html",
        {
            "requests": requests
        }
    )


# ==========================================
# Blood Availability
# ==========================================

def blood_availability(request):

    return render(
        request,
        "DonorPages/blood_availability.html"
    )


# ==========================================
# Notifications
# ==========================================

def notifications(request):

    notifications = DonorNotification.objects.all().order_by('-created_at')

    return render(
        request,
        "DonorPages/notifications.html",
        {
            "notifications": notifications
        }
    )


# ==========================================
# Settings
# ==========================================

def settings(request):
    if request.session.has_key('aid'):
     donor = Donor.objects.first()
     return render(request,"DonorPages/settings.html",{"donor": donor })
    else:
        return HttpResponse("<script>alert('First Login');window.location.href='/login'</script>")


# ==========================================
# Help & Support
# ==========================================

def help_support(request):

    return render(
        request,
        "DonorPages/help_support.html"
    )


# ==========================================
# Logout
# ==========================================

def logout_view(request):

    logout(request)

    return redirect("/")



# ==========================================
# Change Password
# ==========================================

