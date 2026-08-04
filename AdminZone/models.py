from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import User
from django.db import IntegrityError

# Create your models here.

class ContactModel(models.Model):
    name = models.CharField(max_length=100)
    mob = models.CharField(max_length=15)
    email = models.EmailField()
    request_type = models.CharField(max_length=100)
    blood_group = models.CharField(max_length=10)
    msg = models.TextField()

    def __str__(self):
        return self.name


class DonateBloodModel(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    blood_group = models.CharField(max_length=10)
    weight = models.IntegerField()
    address = models.TextField()
    last_donation = models.DateField(null=True, blank=True)
    hemoglobin = models.DecimalField(max_digits=4, decimal_places=1, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    status=models.CharField(max_length=60,blank=True)



class RequestBloodModel(models.Model):
    blood_group = models.CharField(max_length=10)
    units_needed = models.IntegerField()
    urgency = models.CharField(max_length=20)
    patient_name = models.CharField(max_length=100)
    required_by = models.DateField()
    contact_phone = models.CharField(max_length=15)
    hospital_name = models.CharField(max_length=100)
    hospital_address = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class DonorRegisterModel(models.Model):

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    full_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=20)
    dob = models.DateField()
    age = models.IntegerField()
    blood_group = models.CharField(max_length=5)
    weight = models.IntegerField()
    mobile = models.CharField(max_length=10)
    email = models.EmailField()
    state = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    pincode = models.CharField(max_length=10)
    address = models.TextField()
    last_donation = models.DateField(blank=True, null=True)
    hemoglobin = models.DecimalField(max_digits=4, decimal_places=1, blank=True, null=True)
    disease = models.CharField(max_length=20)
    disease_details = models.TextField(blank=True)
    medicine = models.CharField(max_length=20)
    previous_donation = models.CharField(max_length=20)

    def __str__(self):
        return self.full_name

class LoginModel(models.Model):
    role=models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=100)