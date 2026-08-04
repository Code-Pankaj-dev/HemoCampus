from django.db import models


class Hospital(models.Model):
    hospital_name = models.CharField(max_length=200)
    registration_no = models.CharField(max_length=100, unique=True)

    doctor_name = models.CharField(max_length=100)

    email = models.EmailField(unique=True)

    phone = models.CharField(max_length=15)

    address = models.TextField()

    district = models.CharField(max_length=100)

    state = models.CharField(max_length=100)

    logo = models.ImageField(upload_to='hospital_logo/', blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.hospital_name


# ===========================================
# Blood Request
# ===========================================

class BloodRequest(models.Model):

    STATUS = (
        ('Pending', 'Pending'),
        ('Approved', 'Approved'),
        ('Rejected', 'Rejected'),
    )

    PRIORITY = (
        ('Normal', 'Normal'),
        ('Emergency', 'Emergency'),
    )

    BLOOD_GROUP = (
        ('A+', 'A+'),
        ('A-', 'A-'),
        ('B+', 'B+'),
        ('B-', 'B-'),
        ('AB+', 'AB+'),
        ('AB-', 'AB-'),
        ('O+', 'O+'),
        ('O-', 'O-'),
    )

    hospital = models.ForeignKey(
        Hospital,
        on_delete=models.CASCADE
    )

    patient_name = models.CharField(max_length=100)

    blood_group = models.CharField(
        max_length=5,
        choices=BLOOD_GROUP
    )

    units = models.PositiveIntegerField()

    required_date = models.DateField()

    priority = models.CharField(
        max_length=20,
        choices=PRIORITY,
        default='Normal'
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS,
        default='Pending'
    )

    remarks = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.patient_name} ({self.blood_group})"