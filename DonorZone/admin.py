from django.contrib import admin
from .models import (
    Donor,
    DonationHistory,
    DonorBloodRequest,
    DonorNotification,
)

admin.site.register(Donor)
admin.site.register(DonationHistory)
admin.site.register(DonorBloodRequest)
admin.site.register(DonorNotification)