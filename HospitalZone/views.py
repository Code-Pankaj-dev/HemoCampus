from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.utils import timezone

from .models import Hospital, BloodRequest


# ======================================
# Hospital Dashboard
# ======================================

def hospital_dashboard(request):

    hospital = Hospital.objects.first()
    requests = BloodRequest.objects.all().order_by('-created_at')

    context = {
        "hospital": hospital,
        "requests": requests,
        "today": timezone.now(),

        "total_requests": requests.count(),
        "approved_requests": requests.filter(status="Approved").count(),
        "pending_requests": requests.filter(status="Pending").count(),
        "rejected_requests": requests.filter(status="Rejected").count(),

        "blood_units_received": sum(
            requests.filter(status="Approved").values_list("units", flat=True)
        ),

        "emergency_requests": requests.filter(
            priority="Emergency"
        ).count(),
    }

    return render(
        request,
        "HospitalPages/hospital_dashboard.html",
        context
    )


# ======================================
# Request Blood
# ======================================

def request_blood(request):

    hospital = Hospital.objects.first()

    return render(
        request,
        "HospitalPages/request_blood.html",
        {
            "hospital": hospital
        }
    )


# ======================================
# Emergency Request
# ======================================

def emergency_request(request):

    hospital = Hospital.objects.first()

    return render(
        request,
        "HospitalPages/emergency_request.html",
        {
            "hospital": hospital
        }
    )


# ======================================
# Blood Availability
# ======================================

def blood_availability(request):

    return render(
        request,
        "HospitalPages/blood_availability.html"
    )


# ======================================
# My Requests
# ======================================

def my_requests(request):

    requests = BloodRequest.objects.all().order_by("-created_at")

    return render(
        request,
        "HospitalPages/my_requests.html",
        {
            "requests": requests
        }
    )


# ======================================
# Request History
# ======================================

def request_history(request):

    requests = BloodRequest.objects.all().order_by("-created_at")

    return render(
        request,
        "HospitalPages/request_history.html",
        {
            "requests": requests
        }
    )


# ======================================
# Notifications
# ======================================

def notifications(request):

    return render(
        request,
        "HospitalPages/notifications.html"
    )


# ======================================
# Hospital Profile
# ======================================

def hospital_profile(request):

    hospital = Hospital.objects.first()

    return render(
        request,
        "HospitalPages/profile.html",
        {
            "hospital": hospital
        }
    )


# ======================================
# Settings
# ======================================

def settings(request):

    return render(
        request,
        "HospitalPages/settings.html"
    )


# ======================================
# Download Report
# ======================================

def download_report(request):

    requests = BloodRequest.objects.all()

    return render(
        request,
        "HospitalPages/download_report.html",
        {
            "requests": requests
        }
    )


# ======================================
# Logout
# ======================================

def logout_view(request):

    logout(request)

    return redirect("/")