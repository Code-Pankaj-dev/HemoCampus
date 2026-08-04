from django.contrib import admin

from .models import (
    ContactModel,
    DonateBloodModel,
    RequestBloodModel,
    DonorRegisterModel,
LoginModel,
)

admin.site.register(ContactModel)
admin.site.register(DonateBloodModel)
admin.site.register(RequestBloodModel)
admin.site.register(DonorRegisterModel)
admin.site.register(LoginModel)