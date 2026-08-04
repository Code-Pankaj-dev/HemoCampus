# from django.db import models
#
# class HospitalRegistration(models.Model):
#     hospital_name = models.CharField(max_length=200)
#     registration_no = models.CharField(max_length=100)
#     incharge_name = models.CharField(max_length=100)
#     hospital_type = models.CharField(max_length=50)
#     phone = models.CharField(max_length=10)
#     email = models.EmailField()
#     state = models.CharField(max_length=100)
#     city = models.CharField(max_length=100)
#     pincode = models.CharField(max_length=6)
#     address = models.TextField()
#     total_beds = models.IntegerField()
#     blood_bank_available = models.CharField(max_length=10)
#     license_certificate = models.FileField(upload_to="hospital_license/")
#     username = models.CharField(max_length=100)
#     password = models.CharField(max_length=100)
#
# # Create your models here.
