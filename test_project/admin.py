from django.contrib import admin
from .models import Measurement, Participant

# Register your models here.


admin.site.register(Participant)
admin.site.register(Measurement)