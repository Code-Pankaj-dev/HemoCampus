from django.db import models


# ==========================================
# Donor Profile
# ==========================================

class Donor(models.Model):

    GENDER = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
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

    full_name = models.CharField(max_length=150)
    gender = models.CharField(max_length=10, choices=GENDER)
    blood_group = models.CharField(max_length=5, choices=BLOOD_GROUP)

    date_of_birth = models.DateField()

    age = models.PositiveIntegerField()

    mobile = models.CharField(max_length=15)

    email = models.EmailField(unique=True)

    address = models.TextField()

    city = models.CharField(max_length=100)

    state = models.CharField(max_length=100)

    profile_photo = models.ImageField(
        upload_to='donor_photo/',
        blank=True,
        null=True
    )

    reward_points = models.PositiveIntegerField(default=0)

    total_donations = models.PositiveIntegerField(default=0)

    last_donation_date = models.DateField(
        blank=True,
        null=True
    )

    next_eligible_date = models.DateField(
        blank=True,
        null=True
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name


# ==========================================
# Donation History
# ==========================================

class DonationHistory(models.Model):

    STATUS = (
        ('Pending', 'Pending'),
        ('Approved', 'Approved'),
        ('Rejected', 'Rejected'),
    )

    donor = models.ForeignKey(
        Donor,
        on_delete=models.CASCADE
    )

    donation_date = models.DateField()

    hospital_name = models.CharField(max_length=150)

    units = models.PositiveIntegerField()

    blood_group = models.CharField(max_length=5)

    status = models.CharField(
        max_length=20,
        choices=STATUS,
        default='Pending'
    )

    remarks = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.hospital_name


# ==========================================
# Blood Request
# ==========================================

class DonorBloodRequest(models.Model):

    STATUS = (
        ('Pending', 'Pending'),
        ('Approved', 'Approved'),
        ('Rejected', 'Rejected'),
    )

    donor = models.ForeignKey(
        Donor,
        on_delete=models.CASCADE
    )

    hospital_name = models.CharField(max_length=150)

    blood_group = models.CharField(max_length=5)

    required_units = models.PositiveIntegerField()

    requested_date = models.DateField()

    status = models.CharField(
        max_length=20,
        choices=STATUS,
        default='Pending'
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.hospital_name


# ==========================================
# Notifications
# ==========================================

class DonorNotification(models.Model):

    donor = models.ForeignKey(
        Donor,
        on_delete=models.CASCADE
    )

    title = models.CharField(max_length=200)

    message = models.TextField()

    is_read = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title