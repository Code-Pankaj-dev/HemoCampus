from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import logout
from django.contrib.auth.models import User
from AdminZone.models import (ContactModel,DonateBloodModel,RequestBloodModel,DonorRegisterModel,LoginModel)
from django.contrib.auth.decorators import login_required
from HospitalZone.models import Hospital
from django.shortcuts import redirect, render
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages


# ===========================
# Website Views
# ===========================

def home(request):
    return render(request, "index.html")


def about(request):
    return render(request, "About_Us.html")


def blood_availability(request):
    return render(request, "Blood_Availabilite.html")


def blood_center_directory(request):
    return render(request, "Blood_Center_Directory.html")


def camp_schedule(request):
    return render(request, "Camp_Schedule.html")



def donate(request):
    return render(request, "Donate_blood.html")


def request_blood(request):
    return render(request, "Request_Blood.html")


def contact(request):
    return render(request, "Contact_Us.html")

def hospital_registration(request):
    return render(request,'hospital_registration.html')

def login(request):
    return render(request, "login.html")

def loginCode(request):

    if request.method == "POST":

        username = request.POST.get("username")
        password = request.POST.get("password")
        role=request.POST.get("role")

        data=LoginModel.objects.filter(email=username,password=password,role=role)
        if (data.exists()):
            role=data.first().role
            if(role=='admin'):
                request.session['aid']=username
                return HttpResponse("<script>alert('Welcome to Admin Zone');window.location.href='/Admin_Dashboard/'</script>")
            elif(role=='donor'):
                request.session['aid'] = username
                return HttpResponse("<script>alert('Welcome to Donor Zone');window.location.href='/donor-dashboard/'</script>")
            elif(role=='hospital'):
                request.session['aid'] = username
                return HttpResponse("<script>alert('Welcome to Hospital ');window.location.href='/hospital-dashboard/'</script>")
        else:
            return HttpResponse("<script>alert('Invalid UserId or Password');window.location.href='/login'</script>")

def register(request):
    return render(request, "register.html")


# ===========================
# Settings
# ===========================

@login_required
def settings(request):
    return render(request, "AdminPages/settings.html")




def logout_view(request):
    logout(request)
    return redirect("login")


# ===========================
# Contact Form
# ===========================

def contectdata(request):

    if request.method == "POST":

        ContactModel.objects.create(
            name=request.POST.get("fullname"),
            mob=request.POST.get("phone"),
            email=request.POST.get("email"),
            request_type=request.POST.get("request_type"),
            blood_group=request.POST.get("blood_group"),
            msg=request.POST.get("message"),
        )

        return HttpResponse(
            "<script>alert('Thanks For Contacting Us');window.location.href='/contact/'</script>"
        )

    return HttpResponse(
        "<script>alert('Data Not Submitted');window.location.href='/contact/'</script>"
    )


# ===========================
# Donate Blood
# ===========================

def DonateBloodData(request):

    if request.method == "POST":

        DonateBloodModel.objects.create(
            name=request.POST.get("name"),
            age=request.POST.get("age"),
            phone=request.POST.get("phone"),
            email=request.POST.get("email"),
            blood_group=request.POST.get("blood_group"),
            weight=request.POST.get("weight"),
            address=request.POST.get("address"),
            last_donation=request.POST.get("last_donation"),
            hemoglobin=request.POST.get("hemoglobin"),
        )

        return HttpResponse(
            "<script>alert('Thank You For Donating Blood ❤️');window.location.href='/donate/'</script>"
        )

    return HttpResponse(
        "<script>alert('Data Not Submitted');window.location.href='/donate/'</script>"
    )


# ===========================
# Request Blood
# ===========================

def RequestBloodData(request):

    if request.method == "POST":

        RequestBloodModel.objects.create(
            blood_group=request.POST.get("blood_group"),
            units_needed=request.POST.get("units_needed"),
            urgency=request.POST.get("urgency"),
            patient_name=request.POST.get("patient_name"),
            required_by=request.POST.get("required_by"),
            contact_phone=request.POST.get("contact_phone"),
            hospital_name=request.POST.get("hospital_name"),
            hospital_address=request.POST.get("hospital_address"),
        )

        return HttpResponse(
            "<script>alert('Blood Request Submitted Successfully');window.location.href='/request-blood/'</script>"
        )

    return HttpResponse(
        "<script>alert('Data Not Submitted');window.location.href='/request-blood/'</script>"
    )

# ===========================
# Donor Registration
# ===========================

def DonorRegisterData(request):

    if request.method == "POST":

        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")

        if password != confirm_password:
            return HttpResponse(
                "<script>alert('Password and Confirm Password do not match');window.location.href='/register/'</script>"
            )

        username = request.POST.get("username")

        if User.objects.filter(username=username).exists():
            return HttpResponse(
                "<script>alert('Username already exists');window.location.href='/register/'</script>"
            )

        # Create Django User
        user = User.objects.create_user(
            username=username,
            email=request.POST.get("email"),
            password=password
        )

        # Create Donor Profile
        DonorRegisterModel.objects.create(

            user=user,

            full_name=request.POST.get("full_name"),
            gender=request.POST.get("gender"),
            dob=request.POST.get("dob"),
            age=request.POST.get("age"),

            blood_group=request.POST.get("blood_group"),
            weight=request.POST.get("weight"),

            mobile=request.POST.get("mobile"),
            email=request.POST.get("email"),

            state=request.POST.get("state"),
            city=request.POST.get("city"),
            pincode=request.POST.get("pincode"),

            address=request.POST.get("address"),

            last_donation=request.POST.get("last_donation") or None,
            hemoglobin=request.POST.get("hemoglobin") or None,

            disease=request.POST.get("disease"),
            disease_details=request.POST.get("disease_details"),

            medicine=request.POST.get("medicine"),
            previous_donation=request.POST.get("previous_donation"),
        )

        return HttpResponse(
            "<script>alert('Donor Registered Successfully');window.location.href='/login/'</script>"
        )

    return HttpResponse(
        "<script>alert('Data Not Submitted');window.location.href='/register/'</script>"
    )


from django.contrib.auth import update_session_auth_hash

def LogoutPage(request):
    del request.session["aid"]
    return HttpResponse(
        "<script>alert('Logout');window.location.href='/login/'</script>"
    )



def hospital_registration(request):
    if request.method == "POST":
        print("View Called")
        print(request.POST)

        hospital = Hospital(
            hospital_name=request.POST.get("hospital_name"),
            email=request.POST.get("email"),
            phone=request.POST.get("phone"),
            address=request.POST.get("address"),
            username=request.POST.get("username"),
            password=request.POST.get("password"),
            agree=request.BooleanField(default=False)
        )

        hospital.save()
        print("Hospital Saved Successfully")

        return redirect("hospital_login")

    return render(request, "hospital_registration.html")