from django.contrib import admin

# Register your models here.
from main.models import *

admin.site.register(UserProfile)
admin.site.register(Log)
admin.site.register(DoctorProfile)
admin.site.register(Clinic)